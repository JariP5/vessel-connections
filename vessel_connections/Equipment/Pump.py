from vessel_connections.equipment.Equipment import Equipment

class Pump(Equipment):

    def get_equipment_type(self) -> str:
        return 'pump'
