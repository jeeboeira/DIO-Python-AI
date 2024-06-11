class Conta:
    import ContaCorrente
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._cliente = cliente
        self._historico = Historico()
        self._AGENCIA = "0001"
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero,cliente)
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._AGENCIA
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        #limite = Chamar Contacorrente.limite
        #excedeu_limite = valor > limite
        #excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    #elif excedeu_limite:
     #   print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    #elif excedeu_saques:
     #   print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    
    elif valor > 0:
        self._saldo -= valor
        #Chamar extrato
        #extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        #numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
        return True
    
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return False
    
    #return saldo, extrato
    
    def depositar(self, valor):
        if valor > 0:
            saldo += valor
            #extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
        return True
       
