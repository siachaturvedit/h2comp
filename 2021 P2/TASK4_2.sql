SELECT competitor.name, scores.score 
    FROM competitor JOIN scores ON competitor.id = scores.id
    WHERE round = 1
    ORDER BY scores.score DESC;


SELECT competitor.name, scores.score 
    FROM competitor JOIN scores ON competitor.id = scores.id
    WHERE round = 2
    ORDER BY scores.score DESC;


SELECT competitor.name, scores.score 
    FROM competitor JOIN scores ON competitor.id = scores.id
    WHERE round = 2
    ORDER BY scores.score DESC;