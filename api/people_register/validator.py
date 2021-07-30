from validate_docbr import CPF
import re


def cpf_valido(num_cpf):
    cpf = CPF()
    return cpf.validate(num_cpf)


def nome_valido(nome):
    return all(x.isalpha() or x.isspace() for x in nome)


def celular_valido(celular):
    modelo ='[0-9]{2}[0-9]{5}[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta