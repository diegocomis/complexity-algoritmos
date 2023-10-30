#pip install pyahocorasick
import ahocorasick

def find_keywords(text, keywords):
    # implementar um for para percorrer o dataset
    A = ahocorasick.Automaton()
    for keyword in keywords:
        A.add_word(keyword, keyword)
    A.make_automaton()

    results = set()
    for end_index, keyword in A.iter(text):
        start_index = end_index - len(keyword) + 1
        results.add((start_index, end_index, keyword))

    return results

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
    # ... Outros artigos ...
]
text = "This is a sample text where we search for keywords like sample, text, and more."
keywords = ["sample", "text", "more"]

matches = find_keywords(text, keywords)
for start, end, keyword in matches:
    print(f"Found '{keyword}' at positions {start}-{end}")