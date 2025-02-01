from flask import Blueprint, request, jsonify, current_app
from bson import ObjectId
import csv

# Create a Blueprint
routes_blueprint = Blueprint("routes", __name__)


@routes_blueprint.route("/upload", methods=["POST"])
def upload_csv():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith(".csv"):
        # Read the CSV file
        csv_data = csv.DictReader(file.read().decode("utf-8").splitlines())
        movies = []
        for row in csv_data:
            movies.append(row)

        if movies:
            current_app.movies_collection.insert_many(movies)
            return jsonify({"message": "File uploaded successfully"}), 200
        else:
            return jsonify({"error": "No data found in CSV"}), 400
    else:
        return jsonify({"error": "Invalid file type"}), 400


@routes_blueprint.route("/movies", methods=["GET"])
def get_movies():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))

    # Filtering
    filters = {}
    release_year = request.args.get("release_year")
    language = request.args.get("language")
    if release_year:
        filters["release_date"] = {"$regex": f"{release_year}"}
    if language:
        filters["original_language"] = language

    # Sorting
    sort_by = request.args.get("sort_by", "release_date")
    sort_order = int(request.args.get("sort_order", 1))

    movies = (
        current_app.movies_collection.find(filters)
        .sort(sort_by, sort_order)
        .skip((page - 1) * per_page)
        .limit(per_page)
    )
    movie_list = list(movies)

    for movie in movie_list:
        movie["_id"] = str(movie["_id"])

    return jsonify(movie_list), 200
