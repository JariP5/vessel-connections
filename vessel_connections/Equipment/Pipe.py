from vessel_connections.equipment.equipment import Equipment

class Pipe(Equipment):

    def get_equipment_type(self) -> str:
        return 'pipe'
