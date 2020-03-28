# Python - Object-relational mapping
![N|Solid](https://www.holbertonschool.com/holberton-logo.png)
--
## Background Context

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module  `MySQLdb`  to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module  `SQLAlchemy`  (dont ask me how to pronounce it) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be What can I do with my objects and not How this object is stored? where? when?. You wont write any SQL queries only Python code. Last thing, your code wont be storage type dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:

```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

```

With an ORM:

```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
## More Info

### Install  `MySQLdb`  module version  `1.3.x`

For installing  `MySQLdb`, you need to have  `MySQL`  installed:  [How to install MySQL 5.7 in Ubuntu 14.04](https://intranet.hbtn.io/rltoken/PW9oQwiiM7BuaKtPEoPJVA "How to install MySQL 5.7 in Ubuntu 14.04")

```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__ 
'1.3.10'

```

### Install  `SQLAlchemy`  module version  `1.2.x`

```
$ pip3 install SQLAlchemy==1.2.5
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.2.5'

```

Also, you can have this warming message:

```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
    ```

    You can ignore it.
```
