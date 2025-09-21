
"""
This module is the main entry point for the backend application.
It creates the FastAPI app and defines the API endpoints.
"""
import os
from fastapi import FastAPI
from dotenv import load_dotenv
from backend.application.use_cases.get_tables import GetTables
from backend.infrastructure.repositories import CsvTableRepository, SnowflakeTableRepository

load_dotenv()

app = FastAPI(
    title="Snowflake Table Catalog API",
    description="API for querying the Snowflake table catalog.",
    version="1.0.0"
)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "API is running"}

@app.get("/tables", tags=["Tables"])
def get_tables():
    """
    Endpoint to get a list of all tables.
    
    The data source is determined by the `APP_ENV` environment variable.
    - `production`: Uses the Snowflake repository.
    - `development` (or any other value): Uses a CSV file.
    """
    if os.environ.get("APP_ENV") == "production":
        repo = SnowflakeTableRepository()
    else:
        repo = CsvTableRepository(file_path="backend/sample_data.csv")
    
    use_case = GetTables(table_repository=repo)
    return use_case.execute()
