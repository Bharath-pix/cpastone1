from src.models import MobileNode, AccessPoint, Network
from src.simulation import Simulation

def main():
    # Create mobile nodes
    mn1 = MobileNode(node_id=1, position=(10, 20), velocity=5, battery_level=80)
    mn2 = MobileNode(node_id=2, position=(50, 60), velocity=10, battery_level=60)

    # Create access points
    ap1 = AccessPoint(ap_id=1, position=(15, 25), signal_strength=80, network_type='Wi-Fi')
    ap1.cost_per_mb = 0.1
    ap2 = AccessPoint(ap_id=2, position=(55, 65), signal_strength=90, network_type='Cellular')
    ap2.cost_per_mb = 0.5

    # Create network
    network = Network(mobile_nodes=[mn1, mn2], access_points=[ap1, ap2])

    # Define service requirements
    service_requirements = {'bandwidth': 10} # 10 Mbps

    # Create and run simulation
    simulation = Simulation(network, service_requirements)
    simulation.run(simulation_duration=20)

if __name__ == '__main__':
    main()
