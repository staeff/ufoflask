# Installation on codio.com

## Install MySQL and load data
```
$ parts install mysql
$ parts start mysql
$ wget https://www.dropbox.com/s/aoim0kwg7v30fii/sightings.tsv
$ mysql -u root 
mysql> CREATE DATABASE ufosightings;
$ mysql --local-infile=1 -u root -D ufosightings < create_table_read_data.sql
```

## Install Python and Modules
```
$ parts install pip
```

## Install Flask
```
$ pip install -r requirements.txt
```

## Run the program
```
$ python routes.py
```


Learn from here how to secure the database: http://deeb.me/20140324/django-on-codio