SELECT competitor.name as name, SUM(scores.score) as total, SUM(scores.score)>250 as qualified
    FROM competitor JOIN scores 
    ON competitor.id = scores.id 
    GROUP BY name 
    ORDER BY qualified DESC, total DESC;