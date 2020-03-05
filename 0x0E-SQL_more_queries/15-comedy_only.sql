-- atabase dump from hbtn_0d_tvshows to your MySQL server
-- (same as 14-my_genres.sql)
SELECT tv_shows.title FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_genres.name = 'Comedy' ORDER BY tv_shows.title ASC;
