# 1. Defina os dados para as variáveis 'year' e 'pop'
year = [1950, 1970, 1990, 2010, 2030]
pop = [2.519, 3.692, 5.263, 6.972, 8.525] # População em bilhões (exemplo)

# 2. Print the last item from year and pop (como pedia o comentário)
print("Último ano da lista:", year[-1])
print("Último dado de população:", pop[-1])

# 3. Importe a biblioteca de gráficos
import matplotlib.pyplot as plt

# 4. Crie o gráfico de linha: ano no eixo x, pop no eixo y
plt.plot(year, pop)

# 5. Adicione títulos para clareza (Opcional, mas recomendado)
plt.title("Crescimento da População Mundial")
plt.xlabel("Ano")
plt.ylabel("População (em Bilhões)")

# 6. Exiba o gráfico
plt.show()
