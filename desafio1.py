# desafio1.py
def ler_entrada():
    with open("entrada.txt", "r") as f:
        linhas = f.readlines()
    
    cidades = []
    for linha in linhas:
        if "--" in linha:
            break
        cidade, cep_inicial, cep_final = linha.strip().split(",")
        cidades.append((cidade, int(cep_inicial), int(cep_final)))
    
    cep_pesquisa = int(linhas[-1].strip())
    
    for cidade, cep_inicial, cep_final in cidades:
        if cep_inicial <= cep_pesquisa <= cep_final:
            return cidade
    return "CEP não encontrado"

if __name__ == "__main__":
    cidade = ler_entrada()
    print(f"O CEP pertence à cidade: {cidade}")
