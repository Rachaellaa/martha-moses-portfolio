from fastapi import APIRouter
from app.schemas.projects import ProjectResponse

router = APIRouter(prefix="/api/projects", tags=["Projects"])


@router.get("/", response_model=list[ProjectResponse])
def get_projects():

    return [

        ProjectResponse(
            title="Enterprise SQL Server Data Warehousing, ETL & BI Platform",
            category="Data Engineering",
            industry="Enterprise Data and Business Intelligence",
            description="An enterprise-style data warehousing solution for integrating, transforming and organising business data.",
            problem_statement="Fragmented data sources make reliable reporting difficult.",
            solution="Designed a SQL Server data warehouse with ETL processes and analytical reporting.",
            technologies=["SQL Server", "T-SQL", "SSIS", "SSAS", "SSRS", "Power BI"],
            key_features=["ETL pipelines", "Data warehousing", "Dimensional modelling", "Reporting"],
            featured=True
        ),

        ProjectResponse(
            title="End-to-End Modern Data Engineering Platform",
            category="Data Engineering",
            industry="Enterprise Data Infrastructure",
            description="A modern data engineering platform covering ingestion, transformation and storage.",
            problem_statement="Organisations need scalable and maintainable data pipelines.",
            solution="Designed a modular architecture for data ingestion, transformation and storage.",
            technologies=["Python", "SQL", "PostgreSQL", "Microsoft Azure", "Azure Data Factory", "Microsoft Fabric"],
            key_features=["Data ingestion", "ETL and ELT", "Transformation", "Pipeline orchestration"],
            featured=True
        ),

        ProjectResponse(
            title="Cloud Data Engineering and Lakehouse Platform",
            category="Data Engineering",
            industry="Cloud Data Infrastructure",
            description="A cloud-focused data platform demonstrating modern lakehouse architecture.",
            problem_statement="Traditional storage environments can limit integrated data processing.",
            solution="Designed a cloud data architecture using Azure and Microsoft Fabric.",
            technologies=["Microsoft Azure", "Azure Data Factory", "Microsoft Fabric", "OneLake", "Python", "SQL"],
            key_features=["Cloud ingestion", "Lakehouse architecture", "Data transformation", "Cloud storage"],
            featured=True
        ),

        ProjectResponse(
            title="Real-Time Data Streaming and Processing",
            category="Data Engineering",
            industry="Real-Time Data Infrastructure",
            description="A project focused on processing continuously generated data.",
            problem_statement="Batch processing can delay access to operational information.",
            solution="Designed a workflow demonstrating event ingestion and downstream data delivery.",
            technologies=["Python", "SQL", "PostgreSQL", "Data Streaming"],
            key_features=["Event ingestion", "Stream processing", "Data transformation", "Data storage"],
            featured=True
        ),

        ProjectResponse(
            title="Retail Business Performance and Executive Sales Intelligence",
            category="Data Analytics & Business Intelligence",
            industry="Retail and E-commerce",
            description="An analytical solution transforming retail sales data into business insights.",
            problem_statement="Retail stakeholders need visibility into sales and product performance.",
            solution="Used SQL and Python for analysis and Power BI for executive reporting.",
            technologies=["PostgreSQL", "SQL", "Python", "Pandas", "NumPy", "Excel", "Power BI", "DAX"],
            key_features=["Sales analysis", "Product performance", "Business KPIs", "Executive dashboards"],
            featured=True
        ),

        ProjectResponse(
            title="Customer Behaviour, Segmentation and Predictive Analytics",
            category="Data Analytics & Business Intelligence",
            industry="Customer Analytics",
            description="A customer analytics solution focused on behaviour and segmentation.",
            problem_statement="Businesses need to understand customer behaviour.",
            solution="Used SQL, Python and machine learning techniques to analyse customer data.",
            technologies=["PostgreSQL", "Python", "Pandas", "NumPy", "Scikit-learn", "Power BI"],
            key_features=["Customer segmentation", "Behavioural analysis", "Predictive modelling"],
            featured=True
        ),

        ProjectResponse(
            title="Food Industry Quality, Production and Operational Analytics",
            category="Data Analytics & Business Intelligence",
            industry="Food Manufacturing",
            description="An analytical project focused on food production and quality indicators.",
            problem_statement="Food production environments need reliable quality and operational data.",
            solution="Applied SQL, Python and Power BI to analyse operational datasets.",
            technologies=["PostgreSQL", "SQL", "Python", "Pandas", "NumPy", "Power BI"],
            key_features=["Production analysis", "Quality analysis", "Operational KPIs", "Dashboards"],
            featured=True
        )

    ]