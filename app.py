from flask import Flask, request, redirect, render_template, url_for
from flask import session as login_session


app = Flask(__name__)

app.config['SECRET_KEY'] = 'shir'

@app.route('/', methods = ["GET"])
def home():
	return render_template("home.html")

@app.route('/addPlace', methods=['POST'])
def addPlace():
	if request.method == "POST":
		add_place(request.form['name'], request.form['city'], request.form['street'])
		return home()

	else:
		return 'Invalid password <br> <a href="/">Home</a>'

if __name__ == '__main__':
	app.run(debug=True)