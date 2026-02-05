-- ==================================================
-- Análises Estratégicas - Jogos (Steam)
-- ==================================================

-- Jogo mais popular com base em avaliações positivas
SELECT
    nome AS jogo,
    positive_ratings AS avaliacoes_positivas
FROM steam_games
ORDER BY positive_ratings DESC
LIMIT 1;

-- Gêneros com maior engajamento (avaliações positivas)
SELECT
    genres AS genero,
    SUM(positive_ratings) AS total_engajamento
FROM steam_games
GROUP BY genres
ORDER BY total_engajamento DESC;

-- Quantidade de jogos por gênero
SELECT
    genres AS genero,
    COUNT(*) AS total_jogos
FROM steam_games
GROUP BY genres
ORDER BY total_jogos DESC;

-- Tempo médio de jogo por gênero
SELECT
    genres AS genero,
    AVG(average_playtime) AS tempo_medio_jogado
FROM steam_games
GROUP BY genres
ORDER BY tempo_medio_jogado DESC;

-- ==================================================
-- Análises Financeiras - Filmes e Séries (IMDB)
-- ==================================================

-- Faturamento médio por gênero
SELECT
    genre,
    AVG(gross) AS faturamento_medio
FROM imdb
WHERE gross IS NOT NULL
GROUP BY genre;

-- ==================================================
-- Análises Musicais - Popularidade
-- ==================================================

-- Gêneros musicais mais populares
SELECT
    track_genre,
    AVG(popularity) AS popularidade_media
FROM musics
GROUP BY track_genre
ORDER BY popularidade_media DESC
LIMIT 10;

-- ==================================================
-- Comparativo Filme vs Série e Sazonalidade
-- ==================================================

-- Comparação entre filmes e séries
SELECT
    media_type,
    AVG(vote_average) AS nota_media,
    AVG(vote_count) AS votos_medios
FROM sazonalidade
GROUP BY media_type;

-- Volume de lançamentos por mês
SELECT
    MONTH(release_date) AS mes,
    COUNT(*) AS total_lancamentos
FROM sazonalidade
WHERE release_date IS NOT NULL
GROUP BY mes
ORDER BY mes;
