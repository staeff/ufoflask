from flask import Flask, request, jsonify, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

class Sighting(db.Model):
    __tablename__ = 'sightings'
    id = db.Column(db.Integer, primary_key = True)
    sighted_at = db.Column(db.Date)
    reported_at = db.Column(db.Date)
    location_city = db.Column(db.String(100))
    location_state = db.Column(db.String(100))
    shape = db.Column(db.String(10))
    duration = db.Column(db.String(10))
    description = db.Column(db.Text)
    lat = db.Column(db.Float(6))
    lon = db.Column(db.Float(6))

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/sightings/', methods=['GET'])
def sightings():
    if request.method == 'GET':
        lim = request.args.get('limit', 10)
        off = request.args.get('offset', 0)

        radius = request.args.get('radius', 10)
        location = request.args.get('location', ',')
        lat, lon = location.split(',')

        if lat and lon and radius:
            query = "SELECT id,  location_city, ( 3959 * acos( cos( radians( %(latitude)s ) ) * cos( radians( lat ) ) * cos( radians( lon ) - radians( %(longitude)s ) ) + sin( radians( %(latitude)s ) ) * sin( radians( lat ) ) ) ) AS distance FROM sightings HAVING distance < %(radius)s ORDER BY distance LIMIT %(limit)s" % {"latitude": lat, "longitude": lon, "radius": radius, "limit": lim}
            results = Sighting.query.from_statement(query).all()
        else:
            # SQLAlchemy equivalent to SELECT * from sightings LIMIT 10 OFFSET 0;
            results = Sighting.query.limit(lim).offset(off).all()

        json_results = []
        for result in results:
            d = {'sighted_at': result.sighted_at.strftime('%Y-%m-%d'),
                 'reported_at': result.reported_at.strftime('%Y-%m-%d'),
                 'city': result.location_city,
                 'state': result.location_state,
                 'shape': result.shape,
                 'duration': result.duration,
                 'description': result.description,
                 'lat': result.lat,
                 'lon': result.lon}
            json_results.append(d)

        return jsonify(items=json_results)

@app.route('/sightings/<int:sighting_id>', methods=['GET'])
def sighting(sighting_id):
    if request.method == 'GET':
        result = Sighting.query.filter_by(id=sighting_id).first()

        json_result = {'sighted_at': result.sighted_at.strftime('%Y-%m-%d'),
                   'reported_at': result.reported_at.strftime('%Y-%m-%d'),
                   'city': result.location_city,
                   'state': result.location_state,
                   'shape': result.shape,
                   'duration': result.duration,
                   'description': result.description,
                   'lat': result.lat,
                   'lon': result.lon}


        return jsonify(items=json_result)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
