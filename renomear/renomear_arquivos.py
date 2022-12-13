# -*- coding: cp1252 -*-
import os
import shutil
PASTA_RELATORIOS_SEFAZ = r'U:\SEFAZ\RELATORIO_NOTAS'


def criar_nova_pasta(caminho):
    os.makedirs(caminho)


def criar_dicionario_empresas():
    with open('empresas.csv', encoding='cp1252') as arquivo:
        dic_empresas = {}
        cabecalho = True
        for registro in arquivo:
            emp = registro.strip().split(';')
            if not cabecalho:
                dic_empresas[emp[4]] = emp
            cabecalho = False
    return dic_empresas


def renomear_arquivos(old_name, new_name):
    os.rename(old_name, new_name)


def copiar_arquivos(origem, destino):
    shutil.copyfile(origem, destino)


def renomear_relatorios_sefaz(lista_clientes):

    for diretorio, subpastas, arquivos in os.walk(PASTA_RELATORIOS_SEFAZ):

        for arquivo in arquivos:
            if arquivo != 'Thumbs.db':
                parte_inicial = os.path.join(
                    diretorio, arquivo).split(' ')[0:-2]
                CNPJ_meio = os.path.join(diretorio, arquivo).split(' ')[-2]
                parte_final = os.path.join(diretorio, arquivo).split(' ')[-1]
                old_name = os.path.join(diretorio, arquivo)
                new_name = f"{' '.join(parte_inicial)} {CNPJ_meio} {parte_final}"
                new_name = new_name.upper()
                new_name = new_name.replace('.PDF', '')
                renomear_arquivos(old_name, new_name)
                print(
                    f"{' '.join(parte_inicial)} {CNPJ_meio} {parte_final}")


if __name__ == '__main__':

    lista_clientes = {'30841034000170': 'Forte Tecnologia LTDA',
                      '18286080000159': 'Gomes & Hartmann LTDA'}
    # dic_empresas = criar_dicionario_empresas()
    renomear_relatorios_sefaz(lista_clientes)
