from litestar import Controller, get, post, patch
from litestar.di import Provide
from app.infrastructure.database.tables import Todo
from app.domain.todos import (
    UpdateTodo,
    CreateTodo,
    TodoRepository,
    TodoService,
)
from uuid import UUID

class TodoController(Controller):
    path = "/todos"
    dependencies = dict(
        repo=Provide(TodoRepository.provide),
        service=Provide(TodoService.provide),
    )

    @get("/")
    async def get_todos(self, repo: TodoRepository) -> list[Todo]:
        return await repo.list()

    @post("/", dto=CreateTodo)
    async def create_todo(self, data: Todo, repo: TodoRepository) -> Todo:
        return await repo.add(data)

    @patch("/{id:uuid}")
    async def update_todo(
        self,
        id: UUID,
        data: Todo,
        service: TodoService,
    ) -> Todo:
        return await service.update(data, id)

    @patch("/", dto=UpdateTodo)
    async def update_todo_(
        self,
        data: Todo,
        repo: TodoRepository,
    ) -> Todo:
        return await repo.update(data)
