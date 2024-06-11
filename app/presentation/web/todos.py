from typing import Annotated, TypeVar
from uuid import UUID
from litestar import Controller, delete, get, patch, post
from litestar.di import Provide
from litestar.response import Template
from litestar.contrib.htmx.request import HTMXRequest
from litestar.contrib.htmx.response import HTMXTemplate
from litestar.params import Body
from litestar.enums import RequestEncodingType
from litestar import status_codes
from app.domain.todos import TodoRepository, TodoService
from app.infrastructure.database.tables import Todo

T = TypeVar("T")
Encoded = Annotated[T, Body(media_type=RequestEncodingType.URL_ENCODED)]
EncodedDict = Encoded[dict]


class WebTodoController(Controller):
    path = "/todos"
    dependencies = dict(
        repo=Provide(TodoRepository.provide),
        service=Provide(TodoService.provide),
    )

    @get("/")
    async def get_todos(
        self,
        request: HTMXRequest,
        repo: TodoRepository
    ) -> Template:
        return Template("todos.html.j2", context=dict(todos=await repo.list()))

    @delete("/{id:uuid}", status_code=status_codes.HTTP_202_ACCEPTED)
    async def delete_todo(self, id: UUID, service: TodoService) -> str:
        await service.delete(id)
        return ""

    @post("/")
    async def create_todo(
        self,
        request: HTMXRequest,
        service: TodoService,
        data: EncodedDict,
    ) -> Template:
        if name := data.get("name"):
            todo = Todo(
                name=name,
                done='done' in data
            )
            return HTMXTemplate(
                template_str="{% include 'todo.html.j2' %}", 
                context=dict(todo=await service.create(todo))
            )
        return ""
    
    @patch("/{id:uuid}")
    async def update_todo(
        self,
        id: UUID,
        data: EncodedDict,
        service: TodoService,
    ) -> Template:
        if name := data.get("name"):
            todo = dict(
                name=name,
            )
        else:
            todo = dict(
                done='done' in data
            )
        print(todo)
        return HTMXTemplate(
            template_name="todo.html.j2",
            context=dict(todo=await service.update(todo, id)),
        )
