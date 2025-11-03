from fastapi import APIrouter, HTTPException, status
from dao import UserDAO
from typing import List
from schemas import (
    UserSchema,
    UserCreateSchema,
    UpdateUserRoleSchema
)

router = APIrouter(
    prefix='/users',
    tags = ['User API']
)

@router.get('/all', summary='Список всех пользователей')
async def get_all_users() -> List[UserSchema]:
    return await UserDAO.find_all()


@router.get('/me', summary='Получить текущего пользователя')
async def me():
    pass


@router.post('/login', summary='Авторизация пользователя')
async def login():
    pass


@router.post('/create', summary='Создать пользователя')
async def create_user(data: UserCreateSchema) -> UserSchema:
    user = await UserDAO.create(**data)
    return user


@router.delete('/delete', summary='Удалить пользователя')
async def delete_user(user_id: int) -> UserSchema:
    user = await UserDAO.delete(id)
    return user


@router.post('/update_role', summary='Дать пользователю новую роль')
async def update_role(data: UpdateUserRoleSchema) -> dict:
    user = await UserDAO.get(user_id=data.user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Пользователь не найден')
    
    await UserDAO.update(user_id=data.user_id, user_role=data.role)