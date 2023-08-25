from flask import Flask,render_template,request,jsonify
from flask_cors import CORS



from chat import get_response

app = Flask(__name__,static_folder='static')

CORS(app)

@app.route('/')
def home():
     return render_template("Home.html")
@app.route('/jobs.html')
def jobs():
    return render_template('jobs.html')
@app.route('/login.html')
def login():
    return render_template('login.html')

@app.post("/predict")
def predict():
    text= request.get_json().get("message")

    # TODO: check if it is a valid input
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__=="__main__":
    app.run(debug=True)