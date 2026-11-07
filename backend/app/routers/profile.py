from fastapi import APIRouter

from app.schemas.profile import ProfileResponse


router = APIRouter(
    prefix="/api/profile",
    tags=["Profile"]
)


@router.get("/", response_model=ProfileResponse)
def get_profile():

    return ProfileResponse(
        full_name="Martha Rachael Moses",

        professional_title="Data Engineer | Analytics Engineer | Data Analyst",

        short_bio=(
            "Data Engineer specialising in building scalable data pipelines, "
            "designing data warehouses, implementing ETL/ELT workflows, and "
            "developing cloud-based data solutions. Experienced in SQL, Python, "
            "Microsoft Azure, Microsoft Fabric, and modern data platforms, with "
            "additional expertise in data analytics, business intelligence, "
            "and transforming complex datasets into actionable business insights."
        ),

        location="Lagos, Nigeria",

        email="martharachaelmoses@gmail.com",

        linkedin_url="https://www.linkedin.com/in/martha-rachael-moses-7106253a4/",

        github_url="https://github.com/Rachaellaa",

        portfolio_url=None
    )