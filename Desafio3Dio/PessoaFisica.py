class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereço):
        super().__init__(endereço)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        