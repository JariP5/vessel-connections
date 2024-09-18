from vessel_connections.DataLoader import DataLoader
from vessel_connections.VesselBuilder import VesselBuilder

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
    print(f"Vessel: {vessel.name}")
    print(f"Version: {vessel.version}")
    print(f"Number of tanks: {len(vessel.tanks)}")
    print(f"Number of pipes: {len(vessel.pipes)}")
    print(f"Number of pumps: {len(vessel.pumps)}")
    print(f"Number of sea connections: {len(vessel.sea_connections)}")
    print(f"Number of valves: {len(vessel.valves)}")
    print(f"{vessel.valves}")

    # Print details of each equipment type
    # print("\nTanks:")
    # for tank in vessel.tanks.values():
    #     print(f"  {tank}")
    #
    # print("\nPipes:")
    # for pipe in vessel.pipes.values():
    #     print(f"  {pipe}")

    # print("\nPumps:")
    # for pump in vessel.pumps.values():
    #     print(f"  {pump}")
    #
    # print("\nSea Connections:")
    # for sea in vessel.sea_connections.values():
    #     print(f"  {sea}")


if __name__ == "__main__":
    main()