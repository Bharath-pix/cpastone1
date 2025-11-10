import math

def calculate_rss(mobile_node, access_point):
    """
    Calculates the Received Signal Strength (RSS) between a mobile node and an access point.
    """
    # Simplified model: RSS decreases with the square of the distance
    distance = math.sqrt((mobile_node.position[0] - access_point.position[0])**2 +
                         (mobile_node.position[1] - access_point.position[1])**2)

    if distance == 0:
        return access_point.signal_strength # Max signal strength at the source

    rss = access_point.signal_strength - 20 * math.log10(distance)
    return rss

def calculate_network_cost(access_point, service_requirements):
    """
    Calculates the cost of using a network based on its bandwidth and the user's service requirements.
    """
    # Simplified model: cost is proportional to the requested bandwidth
    cost = service_requirements['bandwidth'] * access_point.cost_per_mb
    return cost

def evaluate_battery_life(mobile_node, access_point):
    """
    Evaluates the battery life of the mobile node when connected to a specific access point.
    """
    # Simplified model: Wi-Fi is more power-efficient than cellular
    if access_point.network_type == 'Wi-Fi':
        return mobile_node.battery_level * 0.9 # 10% power consumption
    else:
        return mobile_node.battery_level * 0.7 # 30% power consumption
