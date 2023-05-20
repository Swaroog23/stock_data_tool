from urls import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run("urls:app", host="localhost", port=8000, reload=True)