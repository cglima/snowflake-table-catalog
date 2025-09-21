
"""
This module defines the domain entities of the application.
"""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Table:
    """
    Represents a table in Snowflake.
    This is a pure domain entity with no logic.
    """
    TABLE_ID: str
    TABLE_CATALOG: str
    CREATED: datetime
    TABLE_NAME: str
    TABLE_SCHEMA: str
    TABLE_OWNER: str
    TABLE_TYPE: str
    IS_TRANSIENT: str
    CLUSTERING_KEY: str
    ROW_COUNT: int
    BYTES: int
    RETENTION_TIME: int
    LAST_ALTERED: datetime
    AUTO_CLUSTERING_ON: str
    COMMENT: str
    COLUMN_COUNT: int
