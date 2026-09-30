from pydantic import BaseModel, ConfigDict


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
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]
