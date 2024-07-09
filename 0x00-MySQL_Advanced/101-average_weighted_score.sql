-- creates a stored procedure
-- procedure of ComputeAverageWeightedScoreForUser

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE user_id INT;
        DECLARE total_weighted_score DECIMAL(10, 2);
        DECLARE total_weight INT;
        DECLARE done INT DEFAULT FALSE;
        DECLARE cur CURSOR FOR SELECT id FROM users;
        DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    	-- Cursor for looping on each user
    	OPEN cur;

    	read_loop: LOOP
        	FETCH cur INTO user_id;
        	IF done THEN
            		LEAVE read_loop;
        	END IF;

        	-- Calculate total the scores of the users
        	SELECT SUM(c.score * p.weight), SUM(p.weight)
        	INTO total_weighted_score, total_weight
        	FROM corrections c
        	JOIN projects p ON c.project_id = p.id
        	WHERE c.user_id = user_id;

        	-- Update the result
        	UPDATE users
        	SET average_score = IFNULL(total_weighted_score / total_weight, 0)
        	WHERE id = user_id;

    	END LOOP;

    	CLOSE cur;
END //

DELIMITER ;
