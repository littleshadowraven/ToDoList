from fastapi import FastAPI

app = FastAPI(title="Fast API - todo list")

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8000)


# GET /lists
# POST /lists
