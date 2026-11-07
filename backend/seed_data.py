from app.core.database import SessionLocal
from app.models import Profile, Experience, Project, Skill

from app.routers.profile import get_profile
from app.routers.experience import get_experience
from app.routers.projects import get_projects
from app.routers.skills import get_skills


def seed_database():
    db = SessionLocal()

    try:
        # PROFILE
        if db.query(Profile).count() == 0:
            profile = get_profile()
            db.add(Profile(**profile.dict()))
            print("Profile imported.")

        # PROJECTS
        if db.query(Project).count() == 0:
            projects = get_projects()

            for project in projects:
                db.add(Project(**project.dict()))

            print(f"{len(projects)} projects imported.")

        # EXPERIENCE
        if db.query(Experience).count() == 0:
            experiences = get_experience()

            for experience in experiences:
                db.add(Experience(**experience.dict()))

            print(f"{len(experiences)} experiences imported.")

        # SKILLS
        if db.query(Skill).count() == 0:
            skills = get_skills()

            for skill in skills:
                db.add(Skill(**skill.dict()))

            print(f"{len(skills)} skill categories imported.")

        db.commit()

        print("\nDATABASE MIGRATION COMPLETED SUCCESSFULLY!")

    except Exception as error:
        db.rollback()
        print("Migration failed:", error)
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()