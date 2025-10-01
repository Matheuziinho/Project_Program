from typing import Any
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# === 1. Ler dados ===
df = pd.read_excel("/home/matheus/Documentos/Estatcamp/Documentos/Piloto.xlsx")

# Colunas de tempo (ajuste se forem diferentes no seu arquivo)
tempo_cols = ["00:00","02:00","04:00","06:00","08:00","10:00","12:00","20:00","24:00","36:00"]
tempos = np.array([0,2,4,6,8,10,12,20,24,36])  # horas

# === 2. Definir controles e tratados ===
controles = ["C1","C2","B1","B2"]
df_controles = df[df["Sitio"].isin(controles)]
df_tratados = df[~df["Sitio"].isin(controles)]

# === 3. Média dos controles em cada tempo ===
controle_medio = df_controles[["Baseline"]+tempo_cols].mean()

# === 4. Funções ===
def corrige_linha(row: Any) -> np.ndarray:
    """Aplica correção da fórmula para uma linha (tratado)."""
    baseline = row["Baseline"]
    valores = row[tempo_cols].astype(float).values
    controle_vals = controle_medio[tempo_cols].values
    corrigido = valores - baseline - controle_vals
    return corrigido

def trapezio(y: np.ndarray, t: np.ndarray) -> float:
    return np.trapz(y, t)

def hill_equation(dose: float, E_min: float, E_max: float, ED50: float, h: float) -> float:
    return E_min + (E_max - E_min) / (1 + (ED50/dose)**h)

# === 5. Calcular AUEC corrigida por linha ===
corrigidos = []
resultados = []

for idx, row in df_tratados.iterrows():
    corrigido = corrige_linha(row)
    auc = trapezio(corrigido, tempos[1:])  # ignora baseline
    corrigidos.append([row["PP"], row["Braco"], row["Tempo_de_exposicao"], row["Sitio"]] + corrigido.tolist())
    resultados.append([row["PP"], row["Braco"], row["Tempo_de_exposicao"], row["Sitio"], auc])

# Tabelas organizadas
corrigidos_df = pd.DataFrame(corrigidos, columns=["PP","Braco","Tempo_exposicao","Sitio"]+tempo_cols)
auec_df = pd.DataFrame(resultados, columns=["PP","Braco","Tempo_exposicao","Sitio","AUEC"])

# === 6. Média da resposta por tempo de exposição ===
mean_res = auec_df.groupby("Tempo_exposicao")["AUEC"].mean().reset_index()

# === 7. Ajuste do modelo logístico ===
xdata = mean_res["Tempo_exposicao"].values
ydata = mean_res["AUEC"].values

p0 = [min(ydata), max(ydata), np.median(xdata), 1.0]  # chute inicial
popt, pcov = curve_fit(hill_equation, xdata, ydata, p0=p0, maxfev=5000)
E_min, E_max, ED50, h = popt

print(f"\n✅ ED50 estimado = {ED50:.3f} horas")

# === 8. Gráfico ===
xfit = np.linspace(min(xdata), max(xdata), 200)
yfit = hill_equation(xfit, *popt)

plt.scatter(xdata, ydata, label="Dados médios", color="blue")
plt.plot(xfit, yfit, 'r-', label=f"Curva ajustada (ED50={ED50:.2f}h)")
plt.xlabel("Tempo de exposição (h)")
plt.ylabel("AUEC corrigida")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# === 9. Exportar resultados ===
with pd.ExcelWriter("Resultados_ED50.xlsx") as writer:
    df.to_excel(writer, sheet_name="Dados_brutos", index=False)
    corrigidos_df.to_excel(writer, sheet_name="Valores_corrigidos", index=False)
    auec_df.to_excel(writer, sheet_name="AUEC_por_sitio", index=False)
    mean_res.to_excel(writer, sheet_name="AUEC_media_por_dose", index=False)
