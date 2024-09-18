from pydantic import field_validator
from vessel_connections.Equipment import Equipment

class Pipe(Equipment):
    """Represents a pipe in the vessel."""

    @field_validator('id')
    def validate_id(cls, v: str) -> str:
        """Ensure that the pipe ID is a number."""
        if not v.isdigit():
            raise ValueError('Pipe ID must be a number')
        return v

    def equipment_type(self) -> str:
        """Return the type of equipment."""
        return "pipe"
