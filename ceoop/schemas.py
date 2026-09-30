from pydantic import BaseModel


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    name: str
    username: str
    password: str


class UserPublic(BaseModel):
    id: int
    name: str
    username: str


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
