"""
This module implements the repository interfaces defined in the application layer.
"""
import pandas as pd
import numpy as np
from typing import List
from backend.application.repositories import TableRepository
from backend.domain.entities import Table

class CsvTableRepository(TableRepository):
    """
    A repository that reads table data from a CSV file.
    This is useful for development and testing without a live Snowflake connection.
    """

    def __init__(self, file_path: str):
        """
        Initializes the repository with the path to the CSV file.

        Args:
            file_path: The path to the CSV file.
        """
        self.file_path = file_path

    def get_all(self) -> List[Table]:
        """Reads the CSV file and returns a list of Table entities."""
        df = pd.read_csv(self.file_path)
        
        # Coerce errors will turn bad parsing into NaT
        df['CREATED'] = pd.to_datetime(df['CREATED'], errors='coerce')
        df['LAST_ALTERED'] = pd.to_datetime(df['LAST_ALTERED'], errors='coerce')

        # Replace all pandas null-like values (NaN, NaT) with Python's None
        df = df.replace({np.nan: None})
        
        tables = []
        for _, row in df.iterrows():
            tables.append(Table(**row.to_dict()))
        return tables

import os
import snowflake.connector

class SnowflakeTableRepository(TableRepository):
    """
    A repository that reads table data from a Snowflake database.
    """

    def get_all(self) -> List[Table]:
        """
        Connects to Snowflake, queries the table information, and returns a list of Table entities.
        
        Note:
            This repository expects the following environment variables to be set:
            - SNOWFLAKE_USER
            - SNOWFLAKE_PASSWORD
            - SNOWFLAKE_ACCOUNT
        """
        conn = snowflake.connector.connect(
            user=os.environ.get('SNOWFLAKE_USER'),
            password=os.environ.get('SNOWFLAKE_PASSWORD'),
            account=os.environ.get('SNOWFLAKE_ACCOUNT'),
        )

        query = """SELECT
            concat_ws('.',t.table_catalog,t.table_schema,t.table_name) as TABLE_ID,
            t.TABLE_CATALOG,
            t.CREATED,
            t.TABLE_NAME,
            t.TABLE_SCHEMA,
            t.TABLE_OWNER,
            t.TABLE_TYPE,
            t.IS_TRANSIENT,
            t.CLUSTERING_KEY,
            t.ROW_COUNT,
            t.BYTES,
            t.RETENTION_TIME,
            t.LAST_ALTERED,
            t.AUTO_CLUSTERING_ON,
            t.COMMENT,
            c.column_count
        from
            LATAM_ANALYTICS_DLH.INFORMATION_SCHEMA.TABLES t
            left join (
                select
                    concat_ws('.',table_catalog,table_schema,table_name) as table_id,
                    count(1) over(partition by table_id) column_count
                from
                    latam_analytics_dlh.information_schema.columns
                group by
                    table_id
            ) c 
            on
             c.table_id = concat_ws('.',t.table_catalog,t.table_schema,t.table_name)
            where
                t.table_schema <> 'INFORMATION_SCHEMA';      """
        
        cursor = conn.cursor()
        cursor.execute(query)
        
        df = cursor.fetch_pandas_all()
        # Replace all pandas null-like values (NaN, NaT) with Python's None
        df = df.replace({np.nan: None})
        cursor.close()
        conn.close()

        tables = []
        for _, row in df.iterrows():
            tables.append(Table(**row.to_dict()))
        return tables