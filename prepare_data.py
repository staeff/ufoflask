#!/usr/bin/env python
# coding=utf-8

# The original data contains a field that represents city and state
# "Iowa City, IA" - I thought it is a good idea to seperate this field
# to make it easier to search for a city or a state
# or run statistics on those items. Which state has the most ufo-sightings
# But for this it would be even more interesting to work with areas deducted
# by the geocoords

import csv

def prepare_date(string):
    """ Inserts hyphens into an datestring with the format yyyymmdd """
    return '{}-{}-{}'.format(string[:4], string[4:6], string[6:8])

with open('sightings.tsv', 'r') as infile:
    reader = csv.reader( infile, delimiter = '\t' )

    with open('sightings-city-state.tsv', 'wb') as outfile:
        writer = csv.writer( outfile, quotechar='"', quoting=csv.QUOTE_NONNUMERIC ,delimiter='\t')
        for line in reader:
            # turn sighting_at and reported_at fields into date formats
            line[1] = prepare_date(line[1])
            line[2] = prepare_date(line[2])
            # remove unneccessary quotationmark
            line[7] = line[7].strip('"')
            data = line.pop(3)
            # There can be multiple commas in the field, i.e.
            # "Washington, D.C., D.C."
            city, state = data.rsplit(',',1)
            line.insert(3, city)
            line.insert(4, state.strip())
            writer.writerow(line)
