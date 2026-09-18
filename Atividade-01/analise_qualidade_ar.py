"""Mini-relatório: análise de dados reais de qualidade do ar.

Dataset original: UCI Machine Learning Repository, Air Quality.
"""

import pandas as pd
import matplotlib.pyplot as plt


# No Google Colab, envie o arquivo qualidade_ar_real_uci.csv para a sessão.
ARQUIVO = "qualidade_ar_real_uci.csv"

# Carregamento dos dados
df = pd.read_csv(ARQUIVO, parse_dates=["data_hora"])

# Primeiras linhas e informações gerais
print("PRIMEIRAS CINCO LINHAS")
print(df.head())

print("\nINFORMAÇÕES DO DATASET")
df.info()

print("\nESTATÍSTICAS DESCRITIVAS")
print(df.describe(include="all"))

# Gráfico: concentração de monóxido de carbono ao longo do tempo
plt.figure(figsize=(14, 5))
plt.plot(df["data_hora"], df["CO(GT)"], color="#1565C0", linewidth=0.7)
plt.title("Concentração de CO ao longo do tempo")
plt.xlabel("Data")
plt.ylabel("CO (mg/m³)")
plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()

# Análise complementar: correlação entre a medida de referência de CO
# e a resposta do sensor eletrônico voltado para CO.
correlacao = df[["CO(GT)", "PT08.S1(CO)"]].corr().iloc[0, 1]
print(f"\nCorrelação CO(GT) x PT08.S1(CO): {correlacao:.3f}")

# Valores úteis para redigir as observações técnicas
print(f"Período: {df['data_hora'].min()} a {df['data_hora'].max()}")
print(f"Média de CO: {df['CO(GT)'].mean():.3f} mg/m³")
print(f"Máximo de CO: {df['CO(GT)'].max():.1f} mg/m³")
print(f"Dados ausentes em CO: {df['CO(GT)'].isna().mean() * 100:.1f}%")

