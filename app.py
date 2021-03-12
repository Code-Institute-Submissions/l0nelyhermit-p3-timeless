from flask import Flask, render_template, redirect, url_for, request
import os
import pymongo
from dotenv import load_dotenv
from bson.objectid import ObjectId


load_dotenv()

app = Flask(__name__)

# SET UP MONGO CONNECTION
MONGO_URI = os.environ.get('MONGO_URI')
DATABASE = 'Watches'
COLLECTION = 'listing'
# Connection to MONGODB
connect = pymongo.MongoClient(MONGO_URI)
db = connect[DATABASE][COLLECTION]

# cloudinary setup
CLOUD_NAME = os.environ.get('CLOUD_NAME')
UPLOAD_PRESET = os.environ.get('UPLOAD_PRESET')


@app.route('/')
def index():
    data = db.find({})
    return render_template("index.html", data=data)


@app.route('/show_post')
def show_post():
    data = db.find({})
    return render_template("show_post.html", data=data)


@app.route('/create_post')
def create_post():
    return render_template("create_post.html",
                           cloud_name=CLOUD_NAME, upload_preset=UPLOAD_PRESET)


@app.route('/create_post', methods=['POST'])
def insert_post():
    watch_brand = request.form.get("watch_brand")
    watch_model = request.form.get("watch_model")
    content = request.form.get("content")
    price = request.form.get("price")
    uploadURL = request.form.get('uploaded-file-url')
    assetID = request.form.get('asset-id')

    # save to database
    db.insert({
        'watch_brand': watch_brand,
        'watch_model': watch_model,
        'content': content,
        'price': price,
        'uploadURL': uploadURL,
        'assetID': assetID
    })
    return redirect(url_for('show_post'))


@app.route('/edit_post/<item_id>')
def edit_post(item_id):
    watch = db.find_one({
        "_id": ObjectId(item_id)
    })
    return render_template("edit_post.html", watch=watch,
                           cloud_name=CLOUD_NAME, upload_preset=UPLOAD_PRESET)


@app.route('/edit_post/<item_id>', methods=['POST'])
def save_post(item_id):
    # Load in data from form
    watch_brand = request.form.get("watch_brand")
    watch_model = request.form.get("watch_model")
    content = request.form.get("content")
    price = request.form.get("price")
    uploadURL = request.form.get('uploaded-file-url')
    assetID = request.form.get('asset-id')

    # update Mongo database
    db.update({
        "_id": ObjectId(item_id)
    }, {
        '$set': {
            'watch_brand': watch_brand,
            'watch_model': watch_model,
            'content': content,
            'price': price,
            'uploadURL': uploadURL,
            'assetID': assetID
        }
    })
    return redirect(url_for('show_post'))


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
