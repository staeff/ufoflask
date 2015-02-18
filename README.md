# Geolocation App

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
