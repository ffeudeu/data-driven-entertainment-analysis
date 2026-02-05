CREATE DATABASE projeto_big_data;
USE projeto_big_data;

-- ================================
-- Tabela: steam_games
-- ================================
CREATE TABLE steam_games (
    appid INT PRIMARY KEY,
    nome VARCHAR(255),
    release_date DATE,
    english BOOLEAN,
    developer VARCHAR(255),
    publisher VARCHAR(255),
    platforms VARCHAR(100),
    required_age INT,
    categories TEXT,
    genres VARCHAR(255),
    steamspy_tags VARCHAR(255),
    achievements INT,
    positive_ratings INT,
    negative_ratings INT,
    average_playtime INT,
    median_playtime INT,
    owners VARCHAR(50),
    price DECIMAL(6,2)
);

-- ================================
-- Tabela: musics
-- ================================
CREATE TABLE musics (
    track_id VARCHAR(50),
    artists VARCHAR(500),
    album_name VARCHAR(500),
    track_name VARCHAR(500),
    popularity INT,
    duration_ms INT,
    explicit BOOLEAN,
    danceability DOUBLE,
    energy DOUBLE,
    musical_key INT,
    loudness DOUBLE,
    modo INT,
    speechiness DOUBLE,
    acousticness DOUBLE,
    instrumentalness DOUBLE,
    liveness DOUBLE,
    valence DOUBLE,
    tempo DOUBLE,
    time_signature INT,
    track_genre VARCHAR(100)
);

-- ================================
-- Tabela: imdb
-- ================================
CREATE TABLE imdb (
    id INT AUTO_INCREMENT PRIMARY KEY,
    poster_link TEXT,
    series_title VARCHAR(300),
    released_year INT,
    certificate VARCHAR(10),
    runtime VARCHAR(20),
    genre VARCHAR(200),
    imdb_rating DECIMAL(3,1),
    overview TEXT,
    meta_score INT,
    director VARCHAR(200),
    star1 VARCHAR(200),
    star2 VARCHAR(200),
    star3 VARCHAR(200),
    star4 VARCHAR(200),
    no_of_votes INT,
    gross BIGINT
);

-- ================================
-- Tabela: sazonalidade
-- ================================
CREATE TABLE sazonalidade (
    id_registro INT AUTO_INCREMENT PRIMARY KEY,
    tmdb_id INT,
    original_title VARCHAR(300),
    original_language VARCHAR(50),
    release_date DATE,
    popularity DECIMAL(10,3),
    vote_average DECIMAL(4,2),
    vote_count INT,
    media_type VARCHAR(10),
    adult TINYINT(1)
);
