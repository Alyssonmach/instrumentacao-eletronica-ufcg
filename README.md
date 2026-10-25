# Instrumentação Eletrônica — UFCG

Repositório com os dados, scripts de análise, gráficos e relatórios dos experimentos realizados na disciplina de Instrumentação Eletrônica da Universidade Federal de Campina Grande (UFCG).

## Experimentos

| Diretório | Conteúdo |
| --- | --- |
| [Experimento 01](Experimento%2001/) | Inclinação e tensão de saída nos eixos X e Y; curvas de referência, regressão polinomial e ajuste senoidal. |
| [Experimento 02](Experimento%2002/) | Medição de luminosidade em função da tensão e do PWM; curvas de referência e regressão polinomial. |
| [Experimento 03](Experimento%2003/) | Resposta térmica de um módulo Peltier durante aquecimento e resfriamento. |
| [Experimento 04](Experimento%2004/) | Relação entre força e deformação medida com strain gauge, com aproximação linear. |
| [Experimento 05](Experimento%2005/) | Resposta em frequência e defasagem, incluindo gráficos com escala logarítmica. |

Cada diretório reúne os arquivos do experimento: dados de entrada, scripts, gráficos gerados e, quando disponível, o relatório em PDF.

## Requisitos

- Python 3
- Bibliotecas listadas em [`requirements.txt`](requirements.txt)

Instale as dependências na raiz do repositório:

```bash
python -m pip install -r requirements.txt
```

## Como executar

Os scripts usam caminhos relativos ao diretório do experimento. Entre nele antes de executar o arquivo desejado. Por exemplo:

```bash
cd "Experimento 01"
python curvas_referencia.py
```

Scripts disponíveis:

- **Experimento 01:** `curvas_referencia.py`, `modelo_regressao.py`, `modelo_senoidal.py`
- **Experimento 02:** `curvas_referencia.py`, `modelo_regressao.py`
- **Experimento 03:** `modulo_peltier.py`
- **Experimento 04:** `curva_strain_gauge.py`
- **Experimento 05:** `curvas.py`

Os scripts que salvam figuras gravam os arquivos no diretório `imagens/` de cada experimento. As janelas dos gráficos também podem ser fechadas para encerrar a execução.
