@echo off
echo ========================================================
echo Starting BioScan AI (Backend + Frontend)
echo ========================================================

echo Starting FastAPI Backend on http://127.0.0.1:8000 ...
start "BioScan AI Backend" cmd /k "cd backend && python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload"

timeout /t 2 /nobreak >nul

echo Starting React + Vite Frontend on http://localhost:5173 ...
start "BioScan AI Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo Both servers are launching!
echo Open your browser to: http://localhost:5173
echo ========================================================
