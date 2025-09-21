
"""
This module defines the repository interfaces for the application layer.
"""
from abc import ABC, abstractmethod
from typing import List
from backend.domain.entities import Table

class TableRepository(ABC):
    """
    Interface for a repository that handles table data.
    This is the contract that the infrastructure layer must follow.
    """

    @abstractmethod
    def get_all(self) -> List[Table]:
        """Returns a list of all tables."""
        pass
