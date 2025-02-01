from flask import Flask, render_template
from pymongo import MongoClient
from config import Config
from routes import routes_blueprint

app = Flask(__name__)


app.config.from_object(Config)

# MongoDB connection
try:
    client = MongoClient(app.config["MONGO_URI"])
    db = client[app.config["DATABASE_NAME"]]
    app.movies_collection = db[app.config["COLLECTION_NAME"]]
    print("Connected to MongoDB")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")


app.register_blueprint(routes_blueprint)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
