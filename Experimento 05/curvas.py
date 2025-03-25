import matplotlib.pyplot as plt
import numpy as np

# Carregar os dados dos arquivos de frequência e resposta em dB
frequencia = "dados/frequencia.txt"
resposta_db = "dados/resposta.txt"
defasagem = "dados/defasagem.txt"

dado_frequencia = np.loadtxt(frequencia)
dados_resposta_db = np.loadtxt(resposta_db)
dados_defasagem = np.loadtxt(defasagem)

# Plotagem do gráfico da resposta em dB
plt.figure(figsize=(10, 5))
plt.plot(dado_frequencia, dados_resposta_db, label='Resposta em dB')
plt.xscale('log')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Resposta (dB)')
plt.title('Curva de Resposta em Frequência')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('imagens/resposta_db_log.png')
plt.show()

# Plotagem do gráfico da defasagem
plt.figure(figsize=(10, 5))
plt.plot(dado_frequencia, dados_defasagem, label='Defasagem')
plt.xscale('log')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Defasagem (°)')
plt.title('Curva de Defasagem em Frequência')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('imagens/resposta_db_defasagem.png')
plt.show()