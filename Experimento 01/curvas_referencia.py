import json
import matplotlib.pyplot as plt

# Carregar dados do arquivo JSON
with open('dados.json', 'r') as file:
    dados = json.load(file)

angulos = dados['angulos']
tensao_x = dados['tensao_x']
tensao_y = dados['tensao_y']

# Criar subplots lado a lado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# Gráfico para o eixo X
ax1.plot(angulos, tensao_x, marker='o', linestyle='-', color='blue')
ax1.set_title('Ângulo de Inclinação vs. Tensão de Saída (Eixo X)')
ax1.set_xlabel('Ângulo (graus)')
ax1.set_ylabel('Tensão (V)')
ax1.grid(True)

# Gráfico para o eixo Y
ax2.plot(angulos, tensao_y, marker='o', linestyle='-', color='red')
ax2.set_title('Ângulo de Inclinação vs. Tensão de Saída (Eixo Y)')
ax2.set_xlabel('Ângulo (graus)')
ax2.set_ylabel('Tensão (V)')
ax2.grid(True)

# Ajustar layout e salvar a figura
plt.tight_layout()
plt.savefig('imagens/angulo_vs_tensao_subplots.png')  # Salva o gráfico como uma imagem
plt.show()