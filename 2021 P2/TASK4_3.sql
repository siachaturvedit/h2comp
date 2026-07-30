SELECT competitor.name, AVG(scores.score) 
    FROM competitor JOIN scores 
    ON competitor.id = scores.id
    GROUP BY competitor.name
    ORDER BY name ASC;