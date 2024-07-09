--  creates a trigger
-- validating email

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id INT
)
BEGIN
	-- a variable declared
	DECLARE avg_score DECIMAL(10, 2);

	-- average score
	SELECT AVG(score)
	INTO avg_score
	FROM corrections
	WHERE user_id = user_id;
	
	-- users table updates
	UPDATE users
	SET average_score = avg_score
	WHERE id = user_id;
END //

DELIMITER ;
