from flask import *
from flask_cors import CORS
from test import method


app=Flask(__name__)
CORS(app)

@app.route('/mupparaju',methods=['POST'])
def startvid():
    data = request.json
    method()
app.run()