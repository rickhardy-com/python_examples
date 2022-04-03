from sqlite3 import connect
from requests import get

apiKey = 'K7fuod7u2z29gpachtqjJes9aKtbn02zbkIliM2q'

asteroid_recs = []

def fetchAsteroidNeowsFeed():
  URL_NeoFeed = "https://api.nasa.gov/neo/rest/v1/feed"
  params = {
      'api_key':apiKey,
      'start_date':'2022-03-30',
      'end_date':'2022-03-30'
  }
  response = get(URL_NeoFeed,params=params).json()
  #pp.pprint(response)
  return response
asteroids = fetchAsteroidNeowsFeed()


for rec_no, all_asteroids in enumerate(asteroids['near_earth_objects']['2022-03-30']):
    
    asteroid_rec = (asteroids['near_earth_objects']['2022-03-30'][rec_no]['name'], \
                    asteroids['near_earth_objects']['2022-03-30'][rec_no]['links']['self'], \
                    asteroids['near_earth_objects']['2022-03-30'][rec_no]['id'], \
                    asteroids['near_earth_objects']['2022-03-30'][rec_no]['nasa_jpl_url'],\
                    asteroids['near_earth_objects']['2022-03-30'][rec_no]['is_potentially_hazardous_asteroid'],\
                    asteroids['near_earth_objects']['2022-03-30'][rec_no]['absolute_magnitude_h'], \
                    asteroids['near_earth_objects']['2022-03-30'][rec_no]['estimated_diameter']['kilometers']['estimated_diameter_min'], \
                    asteroids['near_earth_objects']['2022-03-30'][rec_no]['estimated_diameter']['kilometers']['estimated_diameter_max'])
                    
    asteroid_recs.append (asteroid_rec)

for rec2 in asteroid_recs:
    print (rec2)

# create an instance of the connect class
conn = connect('pythonex1.db')
c = conn.cursor()

# create table
c.execute(' DROP TABLE asteroids')

c.execute('''CREATE TABLE /*IF NOT EXISTS*/ asteroids (
                                                 name,
                                                 links,
                                                 id,
                                                 nasa_jpl_url,
                                                 is_potentially_hazardous_asteroid,
                                                 absolute_magnitude_h,
                                                 estimated_diameter_min,
                                                 estimated_diameter_max
                                                )'''
          )

# fill tables with data
for data_row in asteroid_recs:
    c.execute('INSERT into asteroids VALUES (?,?,?,?,?,?,?,?)', data_row)

# commit and close
c.close()
conn.commit()
conn.close()
