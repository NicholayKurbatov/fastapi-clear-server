from dotenv import load_dotenv
import os

load_dotenv()

PG_USER = os.environ.get("PG_USER")
PG_PSWD = os.environ.get("PG_PSWD")
PG_HOST = os.environ.get("PG_HOST")
PG_DB = os.environ.get("PG_DB")
PG_SSL = os.environ.get("PG_SSL")