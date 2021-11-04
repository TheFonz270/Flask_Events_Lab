from models.events import Event
import datetime

event1 = Event(datetime.date(2021, 11, 5), "Fireworks", 500, "5-N", "Peeeewwwwwwwwwwwww... BANG!", True )
event2 = Event(datetime.date(2022, 5, 5), "International Food Festival", 375, "1-W", "Mniam mniam!", False )
event3 = Event(datetime.date(2022, 6, 1), "Sports Festival", 200, "Hollyrood Park", "sweat sweat!", True )

events = [event1, event2, event3]