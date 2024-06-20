from litestar import Controller, get, post
from litestar.di import Provide

from app.domain.user import UserRepository, UserService, User, CreateUser, UpdateUser



class UserController(Controller):
    path = "/users"
    dependencies = dict(
        service=Provide(UserService.provide),
        repo=Provide(UserRepository.provide),
    )

    @get("/")
    async def get_users(self, service: UserService) -> list[User]:
        return await service.list()
    
    @post("/", dto=CreateUser)
    async def create_user(self, data: User, service: UserService, repo: UserRepository) -> User:
        return await repo.add(data)
        # return data
