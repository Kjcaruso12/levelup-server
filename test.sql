SELECT * FROM levelupapi_gametype;

SELECT * FROM auth_user;
SELECT * FROM authtoken_token;
SELECT * FROM levelupapi_gamer;

SELECT * FROM levelupapi_game;

DELETE FROM levelupapi_event
WHERE id = 1

SELECT
    e.*,
    g.title,
    gr.id as gamer_id,
    u.first_name || ' ' || u.last_name as full_name
FROM levelupapi_event e
JOIN levelupapi_game g
    ON e.game_id = g.id
JOIN levelupapi_event_attendees a
    ON a.event_id = e.id
JOIN levelupapi_gamer gr
    ON gr.id = a.gamer_id
JOIN auth_user u
    ON gr.user_id = u.id