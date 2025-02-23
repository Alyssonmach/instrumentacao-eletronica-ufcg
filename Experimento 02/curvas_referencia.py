import json
import matplotlib.pyplot as plt

with open('dados.json', 'r') as file:
    dados = json.load(file)

pwm = dados['pwm']
tensao = dados['tensao']
luminosidade = dados['luminosidade']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

ax1.plot(tensao, luminosidade, marker='o', linestyle='-', color='blue')
ax1.set_title('Variação de Tensão vs. Luminosidade')
ax1.set_xlabel('Tensão (V)')
ax1.set_ylabel('Luminosidade (lux)')
ax1.grid(True)

ax2.plot(pwm, tensao, marker='o', linestyle='-', color='red')
ax2.set_title('Variação do PWM vs. Tensão')
ax2.set_xlabel('PWM (%)')
ax2.set_ylabel('Tensão (V)')
ax2.grid(True)

plt.tight_layout()
plt.savefig('imagens/tensao_vs_luminosidade.png')
plt.show()
