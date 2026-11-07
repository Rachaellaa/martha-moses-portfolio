
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine
from app.models import ContactMessage

from app.routers.profile import router as profile_router
from app.routers.experience import router as experience_router
from app.routers.skills import router as skills_router
from app.routers.projects import router as projects_router
from app.routers.contact import router as contact_router


app = FastAPI(
    title="Martha Moses | Data Engineering Portfolio API",
    description="Backend API powering Martha Moses' professional portfolio.",
    version="1.0.0",
)


# Allow the React frontend to communicate with the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def create_database_tables():
    Base.metadata.create_all(bind=engine)


# Register API routers
app.include_router(profile_router)
app.include_router(experience_router)
app.include_router(skills_router)
app.include_router(projects_router)
app.include_router(contact_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Martha Moses' Portfolio API",
        "status": "online"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "Martha Moses Portfolio API"
    }
