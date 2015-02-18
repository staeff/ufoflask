# Geolocation App

Following this article:  
http://tech.pro/tutorial/1213/how-to-build-an-api-with-python-and-flask

## First step

* configure db-uri in config.py and read it into routes.py with
  app.config.from_object('config')

* initialize db with init-db.py

## Second step

* create the table in the database and fill it with data. (create-populate-db.py)
  For this we read the sightings.tsv - file. This works by using SQL. I think
  it would have been possible to go the SQLAlchemy route, if the Model had been
  in Place??


## Third Step

* write the Model in routes.py
* create requirements.txt
* Update README

## Fourth Step

* write views  
  * all sightings: <server>/sightings
  * all sightings with limit and offset param: <server>/sightings/?limit=3&offset=30.
  * single sighting: <server>/sightings/1

## Fifth Step

* implement nearby search following this:
https://developers.google.com/maps/articles/phpsqlsearch_v3#findnearsql
