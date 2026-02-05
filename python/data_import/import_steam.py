import pandas as pd
import mysql.connector
import numpy as np

# =====================================
# Conexão com o banco de dados MySQL
# =====================================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sua_Senha",
    database="projeto_big_data"
)

cursor = conn.cursor()

# =====================================
# Leitura do arquivo CSV
# =====================================
df = pd.read_csv("data/steam.csv")

# =====================================
# Tratamento de valores nulos
# =====================================
df = df.replace({np.nan: None})

# =====================================
# Inserção dos dados no banco
# =====================================
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT IGNORE INTO steam_games (
            appid,
            nome,
            release_date,
            english,
            developer,
            publisher,
            platforms,
            required_age,
            categories,
            genres,
            steamspy_tags,
            achievements,
            positive_ratings,
            negative_ratings,
            average_playtime,
            median_playtime,
            owners,
            price
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            row["appid"],
            row["name"],
            row["release_date"],
            row["english"],
            row["developer"],
            row["publisher"],
            row["platforms"],
            row["required_age"],
            row["categories"],
            row["genres"],
            row["steamspy_tags"],
            row["achievements"],
            row["positive_ratings"],
            row["negative_ratings"],
            row["average_playtime"],
            row["median_playtime"],
            row["owners"],
            row["price"],
        )
    )

# =====================================
# Finalização
# =====================================
conn.commit()
cursor.close()
conn.close()

print("Importação dos dados da Steam concluída com sucesso.")
