--  database dump from hbtn_0d_tvshows to your MySQL server
-- (same as 12-no_genre.sql)
SELECT tv_genres.name as genre, COUNT(tv_show_genres.show_id) as number_of_shows FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY number_of_shows DESC;
