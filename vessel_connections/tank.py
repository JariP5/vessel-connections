from typing import List
from pydantic import field_validator
from Equipment import Equipment

class Tank(Equipment):
    """Represents a tank in the vessel."""

    @field_validator('id')
    def validate_id(cls, v: str) -> str:
        """Ensure that the tank ID is a number."""
        if not v.isdigit():
            raise ValueError('Tank ID must be a number')
        return v

    def equipment_type(self) -> str:
        """Return the type of equipment."""
        return "tank"