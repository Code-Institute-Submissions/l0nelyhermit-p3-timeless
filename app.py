from flask import Flask, render_template, redirect, url_for, request
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
    data = db.find({}).limit(3)
    return render_template("index.html", data=data)


@app.route('/create_post')
def create_post():

    return render_template("create_post.html")
@app.route('/create_post', methods=['POST'])
def insert_post():
    watch_brand = request.form.get("watch_brand")
    watch_model = request.form.get("watch_model")
    content = request.form.get("content")
    price = request.form.get("price")
    db.insert({
        'content': content,
        'watch_brand': watch_brand,
        'watch_model': watch_model,
        'price':price
    })
    return redirect(url_for('index'))


@app.route('/edit_post')
def edit_post():
    return render_template("edit_post.html")


@app.route('/edit_post', methods=['POST'])
def save_post():
    
    return redirect(url_for('index'))


@app.route('/confirm_delete_post')
def confirm_delete_post():
    return render_template("confirm_delete_post.html")


@app.route('/delete_post')
def delete_post():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
