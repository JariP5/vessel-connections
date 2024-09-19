from vessel_connections.DataLoader import DataLoader
from vessel_connections.Vessel import Vessel
from vessel_connections.VesselBuilder import VesselBuilder
from vessel_connections.ConnectionAnalyzer import ConnectionAnalyzer

SCENARIO = 1

def main():
    # Create a data loader
    data_loader = DataLoader()

    # Load data from yml file
    vessel_data = data_loader.load('../settings/vessel.yml')

    if vessel_data is None:
        print("Exiting.")
        return

    # Create a vessel from the loaded data
    vessel = VesselBuilder().load_from_data(vessel_data).build()

    # Print vessel details
    print(vessel)

    # Create analyzer to understand connections for different valve settings
    analyzer = ConnectionAnalyzer(vessel=vessel)

    is_connected = analyzer.is_equipment_connected(type1="tank", id1="001", type2="pipe", id2="002")
    print(f"Equipment connected: {is_connected}")

    # Scenarios
    if SCENARIO == 1:
        vessel.open_valve('001')
        vessel.open_valve('002')
        vessel.open_valve('010')
        vessel.open_valve('015')
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 2:
        vessel.open_valve('002')
        vessel.set_only_open_valves(['001', '004'])
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 3:
        vessel.open_valve('002')
        vessel.set_only_open_valves(['001', '004'])
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 4:
        vessel.open_valve('002')
        vessel.set_only_open_valves(['001', '004'])
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 5:
        vessel.open_valve('002')
        vessel.set_only_open_valves(['001', '004'])
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 6:
        vessel.open_valve('002')
        vessel.set_only_open_valves(['001', '004'])
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 7:
        vessel.open_valve('002')
        vessel.set_only_open_valves(['001', '004'])
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 8:
        vessel.open_valve('002')
        vessel.set_only_open_valves(['001', '004'])
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 9:
        vessel.open_valve('002')
        vessel.set_only_open_valves(['001', '004'])
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    elif SCENARIO == 10:
        vessel.open_valve('002')
        vessel.set_only_open_valves(['001', '004'])
        vessel.print_open_valves()
        analyzer.print_connected_sets()

    else:
        print("Invalid scenario.")

if __name__ == "__main__":
    main()