import time

dataset = [
    {"Título": "Artigo 1", "Resumo": "Resumo do Artigo 1. Ele fala sobre algoritmos."},
    {"Título": "Artigo 2", "Resumo": "Resumo do Artigo 2, que explora o design de algoritmos eficientes."},
    {"Título": "Artigo 3", "Resumo": "Resumo do Artigo 3, explora..."},
    {"Título": "Artigo 4", "Resumo": "Resumo do Artigo 4, explora algoritmos eficientes para suffux tree."},
    {"Título": "Artigo 5", "Resumo": "Resumo do Artigo 5, explora algoritmos."},
    {"Título": "Artigo 6", "Resumo": "Resumo do Artigo 6. Ele fala sobre algoritmos."},
    {"Título": "Artigo 7", "Resumo": "Resumo do Artigo 7, que explora o design de algoritmos eficientes."},
    {"Título": "Artigo 8", "Resumo": "Resumo do Artigo 8, explora..."},
    {"Título": "Artigo 9", "Resumo": "Resumo do Artigo 9, explora algoritmos eficientes para suffux tree."},
    {"Título": "Artigo 1", "Resumo": "Resumo do Artigo 1. Ele fala sobre algoritmos."},
    {"Título": "Artigo 2", "Resumo": "Resumo do Artigo 2, que explora o design de algoritmos eficientes."},
    {"Título": "Artigo 3", "Resumo": "Resumo do Artigo 3, explora..."},
    {"Título": "Artigo 4", "Resumo": "Resumo do Artigo 4, explora algoritmos eficientes para suffux tree."},
    {"Título": "Artigo 5", "Resumo": "Resumo do Artigo 5, explora algoritmos."},
    {"Título": "Artigo 6", "Resumo": "Resumo do Artigo 6. Ele fala sobre algoritmos."},
    {"Título": "Artigo 7", "Resumo": "Resumo do Artigo 7, que explora o design de algoritmos eficientes."},
    {"Título": "Artigo 8", "Resumo": "Resumo do Artigo 8, explora..."},
    {"Título": "Artigo 9", "Resumo": "Resumo do Artigo 9, explora algoritmos eficientes para suffux tree."},
    # ... Outros artigos ...
]

# Palavras-chave para comparação
palavras_chave = ["algoritmo", "design", "eficiente"]

# Inicialização de um dicionário para armazenar o número de correspondências para cada entrada do dataset
correspondencias = {}

tempo_inicial = time.time() # em segundos

# Algoritmo de String Matching
for i, entrada in enumerate(dataset):               # Percorre os registros do dataset
    correspondencias[i] = 0
    for palavra in palavras_chave:                  # Percorre a lista de palavras-chave
        titulo = entrada["Título"].lower()          # Converte os caracteres maiúsculos para minúsculos
        resumo = entrada["Resumo"].lower()
        if palavra in titulo or palavra in resumo:  # Verifica se palavra-chave consta no titulo ou no resumo
            correspondencias[i] += 1                # Incrementa o número de correspondências

tempo_final = time.time() # em segundos

# Classificação e ordenação com base no número de correspondências
resultado_ordenado = sorted(correspondencias, key=lambda x: correspondencias[x], reverse=True)

# Exibição dos resultados ordenados
for i in resultado_ordenado:
    print(f"Classificação: {correspondencias[i]} - Título: {dataset[i]['Título']}, Resumo: {dataset[i]['Resumo']}")

#Print do tempo que demorou para rodar a parte específica do código
print(f"Duração: {tempo_final - tempo_inicial} segundos")