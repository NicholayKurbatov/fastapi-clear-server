# Template fastapi server 
The structure of the fistful api server project on fastapi.

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
│   │   │   └── endpoit1
│   │   │       ├── dependencies.py
│   │   │       ├── exceptions.py
│   │   │       ├── models.py
│   │   │       ├── router.py
│   │   │       ├── schemas.py
│   │   │       ├── service.py
│   │   │       └── utils.py
│   │   └── app.py
│   ├── core
│   │   └── config.py
│   ├── db
│   │   ├── base.py
│   │   ├── config.py
│   │   └── pg_db.py
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

3. Folder __`src/api/endpoints/.../`__ :
- `dependencies.py` ── router dependencies;
- `models.py` ── for db models;
- `router.py` ── module with all the restfull api methods;
- `schemas.py` ── for pydantic models;
- `service.py` ── module specific business logic.
- `utils.py` ── non-business logic functions, e.g. response normalization, data enrichment, etc.
- `exceptions.py` ── module specific exceptions, e.g. PostNotFound, InvalidUserData.

4. Folder __`src/api/core/`__ :
- `config.py` ── .

5. Folder __`src/api/db/`__ :
- `base.py` ── ;
- `config.py` ── ;
- `pg_db.py` ── .

## Configurate DB connection

## DB migration with Alembic