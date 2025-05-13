import pandas as pd
from unidecode import unidecode
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


dict_xpath = {
    "buscar": "/html/body/header/div/div[2]/form/input",
}

def buscar_promocoes(produto):
    print("inicio")
    
    df = pd.DataFrame(columns=['Titulo', 'Preco', 'Link'])

    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    navegador = webdriver.Chrome(options=op)
    navegador.get('https://www.mercadolivre.com.br/')
    navegador.maximize_window()

    WebDriverWait(navegador, timeout=30).until(EC.presence_of_element_located((By.XPATH, dict_xpath['buscar'])))
    navegador.find_element(By.XPATH, dict_xpath['buscar']).send_keys(produto, Keys.ENTER)

    posicao = 1

    while True:
        try:    
            WebDriverWait(navegador, timeout=10).until(EC.presence_of_element_located((By.XPATH, f"/html/body/main/div/div[2]/section/div[6]/ol/li[{posicao}]")))
            container_produto = navegador.find_element(By.XPATH, f"/html/body/main/div/div[2]/section/div[6]/ol/li[{posicao}]")
            classe = container_produto.get_attribute('class')

            if not classe == 'ui-search-layout__item--intervention':
                a_tag = container_produto.find_element(By.CLASS_NAME, "poly-component__title")
                titulo = a_tag.text
                link = a_tag.get_attribute('href')
                
                poly_price_current = container_produto.find_element(By.CLASS_NAME, 'poly-price__current')
                preco = poly_price_current.find_element(By.CLASS_NAME, 'andes-money-amount__fraction').text
                
                preco = int(str(preco).replace('.', ''))
                
                print(f"{unidecode(titulo)} -> {preco} pos: {posicao}")
                
                df.loc[len(df)] = [
                    titulo,
                    preco,
                    link
                ]

            posicao += 1

        except (NoSuchElementException, TimeoutException):
            break

        except Exception as e:
            posicao += 1
    
    navegador.close()
    navegador.quit()
    
    df_ordenado = df.sort_values(by='Preco')

    df_ordenado.to_excel("C:\\Users\\paulo.welton\\Desktop\\promo.xlsx", index=False)
    df_cortado = df_ordenado.head(20)
    
    return df_ordenado, df_cortado

if __name__ == '__main__':
    buscar_promocoes('tenis')
