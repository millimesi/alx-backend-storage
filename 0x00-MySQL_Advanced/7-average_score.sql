--  creates a trigger
-- validating email

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id INT
)
BEGIN
	-- variable for average score
	DECLARE avg_score DECIMAL(10, 2);

	-- Calculate the avg
	SELECT AVG(score)
	INTO avg_score
	FROM corrections
	WHERE user_id = user_id;
	
	-- update the result
	UPDATE users
	SET average_score = avg_score
	WHERE id = user_id;
END //

DELIMITER ;
