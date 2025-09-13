# [cite_start]Passo A: Importar os módulos necessários com seus aliases [cite: 89, 90, 108]
# 'pandas' é usado para carregar e manipular os dados do CSV.
# 'matplotlib.pyplot' é usado para criar os gráficos.
import pandas as pd
from matplotlib import pyplot as plt

# Passo B: Ler o arquivo CSV e carregar os dados
# [cite_start]A função 'read_csv' do pandas transforma o arquivo em uma tabela (DataFrame)[cite: 95, 202].
# A variável 'df' agora armazena todos os dados das notas.
try:
    df = pd.read_csv('notas_matematica.csv', sep=',')
except FileNotFoundError:
    print("Erro: O arquivo 'notas_matematica.csv' não foi encontrado.")
    print("Certifique-se de que ele está na mesma pasta que o script Python.")
    exit()

# Passo C: Exibir e analisar os dados
# [cite_start]Usamos a função 'print()' para visualizar a tabela no terminal[cite: 176].
print("--- Tabela de Notas Carregada ---")
print(df)
print("-" * 30) # Apenas para separar a saída

# Como uma análise simples, vamos calcular a média das notas.
# 'df['Nota']' seleciona a coluna de notas e '.mean()' calcula a média.
media_notas = df['Nota'].mean()
print(f"A média geral da turma é: {media_notas:.2f}\n")


# Passo D: Criar e exibir o gráfico
# [cite_start]Aqui usamos as funções do matplotlib para visualizar os dados[cite: 98, 203].
print("Gerando o gráfico de notas...")

# Cria um gráfico de barras com os alunos no eixo X e as notas no eixo Y.
plt.bar(df['Aluno'], df['Nota'])

# Adiciona um título e rótulos para os eixos, para que o gráfico seja fácil de entender.
plt.title('Desempenho dos Alunos em Matemática')
plt.xlabel('Aluno')
plt.ylabel('Nota Final')

# Define os limites do eixo Y para que a nota máxima seja 10.
plt.ylim(0, 10)

# [cite_start]A função 'show()' exibe a janela do gráfico[cite: 98, 204].
plt.show()

print("Gráfico exibido com sucesso!")