from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsMyOwnSecretKey' # you need to set a secret key for security purposes
# routing rules and rest of server.py below

@app.route('/')
def index():
  # Form is rendered to pass in data using the index template
  return render_template("index.html")

@app.route('/formData', methods=['POST'])
def create_user():
  #sess('KeyName') set to ( values ) 
  session['data'] = request.form 
  print (" --- Form Data Proccesed --- ")
  return redirect('/show') # redirect to a different route(/show) to process the data.

@app.route('/show')
  #using the values stored on session we can render the data user template
def show_user():
  userData = session['data']
  return render_template('user.html',data=userData)#set the data to value and pass the form data 

app.run(debug=True)
