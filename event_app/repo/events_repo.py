from event_app.db.models import Event, Location, Category
from event_app.repo.base_repo import Repository


class EventRepository(Repository):
    model = Event


class LocationRepository(Repository):
    model = Location


class CategoryRepository(Repository):
    model = Category
