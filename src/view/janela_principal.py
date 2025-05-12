import threading
import tkinter as tk
from tkinter import ttk
import webbrowser
from src.model.buscar_promocoes import buscar_promocoes

def janela_principal():
    
    def fazer_pesquisa():
        produto =  input_pesquisa.get()
        if produto == '':
            return
        
        input_pesquisa.delete(0, tk.END)
        
        def rodar_pesquisa():
            df = buscar_promocoes(produto)
        
            for widget in frame.winfo_children()[3:]:
                widget.destroy()
            
            row = 1
            
            for x in range(len(df)):
                linha = df.iloc[x]
                
                titulo = linha['Titulo']
                preco = linha['Preco']
                link = linha['Link']
                
                a = tk.Label(frame, text=f"{titulo}", font=("Arial", 12))    
                a.grid(row=row, column=0)
                
                b = tk.Label(frame, text=f"{preco}", font=("Arial", 12))    
                b.grid(row=row, column=1)
                
                def abrir_link(url=link):
                    webbrowser.open(url)

                c = tk.Label(frame, text=link, font=("Arial", 12), fg="blue", cursor="hand2")
                c.bind("<Button-1>", lambda e: abrir_link())
                c.grid(row=row, column=2)
                
                row += 1

        pesquisa_thread = threading.Thread(target=rodar_pesquisa)
        pesquisa_thread.start()
        
    raiz = tk.Tk()
    raiz.title("Buscar Promoções")
    raiz.state("zoomed")
    # raiz.resizable(False, False)
    
    raiz.grid_columnconfigure(0, weight=1)
    raiz.grid_columnconfigure(1, weight=1)
    
    titulo = tk.Label(raiz, text="Buscar Promoções", font=("Arial", 22))
    titulo.grid(row=0, column=0, columnspan=2, pady=(20, 0))
    
    input_pesquisa = tk.Entry(raiz, width=50, font=("Arial", 12))
    input_pesquisa.grid(row=1, column=0, pady=(10,0), sticky="e")
    
    botao_pesquisar = tk.Button(raiz, text="Pesquisar", font=("Arial", 12))
    botao_pesquisar.grid(row=1, column=1, pady=(10,0),padx=(10,0), sticky="w")
    
    
    # tabela = ttk.Treeview(raiz, columns=("Titulo", "Preco", "Link"), show="headings")
    # tabela.heading("Titulo", text="Título")
    # tabela.heading("Preco", text="Preço")
    # tabela.heading("Link", text="Link")

    # tabela.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    frame = tk.Frame(raiz)
    frame.grid(row=2, column=0, columnspan=2, pady=10, padx=20, sticky="we")
    
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)
    
    label_titulo = tk.Label(frame, text="Titulo", font=("Arial", 19))
    label_titulo.grid(row=0, column=0)
    
    label_preco = tk.Label(frame, text="Preço", font=("Arial", 19))
    label_preco.grid(row=0, column=1)
    
    label_link = tk.Label(frame, text="Link", font=("Arial", 19))
    label_link.grid(row=0, column=2)
    
    botao_pesquisar.config(command=fazer_pesquisa)
    
    raiz.mainloop()
    
if __name__ == "__main__":
    janela_principal()