

def voto(data_nascimento=0):
    from datetime import datetime
    s=datetime.now().year-data_nascimento 
    if s<=16:
        return f"Com {s} anos: VOTO NEGADO!!!\n"
    elif 16<=s<18 or s>65:
        return f"Com {s} anos: VOTO OPCIONAL!!!\n"
    else:
        return f"com {s} anos: VOTO OBRIGATÓRIO!!!\n"
    
    
nascimento=int(input("\nEm que ano você nasceu?: "))
print(voto(nascimento))