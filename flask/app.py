from random import randint
import smtplib
from flask import Flask,render_template, session, redirect, url_for, flash
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
# import detail
from image_process import take_nd_crop, find_max, img_name_count, img_name_nickname_preference, image_names, get_ratio_list, rows
import cctv
from counter import find_counter


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
    
@app.route("/select", methods=['GET', 'POST'])
def select():
    ans = None
    ans_counter = None
    if 'username' in session:
        if request.method == 'POST':
            if 'tablePost' in request.form:
                # urls = ["http://10.12.46.193:8080/shot.jpg", "http://10.12.34.208:8080/shot.jpg", "foot/shot.jpg", "newmessup/shot.jpg"]
                # cctv.get_image(urls[0], "hots")
                # cctv.get_image(urls[1], "host")
                # cctv.get_image(urls[2], "foot")
                # cctv.get_image(urls[3], "newmessup")
                num = int(request.form['num-people'])
                pref = request.form['table-pref']
                dict1 = take_nd_crop(image_names, img_name_count)
                densitylist = get_ratio_list(dict1)
                cansitOrnot, table = find_max(dict1, img_name_nickname_preference, pref, num)
                #ans has the values like the image map, ifprefsideisemptyenoughornot, the most suitable place, the rows list and their densities
                # ans  = ["lab_map/lab_map_right.png", cansitOrnot, table, rows, densitylist]
                if "Hotspot Entry Side" == table:
                    ans  = ["mess_map/Hotspot_Entry_Side.png", cansitOrnot, table, rows, densitylist]
                elif "Hotspot Middle Side" == table:
                    ans  = ["mess_map/Hotspot_Middle_Side.png", cansitOrnot, table, rows, densitylist]
                elif "Hotspot Counter Side" == table:
                    ans  = ["mess_map/Hotspot_Counter_Side.png", cansitOrnot, table, rows, densitylist]
                elif "Hostel Entry Side" == table:
                    ans  = ["mess_map/Hostel_Entry_Side.png", cansitOrnot, table, rows, densitylist]
                elif "Hostel Middle Side" == table:
                    ans  = ["mess_map/Hostel_Middle_Side.png", cansitOrnot, table, rows, densitylist]
                elif "Hostel Counter Side" == table:
                    ans  = ["mess_map/Hostel_Counter_Side.png", cansitOrnot, table, rows, densitylist]
                elif "Football Entry Side" == table:
                    ans  = ["mess_map/Football_Entry_Side.png", cansitOrnot, table, rows, densitylist]
                elif "Football Middle Side" == table:
                    ans  = ["mess_map/Football_Middle_Side.png", cansitOrnot, table, rows, densitylist]
                elif "Football Counter Side" == table:
                    ans  = ["mess_map/Football_Counter_Side.png", cansitOrnot, table, rows, densitylist]
                elif "InsideStairs Counter Side" == table:
                    ans  = ["mess_map/InsideStairs_Counter_Side.png", cansitOrnot, table, rows, densitylist]
                elif "InsideStairs Middle Side" == table:
                    ans  = ["mess_map/InsideStairs_Middle_Side.png", cansitOrnot, table, rows, densitylist]
                elif "InsideStairs TV Side" == table:
                    ans  = ["mess_map/InsideStairs_TV_Side.png", cansitOrnot, table, rows, densitylist]
                else:
                    ans  = ["mess_map/No_Place.png", "Come Later", "Not enough space for your group", rows, densitylist]
            elif 'counterPost' in request.form:
                emptycounter = find_counter()
                ans_counter = [f"mess_map/{emptycounter}.png", "The Most Vacant Counter is", emptycounter]
        return render_template('select.html', name=session['username'], ans=ans, ans_counter=ans_counter)
    else:
        return redirect(url_for('loginpage'))
    #for lab demo-
    # if 'username' in session:
        
    #     if request.method == 'POST':
            # urls = ["http://10.12.46.193:8080/shot.jpg", "http://10.12.34.208:8080/shot.jpg"]
            # cctv.get_image(urls[0], "labroom1")
            # cctv.get_image(urls[1], "labroom2")
    #         num = int(request.form['num-people'])
    #         # pref = request.form['table-pref']
    #         str, amt, numlist = take_nd_crop(image_names)
    #         if num>amt:
    #             ans = "Not enough place in either of the sides"
    #             print(list)
    #         else:
    #             if "LeftSide" in str:
    #                 ans = ["lab_map/lab_map_left.png", str, numlist]
    #             else:
                    # ans = ["lab_map/lab_map_right.png", str, numlist]
    #             print(list)
    #         # table = find_max(dict1, img_name_nickname_preference, pref, num)
    #     return render_template('select.html', name=session['username'], ans=ans)
    # else:
    #     return redirect(url_for('loginpage'))

@app.route("/help")
def help():
    if 'username' in session:
        return render_template('help.html', name=session['username'])
    else:
        return redirect(url_for('loginpage'))
    


@app.route('/terms-of-service')
def terms_of_service():
    return render_template('terms_conditions.html')


@app.route("/map")
def map():
    if 'username' in session:
        return render_template('map.html', name=session['username'])
    else:
        return redirect(url_for('loginpage'))


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///eateasyusers.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class userdata(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)

with app.app_context():
    db.create_all()

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
        email = request.form['email'].lower()
        password = request.form['password']
        save_password = request.form.get('save_password')
        if not (10 <= len(username) <= 12):
            signup = False
        elif userdata.query.filter_by(username=username).first():
            signup = False
        else:
            password_hash = generate_password_hash(password)
            user = userdata(name=name, username=username, email=email, password=password_hash)
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

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        
        email = request.form.get('email')
        user = userdata.query.filter_by(email=email).first()
        # Check if email exists in user database
        if user:
            # Generate OTP
            otp = str(randint(1000, 2000))
            ran = "Hello"
            q = "dog"
            # q = detail.Dog()
            # Send OTP to user's email
            sender_email = q.mail
            receiver_email = email
            password = q.psw
            message = f"""
            Subject: Reset Password OTP
            
            Your OTP to reset your password is {otp}.
            Please do not share this with anyone.
            """
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)

            # Store OTP and email in session
            session['otp'] = otp
            session['email'] = email

            # Redirect to enter OTP page
            return redirect(url_for('enter_otp'))

        # Email does not exist in user database
        else:
            return render_template('forgot-password.html', error="Email not found")

    return render_template('forgot-password.html')


# Enter OTP page
@app.route('/enter_otp', methods=['GET', 'POST'])
def enter_otp():
    if request.method == 'POST':
        otp = request.form.get('otp')

        # Check if OTP matches
        if session['otp'] == otp:
            return redirect(url_for('reset_password'))

        # OTP does not match
        else:
            return render_template('enter_otp.html', error="OTP incorrect")

    return render_template('enter_otp.html')


# Reset password page
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = session['email']
        password = request.form.get('password')
        user = userdata.query.filter_by(email=email).first()

        # Update password in user database
        password_hash = generate_password_hash(password)
        user.password = password_hash
        db.session.commit()
        # Clear session
        session.pop('otp', None)
        session.pop('email', None)

        return redirect(url_for('loginpage'))
    return render_template('reset_password.html')


if __name__ == "__main__":
    app.run(debug =True)