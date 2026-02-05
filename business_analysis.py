import mysql.connector

# =====================================
# Conexão com o banco de dados MySQL
# =====================================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sua_Senha",
    database="projeto_big_data"
)

cursor = conn.cursor(dictionary=True)

print("\n==============================================")
print(" ANÁLISES ESTRATÉGICAS - PROJETO BIG DATA ")
print("==============================================\n")

# =====================================
# Jogos - Steam
# =====================================
print("1️- Jogo com maior número de jogadores:")

cursor.execute("""
    SELECT nome, owners
    FROM steam_games
    ORDER BY owners DESC
    LIMIT 1
""")
print(cursor.fetchone(), "\n")

print("2️- Gênero de jogo mais popular:")

cursor.execute("""
    SELECT genres, SUM(owners) AS total_owners
    FROM steam_games
    GROUP BY genres
    ORDER BY total_owners DESC
    LIMIT 1
""")
print(cursor.fetchone(), "\n")

# =====================================
# Música
# =====================================
print("3️- Estilo musical mais popular:")

cursor.execute("""
    SELECT track_genre, AVG(popularity) AS media_popularidade
    FROM musics
    GROUP BY track_genre
    ORDER BY media_popularidade DESC
    LIMIT 1
""")
print(cursor.fetchone(), "\n")

print("4️- Artistas com maior alcance:")

cursor.execute("""
    SELECT artists, AVG(popularity) AS media_popularidade
    FROM musics
    GROUP BY artists
    ORDER BY media_popularidade DESC
    LIMIT 5
""")
for row in cursor.fetchall():
    print(row)
print()

# =====================================
# Filmes e Séries
# =====================================
print("5️- Consumo por formato (filme vs série):")

cursor.execute("""
    SELECT media_type, COUNT(*) AS total
    FROM sazonalidade
    GROUP BY media_type
""")
for row in cursor.fetchall():
    print(row)
print()

print("6️- Melhor custo-benefício (nota média):")

cursor.execute("""
    SELECT media_type, AVG(vote_average) AS media_avaliacao
    FROM sazonalidade
    GROUP BY media_type
    ORDER BY media_avaliacao DESC
""")
for row in cursor.fetchall():
    print(row)
print()

print("7️- Retorno médio por gênero:")

cursor.execute("""
    SELECT genre, AVG(gross) AS retorno_medio
    FROM imdb
    WHERE gross IS NOT NULL
    GROUP BY genre
    ORDER BY retorno_medio DESC
    LIMIT 5
""")
for row in cursor.fetchall():
    print(row)
print()

print("8- Relação entre nota IMDB e faturamento:")

cursor.execute("""
    SELECT imdb_rating, gross
    FROM imdb
    WHERE imdb_rating IS NOT NULL AND gross IS NOT NULL
    ORDER BY imdb_rating DESC
    LIMIT 5
""")
for row in cursor.fetchall():
    print(row)
print()

# =====================================
# Sazonalidade
# =====================================
print("9️- Lançamentos por mês:")

cursor.execute("""
    SELECT MONTH(release_date) AS mes, COUNT(*) AS total
    FROM sazonalidade
    WHERE release_date IS NOT NULL
    GROUP BY mes
    ORDER BY total DESC
""")
for row in cursor.fetchall():
    print(row)
print()

print("10- Popularidade média por mês:")

cursor.execute("""
    SELECT MONTH(release_date) AS mes, AVG(popularity) AS popularidade_media
    FROM sazonalidade
    WHERE release_date IS NOT NULL
    GROUP BY mes
    ORDER BY popularidade_media DESC
""")
for row in cursor.fetchall():
    print(row)
print()

# =====================================
# Finalização
# =====================================
cursor.close()
conn.close()

print("==============================================")
print(" Análises concluídas com sucesso! ")
print("==============================================")
