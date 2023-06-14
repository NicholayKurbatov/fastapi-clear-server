# Import all the models, so that Base has them before being
# imported by Alembic
from .pg_db import Base  # noqa
from server.models import * # noqa