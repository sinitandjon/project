#!/bin/bash

# Navigate to the backend directory and run FastAPI in the background
cd backend
echo "Starting FastAPI backend..."
uvicorn app:app --reload &
BACKEND_PID=$!  # Capture the backend process ID
cd ..

# Navigate to the frontend directory and run the simple HTTP server in the background
cd frontend
echo "Starting frontend HTTP server on port 8003..."
python3 -m http.server 8003 &
FRONTEND_PID=$!  # Capture the frontend process ID
cd ..

# Open the browser automatically
if command -v xdg-open &> /dev/null; then
    xdg-open "http://localhost:8003"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    open "http://localhost:8003"
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    start "http://localhost:8003"
else
    echo "Please open http://localhost:8003 manually in your browser."
fi

# Wait for user input to stop the servers
echo "Press [Ctrl+C] to stop the servers."

# Wait to keep the script running and handle cleanup on exit
trap "echo 'Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID; exit" SIGINT
wait
