import uvicorn
from fastapi import FastAPI

from event_app.api.endpoints.events import events_router
from event_app.api.endpoints.locations import locations_router
from event_app.api.endpoints.categories import categories_router

app = FastAPI()

app.include_router(events_router)
app.include_router(locations_router)
app.include_router(categories_router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
