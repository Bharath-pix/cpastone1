import random

class MobileNode:
    """Represents a mobile device in the simulation."""
    def __init__(self, node_id, position, velocity, battery_level):
        self.node_id = node_id
        self.position = position
        self.velocity = velocity
        self.battery_level = battery_level
        self.direction = (random.random(), random.random()) # Random initial direction
        self.current_ap = None

    def move(self, timestep=1):
        """Moves the mobile node based on its velocity and direction."""
        # This is a simple random walk model. In a real simulation,
        # you might use a more sophisticated model like Random Waypoint.
        self.position = (self.position[0] + self.velocity * self.direction[0] * timestep,
                         self.position[1] + self.velocity * self.direction[1] * timestep)

        # Change direction randomly
        if random.random() < 0.1: # 10% chance to change direction
            self.direction = (random.random() * 2 - 1, random.random() * 2 - 1)

class AccessPoint:
    """Represents a network access point."""
    def __init__(self, ap_id, position, signal_strength, network_type):
        self.ap_id = ap_id
        self.position = position
        self.signal_strength = signal_strength
        self.network_type = network_type

class Network:
    """Represents the overall network, including mobile nodes and access points."""
    def __init__(self, mobile_nodes, access_points):
        self.mobile_nodes = mobile_nodes
        self.access_points = access_points
