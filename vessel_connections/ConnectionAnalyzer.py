from typing import List, Set, Optional
from pydantic import BaseModel
from vessel_connections.Vessel import Vessel
from vessel_connections.Equipment import Equipment

class ConnectionAnalyzer(BaseModel):
    vessel: Vessel

    def analyze_connections(self) -> List[Set[Equipment]]:
        """Analyze and return the equipment connections based on valve states."""
        visited = set()  # To keep track of visited equipment
        connections = []  # To store the list of connected equipment sets

        # Iterate over all equipment and perform DFS if not visited
        for valve in self.vessel.valves.values():
            if valve.is_open:
                for equipment in valve.connected_equipment:
                    if equipment not in visited:
                        # Find all connected equipment from this starting point
                        connected_set = self._find_connected_equipment(equipment, visited)
                        if connected_set:
                            connections.append(connected_set)

        return connections

    def _find_connected_equipment(self, start_eq: Equipment, visited: Set[Equipment]) -> Set[Equipment]:
        """Perform DFS to find all equipment connected to the start_eq."""
        stack = [start_eq]
        connected_equipment = set()

        while stack:
            eq = stack.pop()
            if eq not in visited:
                visited.add(eq)
                connected_equipment.add(eq)

                # Check which valves are open and lead to other equipment
                for valve in self.vessel.valves.values():
                    if valve.is_open and eq in valve.connected_equipment:
                        # Add all connected equipment to the stack for further traversal
                        stack.extend(valve.connected_equipment - {eq})  # Exclude the current equipment

        return connected_equipment

    def is_equipment_connected(self, type1: str, id1: str, type2: str, id2: str) -> bool:
        """Check if two equipment parts are connected based on their type and ID."""
        eq1 = self.vessel.get_equipment(type1, id1)
        eq2 = self.vessel.get_equipment(type2, id2)

        if eq1 and eq2:
            # Perform DFS to check if eq1 and eq2 are connected
            visited = set()
            stack = [eq1]

            while stack:
                current_eq = stack.pop()
                print(current_eq)
                if current_eq == eq2:
                    return True
                if current_eq not in visited:
                    visited.add(current_eq)
                    for valve in self.vessel.valves.values():
                        if valve.is_open and current_eq in valve.connected_equipment:
                            stack.extend(valve.connected_equipment - {current_eq})

        return False

    def print_connected_sets(self):
        """Print the connected sets of equipment."""
        connections = self.analyze_connections()
        print("Connected equipment sets based on valve states:")
        for i, connected_set in enumerate(connections, 1):
            equipment_info = [f"{eq.get_equipment_type().capitalize()} {eq.id}" for eq in connected_set]
            print(f"Set {i}: {', '.join(equipment_info)}")