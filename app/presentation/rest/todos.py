from litestar import Controller, get
from app.infrastructure.database.tables import Todo
from app.domain.todos import Todo, TodoDTO
from uuid import uuid4

TODOS = [
    Todo(name="Todo 1", done=True),
    Todo(id=uuid4(), name="Todo 2", done=False),
    Todo(id=uuid4(), name="Todo 3", done=True),
]

class TodoController(Controller):
    path = "/todos"
    dto = TodoDTO

    @get("/")
    async def get_todos(self) -> list[Todo]:
        return TODOS
