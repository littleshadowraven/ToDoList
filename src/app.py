from fastapi import FastAPI
from src.api import include_router

app = FastAPI(title="Fast API - todo list")
include_router(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# GET /lists
# POST /lists
# DELETE /lists/{list_id}

# GET /lists/{list_id}/todos
# POST /lists/{list_id}/todos
# PATCH /lists/{list_id}/todos/{todo_id}
# DELETE /lists/{list_id}/todos/{todo_id}