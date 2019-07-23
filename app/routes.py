from app import app
from flask import render_template, request
from app.models import model, formopener


@app.route('/')
@app.route('/index')
def index():
    return render_template ('index.html')
@app.route('/oddeven',  methods = ['GET', 'POST'])#two ways of getting to a page, get: u type in the url, post: userdata grings u to it
def oddeven():
    userData= dict(request.form) #takes info from index page, puts it in a dictionary, then we're redefining the data.
    phrase = userData["sentence"]
    totletters=len(phrase)
    letters= totletters - (int(phrase.count(' ')))
    print(letters)
    if request.method == 'GET':  # takes the data from tbe html form
        return 'Go back and answer'
        
    else:
        if letters%2==0:
            oddeven = 'your sentence is even'
            return oddeven
        else:
            oddeven = 'your sentence is odd'
            return oddeven 
        
    return render_template('oddeven.html', letters = letters, oddeven = oddeven)
    


#userData.sentence[]=