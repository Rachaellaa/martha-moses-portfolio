
from fastapi import APIRouter

from app.schemas.experience import ExperienceResponse


router = APIRouter(
    prefix="/api/experience",
    tags=["Experience"],
)


@router.get("/", response_model=list[ExperienceResponse])
def get_experience():

    return [

        ExperienceResponse(
            job_title="Data Analyst / Systems and Reporting Analyst",
            company="Centre for Food Technology and Research (BSU)",
            employment_type="Full-time",
            location="Benue, Nigeria",
            start_date="2024-05",
            end_date="2026-05",
            is_current=False,
            responsibilities=[
                "Collected, cleaned and structured research datasets across multiple operational workflows.",
                "Improved data accuracy and downstream reporting reliability by 30%.",
                "Developed structured reporting frameworks and automated reporting workflows.",
                "Implemented data validation and quality control processes.",
                "Analysed operational datasets to identify trends and process inefficiencies.",
                "Produced analytical reports and actionable insights for stakeholders."
            ],
            technologies=[
                "Python",
                "SQL",
                "Microsoft Excel",
                "Power BI",
                "PostgreSQL"
            ],
        ),

        ExperienceResponse(
            job_title="Data and Operations Analyst | NYSC",
            company="HQ 82 Division, Nigerian Army Ordnance Corps",
            employment_type="National Youth Service Corps",
            location="Enugu, Nigeria",
            start_date="2023-04",
            end_date="2024-04",
            is_current=False,
            responsibilities=[
                "Designed digital tracking dashboards that improved operational reporting accuracy and visibility by 18%.",
                "Collected and analysed logistics and inventory datasets.",
                "Converted manual records into structured digital datasets.",
                "Improved data consistency through standardised documentation and data entry processes.",
                "Produced performance reports supporting resource allocation and operational planning.",
                "Trained over 50 personnel on data entry standards and reporting tools."
            ],
            technologies=[
                "Microsoft Excel",
                "Power BI",
                "Data Analysis",
                "Dashboard Development",
                "Reporting Automation"
            ],
        )

    ]
