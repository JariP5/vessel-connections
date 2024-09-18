class ConnectionAnalyzer:
    def __init__(self, vessel):
        self.vessel = vessel

    def analyze_connections(self, open_valves):
        return self.vessel.find_connections(open_valves)

    @staticmethod
    def print_connections(self, connections):
        for equipment_id, connected_equipment in connections.items():
            print(f"{equipment_id} is connected to: {', '.join(connected_equipment)}")