from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Define a sample endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to your FastAPI application!"}

# Run the FastAPI application with uvicorn server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)