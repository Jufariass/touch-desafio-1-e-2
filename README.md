# Desafio 1 e 2 - Conversão entre CEPs e Cidades

Este repositório contém a solução para dois desafios propostos:

---

## ✅ Desafio 1: CEP → Cidade

Dado um arquivo `entrada.txt` contendo uma lista de CEPs (um por linha), o script `desafio1.py` busca a cidade correspondente a cada CEP e imprime o resultado no terminal.

Foram utilizadas bibliotecas nativas para leitura do arquivo e tratamento de dados, além de chamadas à API pública do ViaCEP para buscar as informações.

### 📂 Exemplo de entrada (`entrada.txt`):
01001-000 30140-001


### 🖨️ Exemplo de saída:
São Paulo 

Belo Horizonte


---

## ✅ Desafio 2: Cidade → CEP

Dado um arquivo `entrada2.txt` contendo nomes de cidades (um por linha), o script `desafio2.py` busca os CEPs relacionados àquela cidade e imprime os resultados.

### 📂 Exemplo de entrada (`entrada2.txt`):

São Paulo 

Porto Alegre


### 🖨️ Exemplo de saída (resumido):


CEP: 01000-000 - São Paulo/SP 

CEP: 01001-000 - São Paulo/SP 

CEP: 90000-000 - Porto Alegre/RS 

CEP: 90010-001 - Porto Alegre/RS 


---

## 📝 Observações

- Foram tratadas exceções para CEPs ou cidades inválidas.
- O foco foi garantir clareza, funcionalidade e simplicidade.

- ## 🧰 Tecnologias utilizadas

- **Python 3.x**  
- **Biblioteca `requests`**  
- **API pública [ViaCEP](https://viacep.com.br)**

---

