from flask import Flask,render_template, session, redirect, url_for, flash
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'eateasysmart2023'

@app.route("/")
def index():
    if 'username' in session and 'name' in session:
        return render_template('index.html', name=session['name'])
    else:
        return redirect(url_for('loginpage'))

@app.route("/about")
def about():
    if 'username' in session:
        return render_template('about.html', name=session['username'])
    else:
        return redirect(url_for('loginpage'))
@app.route("/select")
def select():
    if 'username' in session:
        return render_template('select.html', name=session['username'])
    else:
        return redirect(url_for('loginpage'))

@app.route("/help")
def help():
    if 'username' in session:
        return render_template('help.html', name=session['username'])
    else:
        return redirect(url_for('loginpage'))

@app.route("/map")
def map():
    if 'username' in session:
        return render_template('map.html', name=session['username'])
    else:
        return redirect(url_for('loginpage'))


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///eateasydata.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class userdata(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)

# with app.app_context():
#     db.create_all()

@app.route("/loginpage", methods=['GET', 'POST'])
def loginpage():
    # If the user is already logged in, redirect to the index page
    if 'username' in session:
        return redirect(url_for('index'))
    
    data = {}
    if request.method == 'POST':
        username = request.form['username'].upper()
        password = request.form['password']
        remember = request.form.get('remember')
        user = userdata.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = username
            session['name'] = user.name
            # set the session to permanent if "remember" is checked
            if remember:
                session.permanent = True
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html', data=data)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    signup = True
    data = {}
    if request.method =='POST':
        name = request.form['name']
        username = request.form['username'].upper()
        password = request.form['password']
        save_password = request.form.get('save_password')
        if not (10 <= len(username) <= 12):
            signup = False
        elif userdata.query.filter_by(username=username).first():
            signup = False
        else:
            password_hash = generate_password_hash(password)
            user = userdata(name=name, username=username, password=password_hash)
            if save_password:
                user.password = password
            db.session.add(user)
            db.session.commit()
            data = {"username": username, "name": name, "signup": signup}
            return redirect(url_for('loginpage'))
    return render_template('signup.html', data=data)

@app.route("/userfeedback", methods=['GET', 'POST'])
def userfeedback():
    # If the user is not logged in, redirect to the login page
    if 'username' not in session:
        return redirect(url_for('loginpage'))
    rating = None
    if request.method == 'POST':
        rating = request.form['rating']
        # Update the user's rating in the database
        user = userdata.query.filter_by(username=session['username']).first()
        user.rating = int(rating)
        db.session.commit()
    return render_template('userfeedback.html', rating=rating)

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('loginpage'))


if __name__ == "__main__":
    app.run(debug =True)