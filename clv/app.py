from clv.api.fast import app
import uvicorn

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("clv.api.fast:app", host="localhost", port=8000)