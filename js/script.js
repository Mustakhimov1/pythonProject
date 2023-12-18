const apiUrl = "https://api.nytimes.com/svc/topstories/v2/home.json?api-key=cAzgZfj16AqOdXcmXA5RQyk8kyfRyaAA";

fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        const newsList = document.getElementById('newsList');
        let isFirstItem = true;

        data.results.forEach(article => {
            const newsItem = document.createElement('div');
            newsItem.classList.add('carousel-item');
            if (isFirstItem) {
                newsItem.classList.add('active');
                isFirstItem = false;
            }

            newsItem.innerHTML = `
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">${article.title}</h5>
                            <p class="card-text">${article.abstract}</p>
                            <p class="card-text"><small class="text-muted">${article.published_date}</small></p>
                        </div>
                    </div>
                `;

            newsList.appendChild(newsItem);
        });
    })
    .catch(error => console.error('Error fetching news:', error));

function requestNewsBySection() {
    const sectionInput = document.getElementById('sectionInput');
    const section = sectionInput.value.trim();

    if (section !== "") {
        const sectionApiUrl = `https://api.nytimes.com/svc/topstories/v2/${section}.json?api-key=cAzgZfj16AqOdXcmXA5RQyk8kyfRyaAA`;

        fetch(sectionApiUrl)
            .then(response => response.json())
            .then(data => {
                const newsList = document.getElementById('newsList');
                newsList.innerHTML = "";

                let isFirstItem = true;

                data.results.forEach(article => {
                    const newsItem = document.createElement('div');
                    newsItem.classList.add('carousel-item');
                    if (isFirstItem) {
                        newsItem.classList.add('active');
                        isFirstItem = false;
                    }

                    newsItem.innerHTML = `
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title">${article.title}</h5>
                                    <p class="card-text">${article.abstract}</p>
                                    <p class="card-text"><small class="text-muted">${article.published_date}</small></p>
                                </div>
                            </div>
                        `;

                    newsList.appendChild(newsItem);
                });
            })
            .catch(error => console.error('Error fetching news by section:', error));
    } else {
        alert('Please enter a section.');
    }
}