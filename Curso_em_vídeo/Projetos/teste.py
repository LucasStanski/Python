#ponto_flutuante=-45.6
#print("O valor absoluto é:",abs(ponto_flutuante))

class carro:
    def __init__(carro,óleo,pneu,estep):
        carro.óleo=óleo
        carro.pneu=pneu
        carro.step=estep
    
    def abrirPorta(self):
        print("Abrindo porta do carro.")
    
    def LigandoCarro(self):
        print("Ligando o carro.")
    
    def pilotar(self):
        print("Pode dirigir para onde quiser.")
    
    def exibirinformacaoescocarro(self):
        print(self.óleo,self.pneu,self.step)

carro1=carro("Checar óleo","Checar calibragem do pneu","Verificar o step")
carro1.exibirinformacaoescocarro()
carro1.abrirPorta()
carro1.LigandoCarro()
carro1.pilotar()
