let currentPage = 1;

// Handle CSV file upload
document.getElementById('uploadForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const fileInput = document.getElementById('csvFile');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('uploadMessage').textContent = data.message || data.error;
            if (!data.error) {
                fetchMovies();
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

function fetchMovies() {
    const releaseYear = document.getElementById('releaseYear').value;
    const language = document.getElementById('language').value;
    const sortBy = document.getElementById('sortBy').value;
    const sortOrder = document.getElementById('sortOrder').value;

    fetch(`/movies?page=${currentPage}&per_page=10&release_year=${releaseYear}&language=${language}&sort_by=${sortBy}&sort_order=${sortOrder}`)
        .then(response => response.json())
        .then(data => {
            const tbody = document.querySelector('#movieTable tbody');
            tbody.innerHTML = '';

            data.forEach(movie => {
                const row = document.createElement('tr');
                row.innerHTML = `
                <td>${movie.title}</td>
                <td>${movie.release_date}</td>
                <td>${movie.original_language}</td>
                <td>${movie.vote_average}</td>
            `;
                tbody.appendChild(row);
            });

            document.getElementById('pageNumber').textContent = `Page ${currentPage}`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function nextPage() {
    currentPage++;
    fetchMovies();
}

function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        fetchMovies();
    }
}

fetchMovies();