from pydantic import field_validator
from vessel_connections.Equipment import Equipment

class Tank(Equipment):
    """Represents a tank in the vessel."""

    def get_equipment_type(self) -> str:
        """Return the type of equipment."""
        return "tank"