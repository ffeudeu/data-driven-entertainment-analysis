# data-driven-entertainment-analysis
Projeto de análise de dados orientado a negócios, utilizando Big Data para apoiar decisões estratégicas no setor de entretenimento.

## Contexto
Uma empresa do setor de entretenimento pretende desenvolver um filme ou série baseado em grandes franquias de jogos.  
Para reduzir riscos financeiros e aumentar as chances de sucesso, o projeto adota uma abordagem **data-driven**, analisando dados de jogos, música, filmes e séries antes do início da produção.

## Objetivo
Apoiar a tomada de decisão sobre:
- Qual jogo deve servir de base para adaptação
- Qual estilo musical e artista comporiam a trilha sonora
- Definição entre filme ou série
- Estimativa de orçamento médio
- Melhor período do ano para lançamento

## Perguntas de Negócio
**Jogos**
- Qual jogo apresenta maior número de downloads/jogadores?
- Qual gênero é mais popular?

**Música**
- Quais estilos musicais apresentam maior popularidade?
- Quais artistas estão em alta?

**Formato**
- O público consome mais filmes ou séries?
- Qual formato apresenta melhor custo-benefício?

**Orçamento**
- Qual o custo médio de produções similares?
- Existe relação entre orçamento e sucesso?

**Lançamento**
- Qual período do ano apresenta maior potencial de consumo?

## Metodologia
O projeto foi dividido em três etapas:

### 1. Análise Estatística e SQL + Python
- Criação de banco de dados relacional a partir de arquivos CSV
- Consultas SQL estratégicas
- Análise estatística utilizando Pandas

### 2. Big Data com Polars
- Conversão dos dados para formato Parquet
- Processamento e análise com Polars
- Aplicação de correlação e regressão linear

### 3. Visualização de Dados
- Criação de dashboard no Power BI
- Apresentação visual das decisões estratégicas
- Construção de narrativa baseada em dados (Data Storytelling)

## Tecnologias Utilizadas
- SQL
- Python
- Pandas
- Polars
- Power BI
- CSV / Parquet

## Estrutura do Projeto
- **sql/**: criação de tabelas e consultas SQL  
- **python/**: scripts de ETL e análises estatísticas  
- **dados/**: datasets utilizados (CSV)  

## Status
Projeto acadêmico com foco prático em análise de dados e Big Data.
