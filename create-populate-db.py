#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import unicodecsv

con = sqlite3.connect('./app.db')
cur = con.cursor()
cur.execute("CREATE TABLE if not exists sightings(id INT, sighted_at INT,reported_at INT, \
             location text, shape text, duration text, description text,  \
             lat real, lon real, PRIMARY KEY (id))")

with open('sightings.tsv', 'rb') as input_file:
    reader = unicodecsv.reader(input_file, delimiter="\t")
    data = [row for row in reader]

cur.executemany("INSERT INTO sightings (id, sighted_at, reported_at, location, \
                 shape, duration, description, lat, lon) \
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", data)
con.commit()
