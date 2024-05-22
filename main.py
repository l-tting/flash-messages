from  flask import Flask,render_template,flash,request,redirect,url_for

app = Flask(__name__)
app.secret_key = 'hejjkdjkkd3848' 

@app.route('/')
def home():
    flash('This is home','success')
    flash('Go to login','error')
    return render_template('index.html')

   
app.run(debug=True)