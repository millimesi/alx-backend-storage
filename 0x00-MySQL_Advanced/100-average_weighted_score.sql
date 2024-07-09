-- creates a stored procedure
-- procedure of ComputeAverageWeightedScoreForUser

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
	IN user_id INT
)
BEGIN
	-- a variable for average score
	DECLARE total_weighted_score DECIMAL(10, 2);
	DECLARE total_weight INT;

	-- average score of specified user_id
    	SELECT SUM(c.score * p.weight), SUM(p.weight)
    	INTO total_weighted_score, total_weight
    	FROM corrections c
    	JOIN projects p ON c.project_id = p.id
    	WHERE c.user_id = user_id;

    	-- users table to be updated
    	UPDATE users
    	SET average_score = total_weighted_score / total_weight
    	WHERE id = user_id;
END //

DELIMITER ;
