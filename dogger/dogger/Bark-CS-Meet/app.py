from database import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session
from model import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/index.html')
def home():
	return render_template('index.html')
# This is a test to see something cool
@app.route('/')
def NewHome():
	return home()

@app.route('/dogpage.html')
def DogPage():
	return render_template('dogpage.html')

@app.route('/check.html')
def Check():
	return render_template('check.html')

@app.route('/starter.html')
def starter():
	return render_template('starter.html')

@app.route('/third.html')
def third():
	return render_template('third.html')


@app.route('/adopt.html' , methods=['GET','POST'])
def upload():
	if request.method == 'GET' :
		return render_template('adopt.html')
	else:
		print("creating object")
		name_of_place = request.form['nameOfplace']
		description = request.form['subject']
		date_of_visit = request.form['Date']
		link = request.form['Link']

		add_place(name_of_place , description , date_of_visit , link)
		return redirect('index.html')


# @app.route('/list.html')
# def fullList():
# 	places=query_all()
# 	return render_template('list.html',places=places)

# @app.route('/place.html/<int:p_id>')
# def place(p_id):
# 	place=session.query(Place).filter_by(id=p_id).one()
# 	return render_template('place.html',place=place)

# --------------------------------------------------
# UP IS STILL IN PROGRESS
# ----------------------------------------------------

# @app.route('/blog.html',methods=["GET","POST"])
# def blog():
# 	if request.method == "GET":
# 		return render_template("blog.html")
# 	else :
# 		username = request.form['username']
# 		event = request.form["event"]
# 		phonenumber = request.form["phonenumber"]
# 		add_event(username,event,phonenumber)
# 		return NewHome()
# @app.route('/about.html')
# def about():
# 	return render_template("about.html")














# @app.route('/login', methods=['POST'])
# def login():
#     user = get_user(request.form['username'])
#     if user != None and user.verify_password(request.form["password"]):
#         login_session['name'] = user.username
#         login_session['logged_in'] = True
#         return logged_in()
#     else:
#         return home()


# @app.route('/signup', methods=['POST'])
# def signup():
#     #check that username isn't already taken
#     user = get_user(request.form['username'])
#     if user == None:
#         add_user(request.form['username'],request.form['password'])
#     return home()


# @app.route('/logged-in')
# def logged_in():
#     return render_template('logged.html')


# @app.route('/logout')
# def logout():
#     login_session['name'] = None
#     login_session['logged_in'] = False
#     return home()



if __name__ == '__main__':
	app.run(debug=True)
