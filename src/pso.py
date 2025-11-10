from src.models import MobileNode, AccessPoint
from src.handoff_decision import calculate_rss, calculate_network_cost, evaluate_battery_life

import random

def fitness_function(mobile_node, access_point, service_requirements):
    """
    Calculates the fitness of an access point for a given mobile node.
    A higher fitness score indicates a better handoff target.
    """
    # Define weights for each factor
    w_rss = 0.4
    w_cost = 0.3
    w_battery = 0.3

    # Calculate individual scores
    rss = calculate_rss(mobile_node, access_point)
    cost = calculate_network_cost(access_point, service_requirements)
    battery = evaluate_battery_life(mobile_node, access_point)

    # Normalize scores (simple normalization for now)
    normalized_rss = rss / 100
    normalized_cost = 1 - (cost / 100)
    normalized_battery = battery / 100

    # Calculate final fitness score
    fitness = (w_rss * normalized_rss) + (w_cost * normalized_cost) + (w_battery * normalized_battery)
    return fitness

class Particle:
    def __init__(self, access_points):
        self.position = random.choice(access_points)
        self.velocity = 0
        self.best_position = self.position
        self.best_fitness = -1

class PSO:
    def __init__(self, mobile_node, access_points, service_requirements, num_particles=10, num_iterations=100):
        self.mobile_node = mobile_node
        self.access_points = access_points
        self.service_requirements = service_requirements
        self.num_particles = num_particles
        self.num_iterations = num_iterations
        self.swarm = [Particle(access_points) for _ in range(num_particles)]
        self.global_best_position = None
        self.global_best_fitness = -1

    def run(self):
        for _ in range(self.num_iterations):
            for particle in self.swarm:
                fitness = fitness_function(self.mobile_node, particle.position, self.service_requirements)

                if fitness > particle.best_fitness:
                    particle.best_fitness = fitness
                    particle.best_position = particle.position

                if fitness > self.global_best_fitness:
                    self.global_best_fitness = fitness
                    self.global_best_position = particle.position

            for particle in self.swarm:
                # This is a simplified velocity and position update for a discrete problem
                if random.random() < 0.5:
                    particle.position = particle.best_position
                if random.random() < 0.5:
                    particle.position = self.global_best_position

        return self.global_best_position
