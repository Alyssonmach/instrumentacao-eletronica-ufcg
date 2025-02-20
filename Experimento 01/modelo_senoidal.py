import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

with open('dados.json', 'r') as file:
    dados = json.load(file)

angulos = np.array(dados['angulos'])
tensao_x = np.array(dados['tensao_x'])
tensao_y = np.array(dados['tensao_y'])

def modelo_senoidal(x, A, omega, phi, offset):
    return A * np.sin(omega * np.radians(x) + phi) + offset

parametros_x, _ = curve_fit(modelo_senoidal, angulos, tensao_x, p0=[1.0, 0.01, 0.0, 0.0])
A_x, omega_x, phi_x, offset_x = parametros_x

parametros_y, _ = curve_fit(modelo_senoidal, angulos, tensao_y, p0=[1.0, 0.01, 0.0, 0.0])
A_y, omega_y, phi_y, offset_y = parametros_y

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

ax1.scatter(angulos, tensao_x, color='blue', label='Dados Reais')
ax1.plot(angulos, modelo_senoidal(angulos, *parametros_x), color='red', label='Ajuste Senoidal')
ax1.set_title('Ajuste Senoidal: Ângulo vs. Tensão (Eixo X)')
ax1.set_xlabel('Ângulo (graus)')
ax1.set_ylabel('Tensão (V)')
ax1.legend()
ax1.grid(True)

ax2.scatter(angulos, tensao_y, color='blue', label='Dados Reais')
ax2.plot(angulos, modelo_senoidal(angulos, *parametros_y), color='red', label='Ajuste Senoidal')
ax2.set_title('Ajuste Senoidal: Ângulo vs. Tensão (Eixo Y)')
ax2.set_xlabel('Ângulo (graus)')
ax2.set_ylabel('Tensão (V)')
ax2.legend()
ax2.grid(True)

plt.savefig('imagens/ajuste_senoidal_subplots.png')
plt.show()

print("Parâmetros ajustados para o Eixo X:")
print(f"Amplitude (A_x): {A_x:.4f}")
print(f"Frequência Angular (omega_x): {omega_x:.4f}")
print(f"Fase (phi_x): {phi_x:.4f}")
print(f"Offset (offset_x): {offset_x:.4f}")

print("\nParâmetros ajustados para o Eixo Y:")
print(f"Amplitude (A_y): {A_y:.4f}")
print(f"Frequência Angular (omega_y): {omega_y:.4f}")
print(f"Fase (phi_y): {phi_y:.4f}")
print(f"Offset (offset_y): {offset_y:.4f}")
