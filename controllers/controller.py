from app import app
from flask import render_template, request, redirect
from models.events_test import events
from models.events import Event

@app.route('/')
def index():
    return render_template('index.html', events = events)

@app.route("/add_event", methods = ["POST"])
def new_event():
    print (request.form)
    event_name = request.form['name']
    event_date = request.form['date']
    number_of_guests = request.form['number_of_guests']
    room_location = request.form['room_location']
    description = request.form['description']
    if request.form['recurring'] == "True":
        recurring = True
    else:
        recurring = False
    print(recurring)
    new_event = Event(event_date, event_name, number_of_guests, room_location, description, recurring)
    events.append(new_event)
    return redirect("/")

@app.route("/delete_event", methods = ["POST"])
def delete_event():
    print(request.form)
    for event in events:
        if event.name_of_event == request.form['name']:
            events.remove(event)
    return redirect("/")
    
