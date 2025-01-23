from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any
from data_storage import users

# class CheckUserMiddleware(BaseMiddleware):
#     async def __call__(
#             self,
#             handler: Callable[[Message, Dict[str, Any]], Any],
#             event: Message,
#             data: Dict[str, Any]
#     ) -> Any:
#         user_id = event.from_user.id
#
#         if user_id not in users:
#             users[user_id] = {
#                 "user_id": user_id,
#                 "weight": None,
#                 "height": None,
#                 "age": None,
#                 "activity": None,
#                 "city": None,
#             }
#
#         return await handler(event, data)