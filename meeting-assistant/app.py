from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# Initialize session variables
@app.before_request
def initialize_session():
    if "agenda_items" not in session:
        session["agenda_items"] = []
    if "participants" not in session:
        session["participants"] = []
    if "meeting_details" not in session:
        session["meeting_details"] = {}

@app.route("/")
def agenda():
    return render_template("agenda.html", agenda_items=session["agenda_items"])

@app.route("/add_agenda_item", methods=["POST"])
def add_agenda_item():
    item = request.form.get("new_agenda_item").strip()
    if item:
        session["agenda_items"].append(item)
        session.modified = True
    return redirect(url_for("agenda"))

@app.route("/remove_agenda_item/<int:index>")
def remove_agenda_item(index):
    if 0 <= index < len(session["agenda_items"]):
        session["agenda_items"].pop(index)
        session.modified = True
    return redirect(url_for("agenda"))

@app.route("/reorder_agenda", methods=["POST"])
def reorder_agenda():
    from_index = int(request.form.get("from_index"))
    to_index = int(request.form.get("to_index"))
    if 0 <= from_index < len(session["agenda_items"]) and 0 <= to_index < len(session["agenda_items"]):
        session["agenda_items"].insert(to_index, session["agenda_items"].pop(from_index))
        session.modified = True
    return redirect(url_for("agenda"))

@app.route("/meeting_details", methods=["GET", "POST"])
def meeting_details():
    if request.method == "POST":
        session["meeting_details"] = {
            "title": request.form.get("title"),
            "date": request.form.get("date"),
            "time": request.form.get("time"),
            "location": request.form.get("location"),
        }
        session.modified = True
        return redirect(url_for("meeting_details"))
    return render_template("meeting_details.html", meeting_details=session["meeting_details"])

@app.route("/participants", methods=["GET", "POST"])
def participants():
    if request.method == "POST":
        participant = request.form.get("new_participant").strip()
        if participant:
            session["participants"].append(participant)
            session.modified = True
    return render_template("participants.html", participants=session["participants"])

@app.route("/remove_participant/<int:index>")
def remove_participant(index):
    if 0 <= index < len(session["participants"]):
        session["participants"].pop(index)
        session.modified = True
    return redirect(url_for("participants"))

@app.route("/summary")
def summary():
    return render_template(
        "summary.html",
        agenda_items=session["agenda_items"],
        meeting_details=session["meeting_details"],
        participants=session["participants"],
    )

if __name__ == "__main__":
    app.run(debug=True)