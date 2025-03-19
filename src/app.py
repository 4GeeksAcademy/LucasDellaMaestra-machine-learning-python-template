
# your code here
import pandas as pd
import os

# URL del CSV
url = "https://raw.githubusercontent.com/4GeeksAcademy/data-preprocessing-project-tutorial/main/AB_NYC_2019.csv"

# Leer CSV desde la URL
df = pd.read_csv(url)


# Guardar archivo CSV crudo en 'data/raw'
df.to_csv('data/raw/AB_NYC_2019.csv', index=False)

print("✅ Datos crudos guardados en 'data/raw/AB_NYC_2019.csv'")

# Obtener dimensiones
df.shape