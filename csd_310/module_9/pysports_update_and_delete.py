ELECT player_id, first_name, last_name, team_id from player;

INSERT INTO team (team_name, mascot)
 VALUES('Team Sauron', 'Orcs');

INSERT INTO team (team_name, mascot)
 VALUES('Team Thorin', 'Oakenshield');




INSERT INTO player (player_id, first_name, last_name, team_id)
VALUES ('2', 'Bilbo', 'Baggins', '1');

INSERT INTO player (player_id, first_name, last_name, team_id)
VALUES ('3', 'Frodo', 'Baggins', '1');

INSERT INTO player (player_id, first_name, last_name, team_id)
VALUES ('4', 'Saruman', 'The White', '2');

INSERT INTO player (player_id, first_name, last_name, team_id)
VALUES ('5', 'Angmar', 'Witch-King', '2');

INSERT INTO player (player_id, first_name, last_name, team_id)
VALUES ('6', 'Azog', 'The Defiler', '2');

INSERT INTO player (first_name, last_name, team_id)
VALUES ('Smeogle', 'Shire Folk', '1');


SELECT player_id, first_name, last_name, team_name
FROM player
INNER JOIN team
	ON player.team_id = team.team_id;

SELECT player_id, first_name, last_name, team_name
FROM player
LEFT OUTER JOIN team
	ON player.team_id = team.team_id;

UPDATE player
SET team_id = 2,
	first_name = 'Gollum',
	last_name = 'Ring Stealer'
WHERE first_name = 'Smeogle';

DELETE FROM player
WHERE first_name = 'Gollum';