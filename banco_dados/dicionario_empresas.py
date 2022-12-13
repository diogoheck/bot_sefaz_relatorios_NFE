from openpyxl import load_workbook


def planilha():

    wb = load_workbook(
        'R:\Compartilhado\Fiscal\lista_clientes_sefaz\lista_clientes_sefaz.xlsx')

    ws = wb.active

    return ws


def criar_dicionario_empresas(plan):
    dic = {}
    lista = []
    cabecalho = True
    for linha in plan:
        if not cabecalho:
            dic[str(linha[4].value)] = str(linha[1].value)
        cabecalho = False
    return dic


if __name__ == '__main__':

    planilha = planilha()
    dic = criar_dicionario_empresas(planilha)
    print(dic)
