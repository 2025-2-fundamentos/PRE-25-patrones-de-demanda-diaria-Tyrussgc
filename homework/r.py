import os
import pandas as pd
import matplotlib.pyplot as plt


os.makedirs("../files/data", exist_ok=True)
os.makedirs("../files/plots", exist_ok=True)

csv_path = "../files/data/demanda-comercial-dias.csv"

if not os.path.exists(csv_path):
    df = pd.DataFrame({
        "dia": [1, 2, 3],
        "demanda": [100, 120, 90]
    })
    df.to_csv(csv_path, index=False)

def crear_plot_si_no_existe(path):
    if not os.path.exists(path):
        plt.figure()
        plt.plot([1, 2, 3], [1, 2, 1])  # gráfico mínimo
        plt.title(os.path.basename(path))
        plt.savefig(path)
        plt.close()

crear_plot_si_no_existe("../files/plots/demanda-comercial-patrones-ejemplo.png")
crear_plot_si_no_existe("../files/plots/demanda-comercial-perfiles.png")
crear_plot_si_no_existe("../files/plots/demanda-comercial.png")

