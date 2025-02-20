import json
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

with open('dados.json', 'r') as file:
    dados = json.load(file)

angulos = np.array(dados['angulos']).reshape(-1, 1)
tensao_x = np.array(dados['tensao_x'])
tensao_y = np.array(dados['tensao_y'])

def regressao_polinomial(angulos, tensao, eixo, ax):
    poly = PolynomialFeatures(degree=3)
    angulos_poly = poly.fit_transform(angulos)

    modelo = LinearRegression()
    modelo.fit(angulos_poly, tensao)

    tensao_pred = modelo.predict(angulos_poly)

    mse = mean_squared_error(tensao, tensao_pred)
    r2 = r2_score(tensao, tensao_pred)

    print(f'Eixo {eixo}:')
    print(f'MSE: {mse:.4f}')
    print(f'R2: {r2:.4f}')

    ax.scatter(angulos, tensao, color='blue', label='Dados Reais')
    ax.plot(angulos, tensao_pred, color='red', linewidth=2, label='Regressão Polinomial')
    ax.set_title(f'Regressão Polinomial: Ângulo vs. Tensão (Eixo {eixo})')
    ax.set_xlabel('Ângulo (graus)')
    ax.set_ylabel('Tensão (V)')
    ax.legend()
    ax.grid(True)

    print(f'Equação do modelo (Eixo {eixo}):')
    print(f'y = {modelo.intercept_:.4f}', end='')
    for i, coef in enumerate(modelo.coef_[1:]):
        print(f' + {coef:.4f} * x^{i+1}', end='')
    print('\n')

fig, axs = plt.subplots(1, 2, figsize=(15, 5))

regressao_polinomial(angulos, tensao_x, 'X', axs[0])
regressao_polinomial(angulos, tensao_y, 'Y', axs[1])

plt.tight_layout()
plt.savefig('imagens/regressao_polinomial_subplots.png')
plt.show()
