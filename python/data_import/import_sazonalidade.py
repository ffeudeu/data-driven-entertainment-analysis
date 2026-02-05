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
df = pd.read_csv("data/trending - sazonalidade.csv")

print("Pré-visualização dos dados:")
print(df.head())

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
        INSERT IGNORE INTO sazonalidade (
            tmdb_id,
            original_title,
            original_language,
            release_date,
            popularity,
            vote_average,
            vote_count,
            media_type,
            adult
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            row["id"],
            row["original_title"],
            row["original_language"],
            row["release_date"],
            row["popularity"],
            row["vote_average"],
            row["vote_count"],
            row["media_type"],
            1 if row["adult"] is True else 0
        )
    )

# =====================================
# Finalização
# =====================================
conn.commit()
cursor.close()
conn.close()

print("Importação dos dados de sazonalidade concluída com sucesso.")
