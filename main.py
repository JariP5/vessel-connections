from vessel_connections.data_loader import DataLoader
from vessel_connections.connection_analyzer import ConnectionAnalyzer
from vessel_connections.vessel.vessel_builder import VesselBuilder

# Scenario number to test different valve states
SCENARIO = 9

def main():
    """Main function to execute different scenarios based on valve settings."""
    # Create a data loader
    data_loader = DataLoader()

    # Load data from YAML file
    vessel_data = data_loader.load('settings/vessel.yml')

    if vessel_data is None:
        print('Exiting.')
        return

    # Create a vessel from the loaded data
    vessel = VesselBuilder().load_from_data(vessel_data).build()

    # Print vessel details
    print(vessel)

    # Create analyzer to understand connections for different valve settings
    analyzer = ConnectionAnalyzer(vessel=vessel)

    # Execute different scenarios
    if SCENARIO == 1:
        vessel.open_valve('001')
        vessel.open_valve('002')
        vessel.open_valve('010')
        vessel.open_valve('015')
        vessel.open_valve('023')
        vessel.open_valve('033')
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 2:
        vessel.close_all_valves()
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 3:
        vessel.open_valve('002')
        vessel.close_valve('001')
        vessel.close_valve('010')
        vessel.close_valve('015')
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 4:
        vessel.open_valve('001')
        vessel.open_valve('004')
        vessel.open_valve('007')
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 5:
        vessel.open_valve('010')
        vessel.open_valve('015')
        vessel.close_valve('001')
        vessel.close_valve('015')
        vessel.print_open_valves()
        analyzer.print_connected_sets()
        is_connected = analyzer.is_equipment_connected(
            type1='tank', id1='001', type2='pipe', id2='010')
        print(f'Equipment connected: {is_connected}')

    elif SCENARIO == 6:
        vessel.open_valve('999')
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 7:
        vessel.close_all_valves()
        vessel.print_open_valves()
        analyzer.print_connected_sets()
        print()
        for valve_id in vessel.valves:
            vessel.open_valve(valve_id)
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 8:
        vessel.open_valve('003')
        vessel.open_valve('008')
        vessel.open_valve('014')
        vessel.close_valve('001')
        vessel.close_valve('002')
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 9:
        vessel.open_valve('002')
        vessel.open_valve('003')
        vessel.open_valve('005')
        vessel.open_valve('007')
        vessel.open_valve('013')
        vessel.open_valve('017')
        vessel.print_open_valves()
        is_connected = analyzer.is_equipment_connected(
            type1='tank', id1='002', type2='pump', id2='01')
        print(f'Equipment connected: {is_connected}')

    elif SCENARIO == 10:
        vessel.open_valve('001')
        vessel.print_open_valves()
        analyzer.print_connected_sets()
        print()
        vessel.close_valve('001')
        vessel.open_valve('004')
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    else:
        print('Invalid scenario.')

if __name__ == '__main__':
    main()
