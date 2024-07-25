import requests
import validate_docbr as doc


class Cadastro:
    def __init__(self, nome, ra, cpf, cep):
        self.nome = nome
        self.ra = int(ra)
        self.cpf = str(cpf)
        self.cep = str(cep)

        # Validate CPF using the validate_docbr library
        if not doc.CPF().validate(self.cpf):
            raise ValueError("CPF is invalid")

    def mascara_cpf(self):
        # Format CPF using the validate_docbr library
        return doc.CPF().mask(self.cpf)

    def mascara_cep(self):
        if len(self.cep) == 8:
            g1 = self.cep[0:5]
            g2 = self.cep[5:8]
            return f"{g1}-{g2}"
        else:
            raise ValueError("CEP is invalid")

    def busca_cep(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        busca = requests.get(url)
        if busca.status_code == 200:
            conteudo = busca.json()
            logradouro = conteudo.get('logradouro', 'CEP invalido')
            bairro = conteudo.get('bairro', 'CEP invalido')
            estado = conteudo.get('uf', 'CEP invalido')
            return f"{logradouro} - {bairro} - {estado}"
        else:
            raise ValueError("Não foi possivel buscar informações sobre o CEP")

    def __str__(self) -> str:
        return f"{self.nome}, CPF: {self.mascara_cpf()}, RA: {self.ra}, CEP: {self.mascara_cep()}"


