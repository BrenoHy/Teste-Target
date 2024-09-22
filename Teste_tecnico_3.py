# Teste Técnico 3

import json

# Função para carregar os dados do arquivo JSON
def carregar_faturamento(arquivo):
    # Abrindo o arquivo e lendo seu conteúdo
    with open(arquivo, 'r') as f:
        dados = json.load(f) # Covertendo o conteúdo do arquivo par um objeto Python
    return dados

# Função para analisar os dados e calcular os valores solicitados

def analisar_faturamento(dados):
    faturamento_valido = [dia['valor'] for dia in dados if dia['valor'] > 0]  # Filtrando os dias que possuem faturamento

    # Calculo de menor e maior faturamento
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)

    # Calculo da média mensal de faturamento (ignorando os dias sem faturamento)
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)

    # Contando o número de dias com faturamento acima da média
    dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

    # Retorna os resultados
    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Função principal
def main():
    # Carregando os dados do arquivo JSON
    dados_faturamento = carregar_faturamento('dados.json')

    # Analisando os dados de faturamento
    menor, maior, dias_acima_media = analisar_faturamento(dados_faturamento)

    # Exibindo os resultados
    print(f"Menor valor de faturamento: R$ {menor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

# Executando o programa
if __name__ == '__main__':
    main()
