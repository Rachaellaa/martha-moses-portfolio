from fastapi import APIRouter
from app.schemas.skills import SkillCategoryResponse

router = APIRouter(prefix="/api/skills", tags=["Skills"])


@router.get("/", response_model=list[SkillCategoryResponse])
def get_skills():

    return [
        SkillCategoryResponse(
            category="Data Engineering",
            skills=[
                "ETL and ELT Pipelines",
                "Data Warehousing",
                "Data Modelling",
                "Data Integration",
                "Data Orchestration",
                "Batch Processing",
                "Data Quality and Validation",
                "Dimensional Modelling"
            ]
        ),

        SkillCategoryResponse(
            category="Cloud and Data Platforms",
            skills=[
                "Microsoft Azure",
                "Azure Data Factory",
                "Microsoft Fabric",
                "OneLake",
                "Fabric Lakehouse",
                "Fabric Warehouse",
                "Fabric Data Factory"
            ]
        ),

        SkillCategoryResponse(
            category="Programming and Databases",
            skills=[
                "Python",
                "SQL",
                "T-SQL",
                "PostgreSQL",
                "Microsoft SQL Server",
                "Pandas",
                "NumPy"
            ]
        ),

        SkillCategoryResponse(
            category="Business Intelligence and Analytics",
            skills=[
                "Power BI",
                "DAX",
                "Power Query",
                "Microsoft Excel",
                "SSIS",
                "SSAS",
                "SSRS"
            ]
        ),

        SkillCategoryResponse(
            category="Development Tools",
            skills=[
                "Git",
                "GitHub",
                "SQL Server Management Studio",
                "Visual Studio",
                "Jupyter Notebook"
            ]
        )
    ]