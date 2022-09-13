from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import MyNewClock
import clocks
import requests
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

app = Flask(__name__)





def get_philly():
    image = plt.imread('philly.png')  # clock face image
    fig = plt.figure(figsize=(4, 4), dpi=300, facecolor=[0.2, 0.2, 0.2])
    ax_image = fig.add_axes([0, 0, 1, 1])  # add axes for Clock face image
    ax_image.axis('off')
    ax_image.imshow(image)
    axc = fig.add_axes([0.062, 0.062, 0.88, 0.88], projection='polar')  # add another axes for Clock angles
    animationClock = FuncAnimation(fig, MyNewClock.philly_clock, interval=1000, repeat=False)  # clock display

@app.route("/")
def home():
    def start_task():
        def do_work(value):
            websitetopng()
            import time
            time.sleep(value)

        thread = Thread(target=do_work, kwargs={'value': request.args.get('value', 20)})
        thread.start()
        return 'started'
    return render_template("index.html")





## HTTP GET - Read Record
@app.route("/clocks")
def get_philly():
    image = plt.imread('philly.png')  # clock face image
    fig = plt.figure(figsize=(4, 4), dpi=300, facecolor=[0.2, 0.2, 0.2])
    ax_image = fig.add_axes([0, 0, 1, 1])  # add axes for Clock face image
    ax_image.axis('off')
    ax_image.imshow(image)
    axc = fig.add_axes([0.062, 0.062, 0.88, 0.88], projection='polar')  # add another axes for Clock angles
    animationClock = FuncAnimation(fig, MyNewClock.philly_clock, interval=1000, repeat=False)  # clock display

get_philly()
def get_japan():
    image = plt.imread('japan.png')  # clock face image
    fig = plt.figure(figsize=(4, 4), dpi=300, facecolor=[0.2, 0.2, 0.2])
    ax_image = fig.add_axes([0, 0, 1, 1])  # add axes for Clock face image
    ax_image.axis('off')
    ax_image.imshow(image)
    axc = fig.add_axes([0.062, 0.062, 0.88, 0.88], projection='polar')  # add another axes for Clock angles
    animationClock = FuncAnimation(fig, MyNewClock.japan_clock, interval=1000, repeat=False)  # clock display
    return MyNewClock.japan_clock.png

def get_seattle():
    image = plt.imread('seattle.png')  # clock face image
    fig = plt.figure(figsize=(4, 4), dpi=300, facecolor=[0.2, 0.2, 0.2])
    ax_image = fig.add_axes([0, 0, 1, 1])  # add axes for Clock face image
    ax_image.axis('off')
    ax_image.imshow(image)
    axc = fig.add_axes([0.062, 0.062, 0.88, 0.88], projection='polar')  # add another axes for Clock angles
    animationClock = FuncAnimation(fig, MyNewClock.seattle_clock, interval=1000, repeat=False)  # clock display
    return MyNewClock.seattle_clock.png
## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_clock():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})
## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
