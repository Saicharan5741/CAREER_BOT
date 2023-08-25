from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
from flask_pymongo import PyMongo
from pymongo import MongoClient
from chat import get_response

app = Flask(__name__, static_folder='static')
CORS(app)

# Configure Flask-PyMongo
app.config['MONGO_URI'] = 'mongodb://localhost:27017/projectlogin'
mongo = PyMongo(app)

app.secret_key = '1234@@'

# Configure MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['projectlogin']
users_collection = db['sai']

@app.route('/')
def home():
    if 'email' in session:
        return render_template("Home.html")
    else:
        return render_template("login.html")

@app.route('/jobs.html')
def jobs():
    if 'email' in session:
        return render_template('jobs.html')
    else:
        return render_template("login.html")

@app.route('/course.html')
def course():
    if 'email' in session:
        return render_template('course.html')
    else:
        return render_template("login.html")
@app.route('/frontend.html')
def cfront():
    if 'email' in session:
        return render_template('frontend.html')
    else:
        return render_template("login.html")
@app.route('/Backend.html')
def cback():
    if 'email' in session:
        return render_template('backend.html')
    else:
        return render_template("login.html")
@app.route('/Devops.html')
def cdev():
    if 'email' in session:
        return render_template('devops.html')
    else:
        return render_template("login.html")
@app.route('/PostgreSQL DBA.html')
def cpos():
    if 'email' in session:
        return render_template('POSTGRESQL.html')
    else:
        return render_template("login.html")
@app.route('/Android developer.html')
def cand():
    if 'email' in session:
        return render_template('android.html')
    else:
        return render_template("login.html")
@app.route('/Blockchain.html')
def cblock():
    if 'email' in session:
        return render_template('Blockchain.html')
    else:
        return render_template("login.html")

@app.route('/React.html')
def creact():
    if 'email' in session:
        return render_template('React.html')
    else:
        return render_template("login.html")
@app.route('/Angular.html')
def cAngular():
    if 'email' in session:
        return render_template('Angular.html')
    else:
        return render_template("login.html")

@app.route('/Java Script.html')
def cjava():
    if 'email' in session:
        return render_template('Java Script.html')
    else:
        return render_template("login.html")
@app.route('/Vue.html')
def cVue():
    if 'email' in session:
        return render_template('Vue.html')
    else:
        return render_template("login.html")
@app.route('/Type Script.html')
def ctype():
    if 'email' in session:
        return render_template('Type Script.html')
    else:
        return render_template("login.html")
@app.route('/Java.html')
def cJava():
    if 'email' in session:
        return render_template('Java.html')
    else:
        return render_template("login.html")
@app.route('/Spring Boot.html')
def cspring():
    if 'email' in session:
        return render_template('Spring Boot.html')
    else:
        return render_template("login.html")
@app.route('/Python.html')
def cPython():
    if 'email' in session:
        return render_template('Python.html')
    else:
        return render_template("login.html")
@app.route('/About.html')
def cqbout():
    if 'email' in session:
        return render_template('About.html')
    else:
        return render_template("login.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the user exists in the database
        user = users_collection.find_one({'email': email, 'password': password})
        if user:
            # User exists, perform login logic
            session['email'] = email
            return render_template('Home.html')
        else:
            # User doesn't exist or invalid credentials
            return jsonify({'message': 'Invalid email or password'})

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['user']
        email = request.form['email']
        password = request.form['password']

        # Check if the email already exists in the database
        existing_user = users_collection.find_one({'email': email})
        if existing_user:
            return jsonify({'message': 'Email already exists'})

        # Insert new user into the database
        new_user = {'email': email, 'password': password,'user':user}
        users_collection.insert_one(new_user)

        session['email'] = email
        session['user']=user
        return jsonify({'message': 'Registration successful'})

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return render_template('login.html')

@app.post("/predict")
def predict():
    text= request.get_json().get("message")

    # TODO: check if it is a valid input
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
