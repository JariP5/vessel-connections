from abc import ABC, abstractmethod
from typing import List
from pydantic import BaseModel, field_validator

class Equipment(BaseModel, ABC):
    """Abstract base class for vessel equipment."""

    id: str
    connected_valves: List[str] = []

    @field_validator('id')
    def validate_id(cls, v: str) -> str:
        """Validate that the equipment ID is not empty or only whitespace."""
        if not v.strip():  # Checks if the string is empty or only contains whitespace
            raise ValueError('ID must not be empty or consist solely of whitespace.')
        return v

    @field_validator('connected_valves')
    def check_connected_valves(cls, v: List[str]) -> List[str]:
        """Ensure that the list of connected valves is not empty."""
        if not v:
            raise ValueError('Connected valves must not be empty')
        return v

    @abstractmethod
    def get_equipment_type(self) -> str:
        """Return the type of equipment (e.g., 'tank', 'pipe', 'pump')."""
        pass

    def get_connected_valves(self) -> List[str]:
        """Return a list of valves connected to this equipment."""
        return self.connected_valves

    def is_connected_to_valve(self, valve_id: str) -> bool:
        """Check if the equipment is connected to a specific valve."""
        return valve_id in self.connected_valves

    def __str__(self) -> str:
        """Return a string representation of the equipment."""
        return f"{self.get_equipment_type().capitalize()} {self.id} connected to valves: {', '.join(self.connected_valves)}"

    def __hash__(self):
        """Make the equipment hashable based on its id."""
        return hash(self.id)

    def __eq__(self, other):
        """Define equality based on id and type."""
        if isinstance(other, Equipment):
            return self.id == other.id and self.get_equipment_type() == other.get_equipment_type()
        return False