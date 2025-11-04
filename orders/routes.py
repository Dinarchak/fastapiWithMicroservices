from fastapi import APIRouter
from dao import OrderDAO
from typing import List
from schemas import OrderSchema, CreateOrderSchema

router = APIRouter(prefix='/orders')


@router.get('/all', summary='Получить все заказы')
async def get_all_orders() -> List[OrderSchema]:
    return await OrderDAO.get_all_orders()


@router.post('/create' summary='Создать заказ')
async def create_order(data: CreateOrderSchema) -> dict:
    order = await OrderDAO.create_order(**data)
    return {'message': f'Заказ {order} оформлен'}

@router.get('/{id}', summaru='Получить заказ по id')
async def get_order(id: int) -> OrderSchema:
    return await OrderDAO.get_order(id)
