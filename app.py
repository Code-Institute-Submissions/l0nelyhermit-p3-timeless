from flask import Flask, render_template
import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# SET UP MONGO CONNECTION
MONGO_URI = os.environ.get('MONGO_URI')
DATABASE = 'Watches'
COLLECTION = 'listing'
# Connection to MONGODB
connect = pymongo.MongoClient(MONGO_URI)
db = connect[DATABASE][COLLECTION]


@app.route('/')
def index():
    # data = db.find({})
    return render_template("index.html")

@app.route('/create')
def create():
    return render_template("create_post.html")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
