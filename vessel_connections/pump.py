from pydantic import field_validator
from vessel_connections.Equipment import Equipment

class Pump(Equipment):
    """Represents a pump in the vessel."""

    def equipment_type(self) -> str:
        """Return the type of equipment."""
        return "pump"
