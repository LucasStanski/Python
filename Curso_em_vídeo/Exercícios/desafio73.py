times=("Botafogo","Palmeiras","Fluminense",
       "Flamengo","Cruzeiro","Atletico-PR",
       "Fortaleza","São Paulo","Atlético-MG",
       "Santos","Grêmio","Internacional","Bahia",
       "Vasco","Bragança","Cuiabá","Corinthians",
       "Goiás","Coritiba","América-MG")
print("="*50)
print(f"Os primeiros colocados no brasileirão são:")
print(f"{times[0:5]}")
print("="*50)
print("Os quatro ultimos colocados são:")
print(f"{times[-4:]}")
times1=sorted(times)
print("="*50)
print(f"Os times em ordem alfabética são:")
print(f"{times1}")
print("="*50)
print(times[5],f"Está na posicão",times.index("Atletico-PR")+1)
print("="*50)
