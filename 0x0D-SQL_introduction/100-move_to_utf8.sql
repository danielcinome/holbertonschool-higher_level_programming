-- script that converts hbtn_0c_0 database to UTF8 (utf8mb4
-- collate utf8mb4_unicode_ci) in your MySQL server.
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_unicode_ci;
ALTER TABLE second_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;
