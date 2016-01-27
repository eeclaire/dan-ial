import random
import sys
import os
from flask import Flask
from flask import render_template
from flask import request

# Move to the directory that contains the interfacing script to import it
# (I'm actually pretty proud of this line because it means I can call server.py from anywhere)
#sys.path.append(os.path.join(os.path.dirname(__file__),'..','peer-mentoring-app-interface'))



app = Flask(__name__)

@app.route('/')
def home():
    print os.getcwd()
    print os.listdir(os.curdir)
    
    sg = scramble()

    return render_template('yolo.html',scram=sg)


def scramble():
    gifs = os.listdir("static/gifs/")
    
    scrambled = [ "gifs/" + gif for gif in gifs ]  
    random.shuffle(scrambled)
    
    
    #print gifs
    print scrambled
    return scrambled

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=80)
    
