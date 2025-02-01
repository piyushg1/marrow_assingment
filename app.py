from flask import Flask, render_template
from pymongo import MongoClient
from config import Config  # Import the Config class
from routes import routes_blueprint  # Import the Blueprint

app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(Config)

# MongoDB connection
try:
    client = MongoClient(app.config["MONGO_URI"])
    db = client[app.config["DATABASE_NAME"]]
    app.movies_collection = db[app.config["COLLECTION_NAME"]]  # Attach to app context
    print("Connected to MongoDB")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")

# Register the Blueprint
app.register_blueprint(routes_blueprint)


@app.route("/")
def home():
    return render_template("index.html")  # Serve the frontend


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
