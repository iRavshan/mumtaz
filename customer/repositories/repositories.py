from uuid import UUID
from _repositories import _CustomerRepository
from customer.models import Customer

class CustomerRepository(_CustomerRepository):
    
    def get_by_id(self, id: UUID) -> Customer:
        return super().get_by_id(id)
    
    def get_by_key(self, key: str) -> Customer:
        return super().get_by_key(key)