import matplotlib.pyplot as plt
import numpy as np

# Carregar os dados dos arquivos de aquecimento e resfriamento
arquivo_aquecimento = "Dados/Aquecimento.txt"
arquivo_resfriamento = "Dados/Resfriamento.txt"

# Carregar os valores de temperatura registrados ao longo do tempo
dados_aquecimento = np.loadtxt(arquivo_aquecimento)
dados_resfriamento = np.loadtxt(arquivo_resfriamento)

# Definição dos valores experimentais extraídos do relatório
TS1 = 23.2031  # Temperatura inicial
TS2 = 24.7411  # Temperatura final de estabilização

TMFQ = 32.9563  # Temperatura máxima face quente
TMFF = 18.168   # Temperatura mínima face fria

TFQD = 32.6196  # Temperatura final de resfriamento face quente
TFFD = 18.9024  # Temperatura final de resfriamento face fria

# Tempos de ativação e desativação do Peltier
tempo_liga = 15.1   # s
tempo_desliga = 90.8 # s

# Cálculo das temperaturas correspondentes a 63% da variação
T63FQA = 0.63 * (TMFQ - TS1) + TS1
T63FFA = 0.63 * (TMFF - TS1) + TS1
T63FQD = TFQD - 0.63 * (TFQD - TS2)
T63FFD = TFFD + 0.63 * (TS2 - TFFD)

print(f"Temperatura correspondente a 63% da variação face quente (acionamento): {T63FQA:.5f} °C")
print(f"Temperatura correspondente a 63% da variação face fria (acionamento): {T63FFA:.5f} °C")
print(f"Temperatura correspondente a 63% da variação face quente (resfriamento): {T63FQD:.5f} °C")
print(f"Temperatura correspondente a 63% da variação face fria (resfriamento): {T63FFD:.5f} °C")
print('---\n')

# Criar vetor de tempo com base na taxa de amostragem (100 ms = 0.1 s)
tempo_aquecimento = np.arange(0, len(dados_aquecimento) * 0.1, 0.1)
tempo_resfriamento = np.arange(0, len(dados_resfriamento) * 0.1, 0.1)

# Encontrar os tempos correspondentes às temperaturas de 63%
tempo_T63FQA = tempo_aquecimento[np.where(np.abs(dados_aquecimento - T63FQA) < 0.1)[0][0]]
tempo_T63FFA = tempo_resfriamento[np.where(np.abs(dados_resfriamento - T63FFA) < 0.5)[0][0]]
tempo_T63FQD = tempo_aquecimento[np.where(np.abs(dados_aquecimento - T63FQD) < 0.1)[0][-1]]
tempo_T63FFD = tempo_resfriamento[np.where(np.abs(dados_resfriamento - T63FFD) < 0.1)[0][-1]]

print(f"Tempo correspondente a T63FQA: {tempo_T63FQA:.2f} s")
print(f"Tempo correspondente a T63FFA: {tempo_T63FFA:.2f} s")
print(f"Tempo correspondente a T63FQD: {tempo_T63FQD:.2f} s")
print(f"Tempo correspondente a T63FFD: {tempo_T63FFD:.2f} s")
print('---\n')

# Calcular os tempos de resposta
tempo_T63FQA_resposta = tempo_T63FQA - tempo_liga
tempo_T63FFA_resposta = tempo_T63FFA - tempo_liga
tempo_T63FQD_resposta = tempo_T63FQD - tempo_desliga
tempo_T63FFD_resposta = tempo_T63FFD - tempo_desliga

print(f"Tempo de resposta face quente (acionamento): {tempo_T63FQA_resposta:.2f} s")
print(f"Tempo de resposta face fria (acionamento): {tempo_T63FFA_resposta:.2f} s")
print(f"Tempo de resposta face quente (resfriamento): {tempo_T63FQD_resposta:.2f} s")
print(f"Tempo de resposta face fria (resfriamento): {tempo_T63FFD_resposta:.2f} s")
print('---\n')

# Plotar os dados de aquecimento
plt.figure(figsize=(10, 5))
plt.plot(tempo_aquecimento, dados_aquecimento, label='Aquecimento')
plt.plot(tempo_resfriamento, dados_resfriamento, label='Resfriamento')
plt.scatter(tempo_T63FQA, T63FQA, color='r', label=f'T63FQA: {tempo_T63FQA:.2f} s', zorder=5)
plt.scatter(tempo_T63FFA, T63FFA, color='g', label=f'T63FFA: {tempo_T63FFA:.2f} s', zorder=5)
plt.scatter(tempo_T63FQD, T63FQD, color='b', label=f'T63FQD: {tempo_T63FQD:.2f} s', zorder=5)
plt.scatter(tempo_T63FFD, T63FFD, color='y', label=f'T63FFD: {tempo_T63FFD: 2f} s', zorder=5)
plt.xlabel('Tempo (s)')
plt.ylabel('Temperatura (°C)')
plt.title('Curvas de Aquecimento e Resfriamento')
plt.legend()
plt.grid(True)
plt.show()
