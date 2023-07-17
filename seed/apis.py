from ninja import NinjaAPI

from calenders.apis import router as calender_router
from users.apis import router as user_router

api = NinjaAPI()
api.add_router('/calenders', calender_router)
api.add_router('/users', user_router)
