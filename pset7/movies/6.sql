SELECT AVG(rating)
FROM ratings JOIN movies On movies.id = ratings.movie_id
WHERE year = 2012;