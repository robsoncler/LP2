class Aluno:
    def __init__(self,nome='',email='',ra='',celular='',desconto=0.0):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
        self.__desconto = desconto
        self.__disciplinas = []

    def getNome(self):
        return self.__nome

    def setNome(self,nome):
        self.__nome = nome

    def getEmail(self):
        return self.__email

    def setEmail(self,email):
        self.__email = email

    def getRa(self):
        return self.__ra

    def getCelular(self):
        return self.__celular
    
    def setCelular(self,celular):
        self.__celular = celular

    def getDesconto(self):
        return self.__desconto
    
    def setDesconto(self,desconto):
        self.__desconto = desconto

    def getDisciplina(self):
        return self.__disciplinas

    def adicionaDisciplina(self,disciplina):
        self.__disciplinas.append(disciplina)

    def aumentaDesconto(self,porcentagem):
        self.__desconto = self.__desconto + porcentagem
    
    def diminuiDesconto(self,porcentagem):
        self.__desconto = self.__desconto - porcentagem

    def retornaSobrenome (self):
        return ' '.join(self.__nome.split(' ')[1:]) #pegar os Sobrenomes

    def retornaValorMensalidade(self):
        vtotal = 0
        for quantidade in self.__disciplinas:
            vtotal += quantidade.getMensalidade()
        return vtotal -((vtotal * self.__desconto)/100)



    def retornaCargaHoraria(self):
        soma_carga = 0
        for d in self.__disciplinas:
            soma_carga += d.getCargaHoraria()/20
            return soma_carga



    

    

    

    


