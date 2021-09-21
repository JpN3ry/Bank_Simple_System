class ContaBlock(Exception):
    def __init__(self,msg):
        super().__init__(msg)


class conta:
    def __init__(self, agencia,conta):
        self.agencia = agencia
        self.conta = conta
        self.saldo = 0
        self.bloqueado = False
        self.digito = self.__geraDigito(conta)
    
    def sacar(self, valor):
        if self.bloqueado == True: # ERRO RAISE!
            raise ContaBlock('Sua conta está bloqueada!') # Força um erro para mostrar mensagem se a conta tiver block
        assert self.saldo - valor >= 0, 'Saldo insuficiente para saque'
        self.saldo -= valor
    
    # IGNORAR ESSE GERA DIGITO!
    def __geraDigito(self, conta):
        soma = 0
        for d in conta:  
            soma += int(d)  # Modo qualquer apenas para gerar um digito qualquer!
        return soma % 11
    
    def __str__(self):
        return f'Conta {self.conta}-{self.digito}, Agencia: {self.agencia}, Saldo: {self.saldo}'

    
if __name__ == '__main__':
    João = conta('1010', '4561')
    print(João)
    try:
        João.saldo = 1500
        João.bloqueado = False
        João.sacar(100)
        print(João)
    
    except AssertionError as ae:
        print(ae)
    except ContaBlock as CB:
        print(CB)


    

        

    


    
