from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from ..database import Base
from ..main import app
from fastapi.testclient import TestClient
import pytest
from ..models import Todos, Users
from ..routers.auth import bcrypt_context

SQLITE_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(
    SQLITE_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {"username": "admin", 'id': 1, 'user_role': 'admin'}


client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todos(title="Test Todo",
                description="Test Description", 
                priority=1, 
                complete=False, 
                owner_id=1
            )   
    db = TestSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()

@pytest.fixture
def test_user():
    user = Users(
        username = "testuser",
        email = "test@gmail.com",
        first_name = "Test",
        last_name = "User",
        hashed_password = bcrypt_context.hash("123456"),
        role = "user",
        phone_number = "1234567890",
    )
    db = TestSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()