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
df = pd.read_csv("data/imdb_top_1000.csv")

print("Pré-visualização dos dados:")
print(df.head())

# =====================================
# Tratamento de valores nulos
# =====================================
df = df.replace({np.nan: None})

# =====================================
# Funções de limpeza de dados
# =====================================
def limpar_int(valor):
    if valor is None:
        return None
    try:
        return int(str(valor).replace(",", ""))
    except:
        return None

def limpar_float(valor):
    if valor is None:
        return None
    try:
        return float(valor)
    except:
        return None

# =====================================
# Inserção dos dados no banco
# =====================================
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT IGNORE INTO imdb (
            poster_link,
            series_title,
            released_year,
            certificate,
            runtime,
            genre,
            imdb_rating,
            overview,
            meta_score,
            director,
            star1,
            star2,
            star3,
            star4,
            no_of_votes,
            gross
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            row["Poster_Link"],
            row["Series_Title"],
            limpar_int(row["Released_Year"]),
            row["Certificate"],
            row["Runtime"],
            row["Genre"],
            limpar_float(row["IMDB_Rating"]),
            row["Overview"],
            limpar_int(row["Meta_score"]),
            row["Director"],
            row["Star1"],
            row["Star2"],
            row["Star3"],
            row["Star4"],
            limpar_int(row["No_of_Votes"]),
            limpar_int(row["Gross"]),
        )
    )

# =====================================
# Finalização
# =====================================
conn.commit()
cursor.close()
conn.close()

print("Importação dos dados do IMDB concluída com sucesso.")
