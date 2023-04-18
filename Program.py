import json

# Funçao para calcular a media
def percentual_faturado(valor, total):
    return (valor * 100) / total

# Declaraçao de dados
dados = {
            "SP": 67836.43,
            "RJ": 36678.66,
            "MG": 29229.88,
            "ES": 27165.48,
            "Outros": 19849.53
        }

# Busca o total faturado no mes
valor_total = sum(dados.values())
print(f'Valor Total do Faturamento da empresa: R$ {valor_total}\n')

# Busca o percentual de cada estado
lista_percentual = []
for dado in dados:
    estado = dados[dado]
    percentual = percentual_faturado(estado, valor_total)
    percentual = f'{percentual:_.2f}%'
    lista_percentual.append(percentual)

# Gera o novo dict com os percentuais correspondente a cada estado
percentual_dict = dict(zip(dados.keys(), lista_percentual))

# Convertendo para JSON e imprimindo
print(json.dumps(percentual_dict, indent=2))
