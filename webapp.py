from flask import Flask, request, render_template, flash
from markupsafe import Markup
from flask import redirect
from flask import session
import time
import os

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)
app.secret_key=os.environ["SECRET_KEY"]; #This is a variable.

@app.route("/")
def render_main():
    return render_template('index.html', methods=["GET", "POST"])
@app.route("/page2")
def render_page2():
   return render_template('page2.html', methods=["GET","POST"])
@app.route("/page3")
def render_page3():
   return render_template('page3.html')
    
@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect('/')

@app.route('/answersOne', methods=['GET', 'POST'])
def handle_form():
    username = request.form.get('username')
    if "answer1" not in session:  
        session["answer1"]=request.form['username']
    return render_template('page3.html')

@app.route('/answersTwo', methods=['GET', 'POST'])
def handle_form2():
    if "answer2" not in session:  
        session["answer2"]=request.form['Pokemon1']
    awnser2 = request.form['Pokemon1']:
    if awnser2 = bulbasour or Bulbasour:    
        awnser1right = True
    return render_template('page4.html')

@app.route('/answersThree', methods=['GET', 'POST'])
def handle_form3():
    if "answer3" not in session:  
        session["answer3"]=request.form['Pokemon2']
    return render_template('page5.html')

@app.route('/answersFour', methods=['GET', 'POST'])
def handle_form4():
    if "answer4" not in session:  
        session["answer4"]=request.form['Pokemon3']
    return render_template('page6.html')

if __name__=="__main__":
    app.run(debug=False)
