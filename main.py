import sqlite3
import pandas as pd

#Ler CSV
df = pd.read_csv('cad_cia_aberta.csv', encoding='latin-1', on_bad_lines='warn', delimiter=';', index_col=0)
df = df.drop(columns=['DENOM_COMERC','DT_CONST',
       'MOTIVO_CANCEL', 'DT_INI_SIT', 'CD_CVM',
       'SETOR_ATIV', 'TP_MERC', 'CATEG_REG', 'DT_INI_CATEG', 'SIT_EMISSOR',
       'DT_INI_SIT_EMISSOR', 'CONTROLE_ACIONARIO', 'TP_ENDER', 'LOGRADOURO',
       'COMPL', 'BAIRRO', 'MUN', 'UF', 'PAIS', 'CEP', 'DDD_TEL', 'TEL',
       'DDD_FAX', 'FAX', 'EMAIL', 'TP_RESP', 'RESP', 'DT_INI_RESP',
       'LOGRADOURO_RESP', 'COMPL_RESP', 'BAIRRO_RESP', 'MUN_RESP', 'UF_RESP',
       'PAIS_RESP', 'CEP_RESP', 'DDD_TEL_RESP', 'TEL_RESP', 'DDD_FAX_RESP',
       'FAX_RESP', 'EMAIL_RESP', 'CNPJ_AUDITOR', 'AUDITOR'],)

df.columns = df.columns.str.strip()

#Conexão com SQL e criação da tabela dados
connection = sqlite3.connect('sparta.db')
cursor = connection.cursor()

df.to_sql('Dados', connection, if_exists='replace')

#Função de consulta de CNPJ
def buscar_dado():
    cnpj = input("Digite o CNPJ da empresa: ")
    cursor.execute("""SELECT CNPJ_CIA, DT_REG FROM Dados WHERE CNPJ_CIA = ?""", (cnpj,))
    dados = cursor.fetchall()
    if not dados:
        print("Nenhum CNPJ identificado")
        return
    datas_disponiveis = list(set(dado[1] for dado in dados))

    for index, data in enumerate(datas_disponiveis):
        print(f"\n{index + 1}. DT_REG: {data}\n")

    escolha = int(input("Selecione o número da data desejada: ")) - 1
    if 0 <= escolha < len(datas_disponiveis):
        data_selecionada = datas_disponiveis[escolha]
        cursor.execute("""SELECT * FROM Dados WHERE CNPJ_CIA = ? AND DT_REG = ?""", (cnpj, data_selecionada))
        registros = cursor.fetchall()

        print(f"\nRegistro(s) selecionado(s) para a data {data_selecionada}:")
        for registro in registros:
            print("CNPJ_CIA:", registro[0])
            print("DT_REG:", registro[1])
            print("SITUAÇÃO:", registro[2])
            print("OUTROS DADOS:", registro[3:], "\n")
    else:
       print("Erro ao selecionar data")

buscar_dado()
connection.close()