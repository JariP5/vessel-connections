from vessel_connections.equipment.Equipment import Equipment

class Pump(Equipment):
    """Represents a pump in the vessel."""

    def get_equipment_type(self) -> str:
        """Return the type of equipment."""
        return "pump"
