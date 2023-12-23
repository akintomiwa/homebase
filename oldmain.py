from fastapi import FastAPI
from models import Todo

app = FastAPI()



@app.get("/")
async def root():
    return {"message":"Hello World"}

todos = []

# Get all todos 
@app.get("/todos")
async def get_todos():
    return {"todos":todos}

# Get a single todo 
@app.get("/todos/{todo_id}")
async def get_single_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No todos found"}


# Create a todo 
@app.post("/todos")
async def create_todo(todo: Todo):
    todos.append(todo)
    return {"message":"Todo added"}

# Update a todo
@app.put("/todos/{todo_id}")
async def update_single_todo(todo_id: int, todo_obj:Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"message": "Todo {todo_id} updated"}
    return {"message": "No todos found to update."}
 

# Delete a To do 
# Get a single todo 
@app.delete("/todos/{todo_id}")
async def delete_single_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted"}
    return {"message": "No todos found"}