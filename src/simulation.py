import random
from src.models import MobileNode, AccessPoint, Network
from src.pso import PSO
from src.mro import MRO

class Simulation:
    def __init__(self, network, service_requirements):
        self.network = network
        self.service_requirements = service_requirements
        self.mro = MRO()
        self.time = 0

    def run(self, simulation_duration):
        for t in range(simulation_duration):
            self.time = t
            print(f"--- Simulation Time: {self.time}s ---")

            for mn in self.network.mobile_nodes:
                mn.move() # Update the mobile node's position
                print(f"Mobile Node {mn.node_id} moved to {mn.position}")

                # Find the best access point using PSO
                pso = PSO(mn, self.network.access_points, self.service_requirements)
                best_ap = pso.run()

                if best_ap and best_ap != mn.current_ap:
                    if self.mro.is_blacklisted(mn, best_ap, self.time):
                        print(f"AP {best_ap.ap_id} is blacklisted for MN {mn.node_id}. Skipping handoff.")
                        continue

                    # Check for ping-pong handoffs before proceeding
                    if not self.mro.detect_ping_pong(mn, best_ap, self.time):
                        print(f"Mobile Node {mn.node_id} is attempting handoff to {best_ap.ap_id}")
                        # Simulate handoff success/failure
                        if random.random() > 0.1: # 90% success rate
                            mn.current_ap = best_ap # Update the current AP
                            self.mro.record_handoff(mn, best_ap, self.time)
                            print(f"Handoff to AP {best_ap.ap_id} successful for MN {mn.node_id}.")
                        else:
                            self.mro.handle_handoff_failure(mn, best_ap, self.time)
                    else:
                        print(f"Ping-pong handoff detected for Mobile Node {mn.node_id}. Preventing handoff to {best_ap.ap_id}")
                elif best_ap:
                    print(f"Mobile Node {mn.node_id} is already connected to the best AP: {best_ap.ap_id}")
