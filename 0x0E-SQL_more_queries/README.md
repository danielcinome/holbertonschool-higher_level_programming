# SQL - More queries

![N|Solid](https://www.holbertonschool.com/holberton-logo.png)

### How to import a SQL dump

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

![N|SOLID](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUZGDONYM4%2F20200303%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200303T162347Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5c5f47909a1e01bf63e7993473e7ec27aebc3f6b40353c53128834fbdd46f4c9)
