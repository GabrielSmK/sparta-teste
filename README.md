# Teste Python - Sparta

## Passo a passo

1 - Execute o arquivo main.py

2 - Digite o CNPJ da empresa desejada

3 - Digite a data do registro que gostaria de exibir

### Exemplo

```bash
(Primeira mensagem exibida pelo console)
Digite o CNPJ da empresa: 47.509.120/0001-82 (dado inserido pelo usuário)

(Segunda mensagem exibida pelo console)

1. DT_REG: 1998-04-06


2. DT_REG: 1985-06-12


3. DT_REG: 2004-11-24

(Terceira mensagem exibida pelo console)

Selecione o número da data desejada: 3 (dado inserido pelo usuário)

(Quarta mensagem exibida pelo console)

Registro(s) selecionado(s) para a data 2004-11-24:
CNPJ_CIA: 47.509.120/0001-82
DT_REG: BRADESCO LEASING S.A. - ARRENDAMENTO MERCANTIL
SITUAÇÃO: 2004-11-24
OUTROS DADOS: (None, 'ATIVO')
```

## Tomada de decisão

Utilizei as bibliotecas pandas e sqlite3 para fazer a conexão e cadastro das informações no banco de dados do projeto, fiquei com dúvida em relação à descrição do projeto, pois requisitava uma consulta de cadastros antigos e atuais, mas não exigia a exibição das datas, portanto, resolvi exibi-las para manter melhor compreensão dos dados.
