# A RESTful API build with Python and Flask.

http://tech.pro/tutorial/1213/how-to-build-an-api-with-python-and-flask

**API:** a collection of functions that allow a software program to access data
from an application. The software program can read or change the application's
data by calling these functions.

**REST (Representational State Transfer):** a set of rules that clients and servers
must follow when communicating with each other. If a communications system follows
these rules, it is called RESTful. HTTP is a RESTful communications protocol
(argueably the most famous one).

**RESTful service:** a URL should identify a piece of information that
the user might want to interact with. Each piece of information is termed a resource.
Resources can be retrieved and changed using the HTTP verbs:  

* `POST` - create a new resource
* `GET` - read a resource
* `PUT` - update an existing resource
* `DELETE` - deletes a resource

## Topic: UFO-sightings

http://blog.infochimps.com/2011/08/12/find-aliens-near-you/:  
*Infamous 60,000+ Documented UFO Sightings with Text Descriptions. This humble
78 MB dataset (also available as an API) has spawned several fun visualizations
and apps.*

* Original Data is coming from [The National UFO Reporting Center](http://www.nuforc.org/index.html),
the Dataset is enhanced with geo data (Latitude, Longitude)

* [API](http://www.infochimps.com/datasets/60000-documented-ufo-sightings-with-text-descriptions-and-metada#api-explorer_tab)
does not work anymore, but the data is still available https://www.dropbox.com/s/aoim0kwg7v30fii/sightings.tsv

### Implemented queries

Get sightings (limited to 10 by items default)  
* http://{server}/sightings

Get sightings with parameters for number of values and first item  
* http://{server}/sightings/?limit=3&offset=30

Get a specific item by ID  
* http://{server}/sightings/42

Get
* http://{server}/sightings/?location=37.7749295,-122.4194155&radius=25&limit=3  
The SQL-Query for nearby is described here
https://developers.google.com/maps/articles/phpsqlsearch_v3#findnearsql

### Possible queries to implement

* location search by name
* sightings longer, short or equal a certain time period
* use date as parameter (sightings since ... to ..., etc.)

## Secrets from the environment

Article about that:  
http://opensourcehacker.com/2012/12/13/configuring-your-python-application-using-environment-variables/

DBUSER={username} PW={password} python routes.py

## Conclusion

May its not neccessary to implement the REST-behaviour. Just take a package:
https://flask-restless.readthedocs.org/en/latest/
