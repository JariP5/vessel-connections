from abc import ABC, abstractmethod
from typing import List
from pydantic import BaseModel, field_validator

class Equipment(BaseModel, ABC):
    """Abstract base class for vessel equipment."""

    id: str
    connected_valves: List[str]

    @field_validator('connected_valves')
    def check_connected_valves(cls, v: List[str]) -> List[str]:
        """Ensure that the list of connected valves is not empty."""
        if not v:
            raise ValueError('Connected valves must not be empty')
        return v

    @abstractmethod
    @field_validator('id')
    def validate_id(cls, v: str) -> str:
        """Validate the equipment ID."""
        pass

    @abstractmethod
    def equipment_type(self) -> str:
        """Return the type of equipment (e.g., 'tank', 'pipe', 'pump')."""
        pass

    def get_connected_valves(self) -> List[str]:
        """Return a list of valves connected to this equipment."""
        return self.connected_valves

    def is_connected_to_valve(self, valve: str) -> bool:
        """Check if the equipment is connected to a specific valve."""
        return valve in self.connected_valves

    def __str__(self) -> str:
        """Return a string representation of the equipment."""
        return f"{self.equipment_type().capitalize()} {self.id} connected to valves: {', '.join(self.connected_valves)}"