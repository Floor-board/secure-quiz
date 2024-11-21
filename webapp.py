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
    return render_template('index.html')
@app.route("/page2")
def render_page2():
   session['start_time'] = time.time()
   return render_template('page2.html')
@app.route("/page3")
def render_page3():
   return render_template('page3.html')
@app.route("/page4")
def render_page4():
   return render_template('page4.html')
@app.route("/page5")
def render_page5():
   return render_template('page5.html')
@app.route("/page6")
def render_page6():
   return render_template('page6.html')
@app.route("/page7")
def render_page7():
   return render_template('page7.html')

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

@app.route('/answersFive', methods=['GET', 'POST'])
def handle_form5():
    if "answer5" not in session:  
        session["answer5"]=request.form['Pokemon4']
    score = 0
    session['end_time'] = time.time()
    Ti = session['start_time']
    Tf = session['end_time']
    time1 = Tf - Ti
    if session["answer2"] == "Bulbasour" or session["answer2"] == "bulbasour":
        awns2 = "Correct"
        score = score+1
    else:
        awns2= "Incorrect"
    if session["answer3"] == "Ivysaur" or session["answer3"] == "ivysaur":
        awns3 = "Correct"
        score = score+1
    else:
        awns3 = "Incorrect"
    if session["answer4"] == "Mew" or session["answer4"] == "mew":
        awns4 = "Correct"
        score = score+1
    else:
        awns4 = "Incorrect"
    if session["answer5"] == "Rhydon" or session["answer5"] == "rhydon":
        awns5 = "Correct"
        score = score+1
    else:
        awns5 = "Incorrect"
    percent = score / 4 * 100
    return render_template('page7.html', awnser2 = awns2, awnser3 = awns3, awnser4 = awns4, awnser5 = awns5, awnsTrue = score, Percent = percent, Time = time1)



if __name__=="__main__":
    app.run(debug=True)
