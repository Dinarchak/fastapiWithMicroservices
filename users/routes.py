from fastapi import APIRouter, HTTPException, status, Response, Depends
from auth import authenticate_user, create_access_token, get_current_user, get_password_hash
from dao import RoleDAO, UserDAO
from typing import List
from schemas import (
    UserLoginSchema,
    UserSchema,
    UserCreateSchema
)
from models import User

router = APIRouter(
    prefix='/users',
    tags = ['User API']
)

@router.get('/all', summary='Список всех пользователей')
async def get_all_users() -> List[UserSchema]:
    return await UserDAO.get_all_users()


@router.get('/me', summary='Получить текущего пользователя')
async def me(user: User = Depends(get_current_user)) -> UserSchema:
    return user


@router.post('/login', summary='Авторизация пользователя')
async def login(response: Response, data: UserLoginSchema):
    user = await authenticate_user(data.username, data.password)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Неверная почта или пароль')
    
    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}


@router.post('/create', summary='Создать пользователя')
async def create_user(data: UserCreateSchema) -> UserSchema:

    default_role = await RoleDAO.get_role('user')
    data_dict = data.model_dump()
    data_dict.update({'role_id': default_role.id, 'password': get_password_hash(data.password)})

    user = await UserDAO.create_user(**data_dict)

    print(user)

    return user


@router.delete('/delete', summary='Удалить пользователя')
async def delete_user(user_id: int) -> dict:
    user = await UserDAO.delete_user(id=user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Пользователь не найлен')
    return {'message': 'Пользователь удален'}


# @router.post('/update_role', summary='Дать пользователю новую роль')
# async def update_role(data: UpdateUserRoleSchema) -> dict:
#     user = await UserDAO.get_by_id_or_none(user_id=data.user_id)
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Пользователь не найден')
    
#     await UserDAO.update(user_id=data.user_id, user_role=data.role)