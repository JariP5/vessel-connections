from pydantic import field_validator
from vessel_connections.Equipment import Equipment

class Pipe(Equipment):
    """Represents a pipe in the vessel."""

    def get_equipment_type(self) -> str:
        """Return the type of equipment."""
        return "pipe"
