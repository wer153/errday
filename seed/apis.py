from ninja import NinjaAPI

from calenders.apis import router

api = NinjaAPI()
api.add_router('/calenders', router)
