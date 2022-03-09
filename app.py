from flask_mail import Mail , Message
from flask import Flask,request,flash, render_template, url_for, redirect,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] =465
app.config['MAIL_USERNAME'] = 'amanbng25@gmail.com'
app.config['MAIL_PASSWORD'] = 'Almora@123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/index")
def index():
   msg = Message('Hello', sender = 'amansinghalm2002@gmail.com', recipients = ['amanbng25@gmail.com'])
   msg.body = "Dear candidate ,Your registration is completed.  Thank for visiting our websi"
   mail.send(msg)
   return "Sent"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/jewellery")
def jewellery():
    return render_template('jewellery.html')






@app.route("/ourclient")
def ourclient():
    return render_template('ourclients.html')
@app.route('/home')
def aj():
    return render_template('index.html')

db = SQLAlchemy(app)

class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   mobile = db.Column(db.String(50))
   email = db.Column(db.String(200)) 
   message= db.Column(db.String(10))

   def __init__(self, name,mobile, email,message):
      self.name = name
      self.mobile =mobile
      self.email = email
      self.message = message

@app.route('/show_all')
def show_all():
   return render_template('show_all.html', students = students.query.all() )


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['mobile'] or not request.form['email'] :
                flash('Please enter all the fields', 'error')
        else:
                student = students(request.form['name'], request.form['mobile'],request.form['email'], request.form['message'])
                
                db.session.add(student)
                db.session.commit()
                flash('Record was successfully added')
                return redirect(url_for('contact'))
    return render_template('contact.html')




if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)



