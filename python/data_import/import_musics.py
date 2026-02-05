import pandas as pd
import mysql.connector
import numpy as np

# =====================================
# Conexão com o banco de dados MySQL
# =====================================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Isaloffeu94",
    database="projeto_big_data"
)

cursor = conn.cursor()

# =====================================
# Leitura do arquivo CSV
# =====================================
df = pd.read_csv("data/musics.csv")

# Remover coluna desnecessária (index)
if "Unnamed: 0" in df.columns:
    df.drop(columns=["Unnamed: 0"], inplace=True)

# =====================================
# Tratamento de valores nulos
# =====================================
df = df.replace({np.nan: None})

# =====================================
# Conversão de boolean para inteiro
# =====================================
df["explicit"] = df["explicit"].apply(lambda x: 1 if x else 0)

# =====================================
# Inserção dos dados no banco
# =====================================
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT IGNORE INTO musics (
            track_id,
            artists,
            album_name,
            track_name,
            popularity,
            duration_ms,
            explicit,
            danceability,
            energy,
            musical_key,
            loudness,
            modo,
            speechiness,
            acousticness,
            instrumentalness,
            liveness,
            valence,
            tempo,
            time_signature,
            track_genre
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            row["track_id"],
            row["artists"],
            row["album_name"],
            row["track_name"],
            row["popularity"],
            row["duration_ms"],
            row["explicit"],
            row["danceability"],
            row["energy"],
            row["key"],
            row["loudness"],
            row["modo"],
            row["speechiness"],
            row["acousticness"],
            row["instrumentalness"],
            row["liveness"],
            row["valence"],
            row["tempo"],
            row["time_signature"],
            row["track_genre"],
        )
    )

# =====================================
# Finalização
# =====================================
conn.commit()
cursor.close()
conn.close()

print("Importação dos dados de músicas concluída com sucesso.")
