The project is a search engine designed to extract and index relevant content from the public websites **public.fr** and **vsd.fr**, leveraging cutting-edge machine learning techniques. First, a web scraping process gathers articles and textual data from these websites. The scraped content is then processed using the pre-trained **SentenceTransformer('all-MiniLM-L6-v2')** model, which converts the text into high-dimensional embeddings—numerical vectors representing the semantic meaning of the content. These embeddings are stored in a vector database powered by **FAISS (Facebook AI Similarity Search)**, optimized for fast and efficient similarity searches. When a user submits a search query, the system uses the same SentenceTransformer model to generate an embedding for the query and performs a similarity search in FAISS to find the top five nearest neighbors—articles or content pieces most semantically similar to the query. The system then returns these results to the user, offering an accurate and responsive search experience tailored to the data from the target websites.

Requirements:

    Python 3.x (https://www.python.org/downloads/)
    faiss ("pip install faiss-cpu)
    sentence_transformers(pip install sentence_transformers)
    uvicorn (pip install uvicorn)

    FastAPI (Backend API) (pip install FastAPI)
    requests (Web requests) (pip install requests)
    beautifulsoup4 (HTML parsing) (pip install beautifulsoup4)
    

Setup:

    Clone the repository.
    Install Python dependencies:


Running the Project:

    Place the run.sh (Linux/macOS) or run.bat (Windows) file in the root directory.

    Run the run.sh (Linux/macOS):

    you can use this('bash run.sh')

    Run the run.bat (Windows):
        Double-click the run.bat file.

What Happens:

    Backend: FastAPI runs on http://127.0.0.1:8000.
    Frontend: Opens in the browser at http://localhost:8001.

Usage:

    Enter a query in the search box to retrieve relevant articles.

    exemple: 'olivier giroud', 'news',
