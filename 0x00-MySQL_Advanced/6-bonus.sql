--  creates a trigger
-- validating email

DELIMITER //

CREATE PROCEDURE AddBonus(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score INT
)
BEGIN
	DECLARE project_id INT;

	-- see if project exists or create it
	SELECT id INTO project_id
	FROM projects
	WHERE name = project_name;

	IF project_id IS NULL THEN
		-- create it
		INSERT INTO projects (name) VALUES (project_name);
		SET project_id = LAST_INSERT_ID();
	END IF;

	-- insert the correction
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END //

DELIMITER ;
