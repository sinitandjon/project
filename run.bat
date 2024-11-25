@echo off

:: Run FastAPI (backend) in a new terminal window
start cmd /k "uvicorn app:app --reload"

:: Serve the frontend using Python's HTTP server
start cmd /k "python -m http.server 8001"

:: Open the browser automatically
start http://localhost:8001
