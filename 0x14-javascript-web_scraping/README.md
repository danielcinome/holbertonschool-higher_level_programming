## # Javascript - Web scraping

## More Info

### Install Node 10

```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs

```

### Install semi-standard

[Documentation](https://intranet.hbtn.io/rltoken/GEBmmrmMUnGd20y4k6_4OA "Documentation")

```
$ sudo npm install semistandard --global

```

### Install  `request`  module and use it

[Documentation](https://intranet.hbtn.io/rltoken/9L4UYvlIwDVDoObD7zpJZQ "Documentation")

```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

### Install MySQL 5.7 on Ubuntu 14.04 LTS

```
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$
```


