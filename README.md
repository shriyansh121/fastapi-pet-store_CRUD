# 🐾 Pet Store Management API

![Project Structure](image.png)

This project is a professional FastAPI application designed to manage a pet store with a MySQL database backend. Below is a detailed breakdown of the project structure and the purpose of each file.

---

## 📦 Why `__init__.py`?

`__init__.py` tells Python that a folder is a **package**, allowing files inside it to be imported using dot notation (e.g., `app.models.pet`).
- **Module Discovery:** Enables Python to find and link modules correctly.
- **Relative Imports:** Simplifies the way files interact within the project.
- **Clean Structure:** Essential for larger applications to prevent import failures.

---

## 📝 1. `logging.py`
*The first file created for the project.*

We initialize logging at the very beginning so it can be used across the entire project with a single configuration. **Logging is extremely helpful** because:
- It provides a clear understanding of the project's flow.
- It is essential for **troubleshooting and debugging** during development.

---

## 🗄️ 2. `database_connection.py`
*The core of our data persistence.*

This file is responsible for connecting to the database and initializing the connection. It also includes connection tests to ensure the pipeline executes smoothly.

> **Note:** `create_engine()` is highly flexible and can connect to **ANY** database with a compatible SQLAlchemy driver.

| Database | Connection URL Template |
| :--- | :--- |
| **MySQL** | `mysql+pymysql://user:password@localhost:3306/db_name` |
| **PostgreSQL** | `postgresql+psycopg2://user:password@localhost:5432/db_name` |
| **SQLite** | `sqlite:///test.db` |
| **Oracle** | `oracle+cx_oracle://user:password@host:port/service_name` |
| **MS SQL** | `mssql+pyodbc://user:password@dsn_name` |

---

## 🦢 3. `Models/pet.py`
*Object Relational Mapping (ORM).*

The Pet model defines how data is represented in the database. It enforces constraints and maps Python objects to database rows.

### 🔄 Data Flow Pipeline
```text
   Client JSON Request
          ↓
   Pydantic (Type & Rule Validation)
          ↓
   ORM Model (Insert / Query)
          ↓
   Database (Constraints Enforced)
          ↓
   ORM Object (Result)
          ↓
   Pydantic (Response Shaping)
          ↓
   Client JSON Response
```

---

## 📜 4. `Schemas/pet_pydantic.py`
*Data validation and serialization.*

- **`PetBase`**: The common schema defining core fields (name, species, age, price, availability). It ensures a shared structure across the app.
- **`PetCreate`**: Inherits from `PetBase`. It exists for future extensibility and clearly marks schema intent for creation requests.
- **`PetUpdate`**: Defines all fields as **Optional**, allowing for "partial updates" (Patch) where the client only sends changed data.
- **`PetInDB`**: Extends `PetBase` with database-generated fields like `id` and `created_at`. It uses `from_attributes=True` so Pydantic can serialize SQLAlchemy ORM objects into API responses.

---

## 🛠️ 5. `Crud/crud_pet.py`
*Business Logic.*

This file handles all **CRUD (Create, Read, Update, Delete)** operations. It acts as the bridge between our API endpoints and the database models.

---

## 🚀 6. `api/pets_endpoints.py`
*The API Layer.*

This file defines all the web endpoints. It receives requests, interacts with the CRUD layer, and returns the appropriate responses to the client.

---

## 🏁 7. `main.py`
*The Application Entry Point.*

This is the heart of the FastAPI application. It initializes the app, includes the routers for our endpoints, and prepares the environment for the server to run.

---

![API](image-1.png)