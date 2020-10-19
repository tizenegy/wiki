# call this script in shell:
# python manage.py shell < db_populate.py

from flights.models import *

# available airports:
jfk = Airport(code="JFK", city="New York")
lhr = Airport(code="LHR", city="London")
cdg = Airport(code="CDG", city="Paris")
nrt = Airport(code="NRT", city="Tokyo")
kol = Airport(code="KOL", city="Kolbermoor")
gfb = Airport(code="GFB", city="Grossfischbach")
kol.save()
gfb.save()
jfk.save()
lhr.save()
cdg.save()
nrt.save()

# new flights:
f = Flight(origin=jfk, destination=cdg, duration=414)
f.save()
f = Flight(origin=jfk, destination=nrt, duration=700)
f.save()
f = Flight(origin=lhr, destination=jfk, duration=400)
f.save()
f = Flight(origin=lhr, destination=cdg, duration=90)
f.save()
f = Flight(origin=lhr, destination=nrt, duration=600)
f.save()
f = Flight(origin=kol, destination=gfb, duration=60)
f.save()