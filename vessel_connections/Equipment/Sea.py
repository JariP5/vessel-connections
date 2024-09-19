from pydantic import field_validator
from vessel_connections.equipment.Equipment import Equipment

class Sea(Equipment):
    """Represents a sea connection in the vessel."""

    @field_validator('id')
    def validate_id(cls, v: str) -> str:
        """Validate the sea connection ID to be 'overboard' or 'seachest'."""
        if v not in ['overboard', 'seachest']:
            raise ValueError('Sea connection ID must be either "overboard" or "seachest"')
        return v

    def get_equipment_type(self) -> str:
        return 'sea'