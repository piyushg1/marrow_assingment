## Step 1: Clone the Repository

First, clone the project repository to your local machine:


git clone https://github.com/piyushg1/marrow_assingment
cd imdb-content-system

## Step 2: Set Up a Virtual Environment

python -m venv venv

Activate the virtual environment:

    On macOS/Linux:
    
    source venv/bin/activate

    On Windows:
    
    venv\Scripts\activate

## Step 3: Install Dependencies

Install the required Python packages using the requirements.txt file:


pip install -r requirements.txt

## Step 4: Set Up MongoDB

You can either use a local MongoDB instance or MongoDB Atlas (cloud-based).

    For MongoDB Atlas:

        Create a cluster and get the connection URI.

        Update the MONGO_URI in the .env file (see below).

    For Local MongoDB:

        Make sure MongoDB is running on localhost:27017.

## Step 5: Configure Environment Variables

Create a .env file in the project root and add the following:


MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
SECRET_KEY=your-secret-key
DEBUG=True

Replace <username>, <password>, and <dbname> with your MongoDB credentials.
Running the Application

Once everything is set up, you can start the Flask development server:


python app.py

Open your browser and go to:

http://localhost:5000/

You should see the IMDb Content Upload System frontend.
## API Endpoints
1. Upload CSV File

    Method: POST

    URL: /upload

    Request Body: Form-data with a CSV file.

    Response: Success or error message.

2. Get Movies

    Method: GET

    URL: /movies

    Query Parameters:

        page: Page number (default: 1).

        per_page: Number of movies per page (default: 10).

        release_year: Filter by release year.

        language: Filter by language.

        sort_by: Sort by release_date or vote_average (default: release_date).

        sort_order: Sort order (1 for ascending, -1 for descending).

    Response: List of movies in JSON format.
## Technologies Used

    - Backend: Python Flask

    - Database: MongoDB

    - Frontend: HTML, CSS, JavaScript

