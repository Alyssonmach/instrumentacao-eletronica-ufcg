import matplotlib.pyplot as plt
import numpy as np

# Carregar os dados dos arquivos de força e deformação
forca = "dados/forca.txt"
deformacao = "dados/deformacao.txt"

# Carregar os valores de respectivos registrados ao longo do tempo
dados_forca = np.loadtxt(forca)
dados_deformacao = np.loadtxt(deformacao)

# Ajustar uma linha reta (aproximação linear) aos dados
coeficientes = np.polyfit(dados_forca, dados_deformacao, 1)
linha_ajustada = np.polyval(coeficientes, dados_forca)

# Plotar os força x deformação e a linha ajustada
plt.figure(figsize=(10, 5))
plt.plot(dados_forca, dados_deformacao, label='Força x Deformação')
plt.plot(dados_forca, linha_ajustada, label='Aproximação Linear', linestyle='--')
plt.xlabel('Força (N)')
plt.ylabel('Deformação ($\\frac{\\mu m}{m}$)')
plt.title('Curva Força x Deformação')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('imagens/forca_vs_deformacao.png')
plt.show()

# Imprimir a equação da reta aproximada
print(f"Equação da reta aproximada: y = {coeficientes[0]:.2f}x + {coeficientes[1]:.2f}")
