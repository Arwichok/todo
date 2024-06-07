from uuid import UUID
from litestar import Controller, get
from litestar.di import Provide
from litestar.response import Template

from app.domain.todos import TodoRepository, TodoService


class WebTodoController(Controller):
    path = "/todos"
    dependencies = dict(
        repo=Provide(TodoRepository.provide),
        service=Provide(TodoService.provide),
    )

    @get("/")
    async def get_todos(self, repo: TodoRepository) -> Template:
        return Template("todos.html.j2", context=dict(todos=await repo.list()))

    @get("/{id:uuid}")
    async def get_todo(self, id: UUID, repo: TodoRepository) -> Template:
        return Template("todo.html.j2", context=dict(todo=await repo.get(id)))
