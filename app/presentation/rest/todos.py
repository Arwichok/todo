from litestar import Controller, get



class TodoController(Controller):
    path = "/todos"


    @get("/")
    async def todos(self) -> list:

        return []
