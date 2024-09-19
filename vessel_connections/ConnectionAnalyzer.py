from typing import Dict, List, Set
from vessel_connections.Equipment import Equipment

class ConnectionAnalyzer:
    def __init__(self, vessel):
        self.vessel = vessel

    def find_connected_equipment(self, open_valve_ids: Set[str]) -> Dict[str, Set[str]]:
        """
        Find equipment connected to each piece of equipment through open valves.

        :param open_valve_ids: Set of IDs of open valves
        :return: Dictionary with equipment IDs as keys and sets of connected equipment IDs as values
        """
        connections = {}
        all_equipment = {**self.vessel.tanks, **self.vessel.pipes,
                         **self.vessel.pumps, **self.vessel.sea_connections}

        for eq_id, equipment in all_equipment.items():
            connected = self._find_connected_recursive(equipment, open_valve_ids, set())
            if connected:
                connections[eq_id] = connected

        return connections

    def _find_connected_recursive(self, equipment: Equipment, open_valve_ids: Set[str], visited: Set[str]) -> Set[str]:
        connected = set()
        visited.add(equipment.id)

        for valve_id in equipment.connected_valves:
            if valve_id in open_valve_ids:
                valve = self.vessel.valves[valve_id]
                for connected_eq in valve.connected_equipment:
                    if connected_eq.id not in visited:
                        connected.add(connected_eq.id)
                        connected.update(self._find_connected_recursive(connected_eq, open_valve_ids, visited))

        return connected

    # def is_path_exists(self, start_id: int,  start_type: str, end_id: int, end_type: str, open_valve_ids: Set[str]) -> bool:
    #     """
    #     Check if there's a path between two pieces of equipment through open valves.
    #
    #     :param start_id: ID of the starting equipment
    #     :param end_id: ID of the ending equipment
    #     :param s: ID of the starting equipment
    #     :param end_id: ID of the ending equipment
    #     :param open_valve_ids: Set of IDs of open valves
    #     :return: True if a path exists, False otherwise
    #     """
    #     all_equipment = {**self.vessel.tanks, **self.vessel.pipes,
    #                      **self.vessel.pumps, **self.vessel.sea_connections}
    #
    #     start_equipment = all_equipment.get(start_id)
    #     if not start_equipment:
    #         return False
    #
    #     connected = self._find_connected_recursive(start_equipment, open_valve_ids, set())
    #     return end_id in connected