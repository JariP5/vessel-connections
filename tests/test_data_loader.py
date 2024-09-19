import unittest
from unittest.mock import patch, mock_open
import yaml
from typing import Dict, List, Union, Optional

from vessel_connections.data_loader import DataLoader

# Define the type alias for the vessel data
VesselData = Dict[str, Union[str, Dict[str, List[str]]]]

valid_data = {
    'vessel': 'test_vessel',
    'version': '0.0.1',
    'tanks': {
        '001': ['001'],
        '002': ['003'],
        '003': ['005'],
        '004': ['007'],
        '005': ['009'],
        '006': []  # Valid: empty list
    },
    'pipes': {
        '': ['001', '002', '012'],  # Valid: Empty id
        '002': ['002', '003', '004'],
        '003': ['004', '005', '006'],
        '004': ['006', '007', '008'],
        '005': ['008', '009', '010'],
        '006': ['010', '011', '012'],
        '007': ['001', '013'],
        '008': ['013', '014'],
        '009': ['010', '014'],
        '010': ['013', '015', '017'],
        '011': ['014', '016', '018'],
        '012': ['019', '021', '023'],
        '013': ['020', '022', '024'],
        '014': ['004', '023'],
        '015': ['023', '024'],
        '016': ['008', '024']
    },
    'pumps': {
        '01': ['017', '019'],
        '02': ['018', '020']
    },
    'sea': {
        'underboard': ['015', '016']  # Valid: unexpected key
    }
}

invalid_data: VesselData = {
    'vessel': 'test_vessel',
    # 'version': '0.0.1', Invalid: Missing version key
    'tanks': {
        '001': ['001'],
        '002': ['003'],
        '003': ['005'],
        '004': ['007'],
        '005': ['009'],
        '006': ['011']
    },
    'pipes': {
        '001': ['001', '002', '012'],
        '002': ['002', '003', '004'],
        '003': ['004', '005', '006'],
        '004': ['006', '007', '008'],
        '005': ['008', '009', '010'],
        '006': ['010', '011', '012'],
        '007': ['002', '013'],
        '008': ['013', '014'],
        '009': ['010', '014'],
        '010': ['013', '015', '017'],
        '011': ['014', '016', '018'],
        '012': ['019', '021', '023'],
        '013': ['020', '022', '024'],
        '014': ['004', '023'],
        '015': ['023', '024'],
        '016': ['008', '024']
    },
    'pumps': {
        '01': ['017', '019'],
        '02': ['018', '020']
    },
    'sea': {
        'overboard': ['015', '016'],
        'seachest': ['021', '022']
    }
}

class TestDataLoader(unittest.TestCase):

    def setUp(self):
        self.valid_data = valid_data
        self.invalid_data = invalid_data

    @patch('builtins.open', new_callable=mock_open, read_data=yaml.dump(valid_data))
    def test_load_valid_data(self, mock_file):
        loader = DataLoader()
        result = loader.load('test.yml')
        self.assertEqual(result, self.valid_data)

    @patch('builtins.open', new_callable=mock_open, read_data=yaml.dump(invalid_data))
    def test_load_invalid_data(self, mock_file):
        loader = DataLoader()
        result = loader.load('test.yml')
        self.assertIsNone(result)

    @patch('builtins.open', new_callable=mock_open)
    def test_load_file_error(self, mock_file):
        mock_file.side_effect = IOError("File not found")
        loader = DataLoader()
        result = loader.load('nonexistent.yml')
        self.assertIsNone(result)

    def test_validate_vessel_data_valid(self):
        self.assertTrue(DataLoader._validate_vessel_data(self.valid_data))

    def test_validate_vessel_data_invalid(self):
        self.assertFalse(DataLoader._validate_vessel_data(self.invalid_data))
