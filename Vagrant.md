# Installation in Vagrant (Ubuntu Precise64)

## Install basics
```
$ sudo apt-get install build-essential
```

## Install MySQL and load data
```
$ sudo apt-get install mysql-server mysql-client
$ wget https://www.dropbox.com/s/aoim0kwg7v30fii/sightings.tsv
$ mysql -u root -p  
mysql> CREATE DATABASE ufosightings;
$ mysql --local-infile=1 -u root -p -D ufosightings < create_table_read_data.sql
```

## Install Python and Modules
```
$ sudo apt-get install python
$ sudo apt-get install python-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install python-pip
$ sudo pip install virtualenv
```

## Install Flask
```
$ virtualenv .
$ source bin/activate
$ pip install -r requirements.txt
```

## Run the program
```
$ python routes.py
```
