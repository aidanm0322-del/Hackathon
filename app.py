from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html", active="dashboard")

@app.route("/checkin")
def checkin():
    return render_template("coming_soon.html", active="checkin", title="Daily Check-In")

@app.route("/medications")
def medications():
    return render_template("coming_soon.html", active="medications", title="Medications")

@app.route("/assistant")
def assistant():
    return render_template("coming_soon.html", active="assistant", title="AI Recovery Assistant")

@app.route("/vitals")
def vitals():
    return render_template("coming_soon.html", active="vitals", title="Vitals")

@app.route("/emergency")
def emergency():
    return render_template("coming_soon.html", active="emergency", title="Emergency Guidance")

if __name__ == "__main__":
    app.run(debug=True)