import json
import numpy as np
import matplotlib.pyplot as plt

with open('dados.json', 'r') as file:
    dados = json.load(file)

pwm = dados['pwm']
tensao = dados['tensao']
luminosidade = dados['luminosidade']

degree = 5

# Ajuste polinomial para tensao vs luminosidade
coef_tensao_luminosidade = np.polyfit(tensao, luminosidade, degree)
poly_tensao_luminosidade = np.poly1d(coef_tensao_luminosidade)
luminosidade_fit = poly_tensao_luminosidade(tensao)

# Ajuste polinomial para pwm vs tensao
coef_pwm_tensao = np.polyfit(pwm, tensao, degree)
poly_pwm_tensao = np.poly1d(coef_pwm_tensao)
tensao_fit = poly_pwm_tensao(pwm)

# Exibir as expressões polinomiais no terminal
print("Expressão polinomial para Tensão vs Luminosidade:")
print(poly_tensao_luminosidade)
print("\nExpressão polinomial para PWM vs Tensão:")
print(poly_pwm_tensao)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

ax1.plot(tensao, luminosidade, marker='o', linestyle='-', color='blue', label='Dados')
ax1.plot(tensao, luminosidade_fit, linestyle='--', color='green', label='Ajuste Polinomial')
ax1.set_title('Variação de Tensão vs. Luminosidade')
ax1.set_xlabel('Tensão (V)')
ax1.set_ylabel('Luminosidade (lux)')
ax1.grid(True)
ax1.legend()

ax2.plot(pwm, tensao, marker='o', linestyle='-', color='red', label='Dados')
ax2.plot(pwm, tensao_fit, linestyle='--', color='green', label='Ajuste Polinomial')
ax2.set_title('Variação do PWM vs. Tensão')
ax2.set_xlabel('PWM (%)')
ax2.set_ylabel('Tensão (V)')
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.savefig('imagens/tensao_vs_luminosidade_modelo_regressao.png')
plt.show()
