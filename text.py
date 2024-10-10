import matplotlib.pyplot as plt

# Dados simples para o gráfico
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Criar o gráfico
plt.plot(x, y)

# Adicionar título e rótulos aos eixos
plt.title('Gráfico Simples de Linha')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Mostrar o gráfico
plt.show()
