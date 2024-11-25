// Base URL of the backend
const BASE_URL = "http://127.0.0.1:8000/search/";

// Function to perform a search query

async function performSearch() {
    // Get the user's search query from the input field
    const query = document.getElementById("searchInput").value;

    // Display a loading indicator
    const resultsContainer = document.getElementById("results");
    resultsContainer.innerHTML = "<p>Loading...</p>";

    try {
        // Make an API request to the backend
        const response = await fetch(`${BASE_URL}?query=${encodeURIComponent(query)}`, {
            method: "GET", // Specify GET method
            headers: {
                "Content-Type": "application/json",
            },
        });
        const data =  await response.json();
        console.log("Search Results:", data); // Log for debugging

        const resultsContainer = document.getElementById("results");
        //console.log('result',resultsContainer)
        // Clear the loading indicator
        resultsContainer.innerHTML = "";

        // Check if results are available
        if (data.results) {
            // Render the results
            Object.values(data.results).forEach((article) => {
                const resultElement = document.createElement("div");
                resultElement.classList.add("result");
                const title = document.createElement("h3");
                title.innerText = article.title;
                title.style.width='60%' 
                resultElement.appendChild(title);

                const img = document.createElement("img");
                img.src = article.image_url;
                img.alt = article.title;
                img.style.width = "60%"; 
                img.style.length='50px' // Adjust image size as needed
                resultElement.appendChild(img);

             
                

                // Create and append resume (combine all paragraphs in the array)
                const resume = document.createElement("p");
                resume.innerText = "RESUME:  "+article.resume.join(" ");
                resume.style.width='60%'  // Join array elements into a single string
                resultElement.appendChild(resume);

                // Append the result element to the results container
                resultsContainer.appendChild(resultElement);
                const link = document.createElement("a");
                link.href = article.link;
                link.target = "_blank";
                link.innerText = 'origine link';
                link.style.width='60%'
                resultElement.appendChild(link);
            });
        } else {
            // No results found
            resultsContainer.innerHTML = "<p>No results found.</p>";
        }
    } catch (error) {
        // Handle errors
        console.error("Error fetching search results:", error);
        resultsContainer.innerHTML = "<p>Error fetching search results. Please try again later.</p>";
    }
}

// Attach event listener to the search button
document.getElementById("searchButton").addEventListener("click", performSearch);

// Allow pressing "Enter" in the input field to trigger the search
document.getElementById("searchInput").addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        performSearch();
    }
});
