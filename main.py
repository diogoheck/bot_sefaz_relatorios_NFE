from conexao.efetuar_conexao_site import conectar
from meus_servicos.modulo_servicos import acesso_modulo_servicos
from relatorios.consulta_relatorio_notas import *
from renomear.renomear_arquivos import renomear_relatorios_sefaz
from copiar_rede_relatorios.copiar_rede import copiar_relatorios_sefaz_rede
from banco_dados.dicionario_empresas import planilha, criar_dicionario_empresas
from gerar_extratos_notas.gerar_extratos import gerar_extratos_notas_fiscais

DT_inicial = '01/11/2022'
DT_final = '30/11/2022'


if __name__ == '__main__':

    planilha = planilha()
    lista_clientes = criar_dicionario_empresas(planilha)

    competencia = DT_inicial.split('/')
    competencia = competencia[1] + competencia[2]

    navegador = conectar()

    navegador = acesso_modulo_servicos(navegador)

    navegador = gerar_extratos_notas_fiscais(navegador,
                                             lista_clientes, DT_inicial, DT_final, competencia)

    print('*' * 50)
    print('finalizandoo')
    print('*' * 50)
    time.sleep(10)

    renomear_relatorios_sefaz(lista_clientes)
    copiar_relatorios_sefaz_rede(lista_clientes, competencia)

    print('finalizado com sucesso!')
