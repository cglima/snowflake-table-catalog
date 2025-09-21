
"""
This module defines the use cases for the application.
"""
from typing import List
from backend.application.repositories import TableRepository
from backend.domain.entities import Table

class GetTables:
    """
    Use case for getting a list of tables.
    It orchestrates the flow of data from the repository to the client.
    """

    def __init__(self, table_repository: TableRepository):
        """
        Initializes the use case with a table repository.

        Args:
            table_repository: The repository to use for fetching tables.
        """
        self.table_repository = table_repository

    def execute(self) -> List[Table]:
        """
        Executes the use case.

        Returns:
            A list of tables.
        """
        return self.table_repository.get_all()
