#If geopy module is not installed, use command- pip install geopy
#Importing Geopy module
from geopy.geocoders import Nominatim
import time

app = Nominatim(user_agent = 'tutorial')
def get_loc(adr):
    time.sleep(1)
    try:
        return app.geocode(adr).raw
    except :
        return get_loc(adr)

print('-'*10)
adr = input('Enter the name of a country/state/city:')
print('-'*10)
location = get_loc(adr)

lat = location['lat']
lon = location['lon']
name = location['display_name']

print(f'location = {name} \nlatitude = {lat} longitude = {lon}')

#End of the program