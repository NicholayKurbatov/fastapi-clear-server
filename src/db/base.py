# Import all the models, so that Base has them before being
# imported by Alembic
from .pg_db import Base  # noqa
from src.models.models import test_model # noqa