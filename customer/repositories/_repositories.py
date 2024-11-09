from abc import abstractmethod
from typing import List
from uuid import UUID
from common._repositories import _BaseRepository
from ..models import Customer

class _CustomerRepository(_BaseRepository[Customer]):
    
    @abstractmethod
    def get_by_id(self, id: UUID) -> Customer:
        pass

    @abstractmethod
    def get_by_key(self, key: str) -> Customer:
        pass
    
    