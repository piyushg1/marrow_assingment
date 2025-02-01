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

