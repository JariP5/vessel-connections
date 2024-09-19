from vessel_connections.equipment.equipment import Equipment

class Tank(Equipment):

    def get_equipment_type(self) -> str:
        return 'tank'