# Template fastapi server 
The structure of the fistfull api server project on fastapi.

---

## Project tree
The project consists of the following directories:

```bash
.
├── alembic
│   ├── versions
│   └── env.py
├── src
│   ├── api
│   │   ├── endpoints
│   │   │   ├── dependencies.py
│   │   │   ├── exceptions.py
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   └── utils.py
│   │   └── app.py
│   ├── core
│   │   └── config.py
│   ├── crud
│   │   └── crud.py
│   ├── db
│   │   ├── base.py
│   │   ├── config.py
│   │   └── pg_db.py
│   ├── models
│   │   └── models.py
│   ├── schemas
│   │   └── schemas.py
│   └── main.py
├── .env
├── alembic.ini
├── Dockerfile
├── requirements.txt
└── startserver.sh
```

In some directories there is an empty file `__init__.py` that is needed to recognize directories as packages.

1. Store all domain directories inside __`src`__ folder:
- `src/` ── highest level of an app, contains common models, configs, and constants, etc;
- `src/main.py` ── root of the project, which inits the FastAPI app.

2. Folder __`src/api`__ connects all restfull api logic:
- `api/api.py` ── main file with union all endpoints [`APIRouter()`](https://fastapi.tiangolo.com/tutorial/bigger-applications/#:~:text=app.internal.admin-,APIRouter,-%C2%B6).

3. Folder __`src/api/endpoints/`__ consists all the endpoints and methods for the restfull api:
- `dependencies.py` ── router dependencies;
- `router.py` ── module with all the restfull api methods;
- `service.py` ── module specific business logic.
- `utils.py` ── non-business logic functions, e.g. response normalization, data enrichment, etc.
- `exceptions.py` ── module specific exceptions, e.g. PostNotFound, InvalidUserData.

4. Folder __`src/core/`__ meta information for Swagger spec;

5. Folder __`src/crud/`__ all manipulation with db;

6. Folder __`src/db/`__ meta information/connectors to db;

7. Folder __`src/models/`__ ── for db models;

8. Folder __`src/schemas/`__ ── for pydantic models;


## Configurate DB connection

## DB migration with Alembic