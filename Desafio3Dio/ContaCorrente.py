import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super.__init__(numero, cliente)
        self._LIMITE = 50000,00
        self._LIMITE_SAQUES = 3

    
    @property
    def limite(self):
        return self._LIMITE
    
    @property
    def limite_saque(self):
        return self._LIMITE_SAQUES
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in Historico().
             transacoes if transacao["tipo"] == Saque.
             __name__]
        )

        #5:20