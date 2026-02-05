-- =====================================
-- Injeção de Dados - Steam Games
-- =====================================
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/steam.csv'
INTO TABLE steam_games
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
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
);

-- =====================================
-- Injeção de Dados - Musics
-- =====================================
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/musics.csv'
IGNORE
INTO TABLE musics
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    @idx,
    track_id,
    artists,
    album_name,
    track_name,
    popularity,
    duration_ms,
    @explicit,
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
)
SET explicit = CASE
    WHEN @explicit = 'True' THEN 1
    ELSE 0
END;

-- =====================================
-- Injeção de Dados - IMDB
-- =====================================
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/imdb_top_1000.csv'
INTO TABLE imdb
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
    @poster_link,
    @series_title,
    @released_year,
    @certificate,
    @runtime,
    @genre,
    @imdb_rating,
    @overview,
    @meta_score,
    @director,
    @star1,
    @star2,
    @star3,
    @star4,
    @no_of_votes,
    @gross
)
SET
poster_link = NULLIF(@poster_link, ''),
series_title = NULLIF(@series_title, ''),
released_year = CASE
    WHEN @released_year REGEXP '^[0-9]{4}$' THEN @released_year
    ELSE NULL
END,
certificate = NULLIF(@certificate, ''),
runtime = NULLIF(@runtime, ''),
genre = NULLIF(@genre, ''),
imdb_rating = NULLIF(@imdb_rating, ''),
overview = NULLIF(@overview, ''),
meta_score = NULLIF(@meta_score, ''),
director = NULLIF(@director, ''),
star1 = NULLIF(@star1, ''),
star2 = NULLIF(@star2, ''),
star3 = NULLIF(@star3, ''),
star4 = NULLIF(@star4, ''),
no_of_votes = NULLIF(@no_of_votes, ''),
gross = CASE
    WHEN @gross IS NULL OR TRIM(@gross) = '' THEN NULL
    WHEN @gross REGEXP '^[0-9,]+$'
        THEN CAST(REPLACE(@gross, ',', '') AS UNSIGNED)
    ELSE NULL
END;

-- =====================================
-- Injeção de Dados - Sazonalidade
-- =====================================
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/trending - sazonalidade.csv'
INTO TABLE sazonalidade
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
    @idx,
    tmdb_id,
    @original_title,
    original_language,
    @release_date,
    popularity,
    vote_average,
    vote_count,
    media_type,
    @adult
)
SET
original_title = NULLIF(@original_title, ''),
release_date = NULLIF(@release_date, ''),
adult = CASE
    WHEN @adult = 'True' THEN 1
    ELSE 0
END;
