from src.model.buscar_promocoes import buscar_promocoes

try:
    df = buscar_promocoes('perfume')

    print(df)
    
except Exception as e:
    print(e)
    
finally:
    pass