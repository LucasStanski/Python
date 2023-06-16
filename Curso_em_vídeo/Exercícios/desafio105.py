def notas(*num,sit):
    dict={"Notas":len(num),"MaiorNota":max(num),"MenorNota":min(num),"Média":sum(num)/len(num)} 
    if sit==True:
        if dict["Média"] <=5.0:
            dict["Situação"]="RUIM!!!"
        if 5.0<=dict["Média"]<7.0:
            dict["Situação"]="DA PRA MELHORAR!!!"
        if dict["Média"]>=7.0:
            dict["Situação"]="PARABÉNS!!!"
    if sit==False:
        return dict
        quit()
    return dict
resp=notas(1,1,2,4.9, sit=True)
print()
print(resp)
print()