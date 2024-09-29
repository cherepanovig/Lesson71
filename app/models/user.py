from fastapi import APIRouter
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates="user")

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))


# Создаем роутер с префиксом '/user' и тегом 'user'
router = APIRouter(prefix='/user', tags=['user'])

# Маршрут для получения всех пользователей
@router.get('/')
async def all_users():
    pass

# Маршрут для получения пользователя по ID
@router.get('/{user_id}')
async def user_by_id(user_id: int):
    pass

# Маршрут для создания нового пользователя
@router.post('/create')
async def create_user():
    pass

# Маршрут для обновления пользователя
@router.put('/update')
async def update_user():
    pass

# Маршрут для удаления пользователя
@router.delete('/delete')
async def delete_user():
    pass