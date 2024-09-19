import yaml
from typing import Any, Dict, List, Union, Optional

VesselData = Dict[str, Union[str, Dict[str, List[str]]]]

class DataLoader:
    """Class to handle loading and validating YAML data for vessel configurations."""

    @staticmethod
    def load(file_path: str) -> Optional[VesselData]:
        try:
            with open(file_path, 'r') as file:
                data = yaml.safe_load(file)

            if not DataLoader._validate_vessel_data(data):
                print("Error: Loaded data does not conform to data structure")
                return None

            return data
        except (yaml.YAMLError, IOError) as e:
            print(f"Error loading YAML file: {e}")
            return None

    @staticmethod
    def _validate_vessel_data(data: Any) -> bool:
        if not isinstance(data, dict):
            return False

        required_keys = {'vessel', 'version', 'tanks', 'pipes', 'pumps', 'sea'}
        if not all(key in data for key in required_keys):
            return False

        if (not isinstance(data['vessel'], str) or
            not isinstance(data['version'], str)):
            return False

        equipment_types = ['tanks', 'pipes', 'pumps', 'sea']
        for eq_type in equipment_types:
            if not isinstance(data[eq_type], dict):
                return False
            for key, value in data[eq_type].items():
                if not isinstance(key, str) or not isinstance(value, list):
                    return False
                if not all(isinstance(v, str) for v in value):
                    return False

        return True