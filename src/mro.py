class MRO:
    def __init__(self, ping_pong_threshold=5, blacklist_duration=10):
        """
        Initializes the Mobile Robustness Optimization module.
        :param ping_pong_threshold: The time threshold (in seconds) to detect ping-pong handoffs.
        :param blacklist_duration: The time duration (in seconds) to blacklist a failed access point.
        """
        self.ping_pong_threshold = ping_pong_threshold
        self.blacklist_duration = blacklist_duration
        self.handoff_history = {}
        self.blacklist = {}

    def detect_ping_pong(self, mobile_node, target_ap, current_time):
        """
        Detects if a handoff is a ping-pong handoff.
        A ping-pong handoff occurs when a mobile node switches back to a previous access point too quickly.
        """
        if mobile_node.node_id not in self.handoff_history:
            return False

        history = self.handoff_history[mobile_node.node_id]
        if len(history) < 2:
            return False

        last_handoff = history[-1]
        previous_handoff = history[-2]

        # Check if the mobile node is switching back to the previous AP within the threshold
        if (previous_handoff['ap_id'] == target_ap.ap_id and
                (current_time - last_handoff['timestamp']) < self.ping_pong_threshold):
            return True

        return False

    def record_handoff(self, mobile_node, ap, current_time):
        """
        Records a successful handoff in the history.
        """
        if mobile_node.node_id not in self.handoff_history:
            self.handoff_history[mobile_node.node_id] = []

        self.handoff_history[mobile_node.node_id].append({
            'ap_id': ap.ap_id,
            'timestamp': current_time
        })

    def handle_handoff_failure(self, mobile_node, failed_ap, current_time):
        """
        Handles a handoff failure by blacklisting the failed access point for a certain duration.
        """
        key = (mobile_node.node_id, failed_ap.ap_id)
        expiration_time = current_time + self.blacklist_duration
        self.blacklist[key] = expiration_time
        print(f"Handoff to AP {failed_ap.ap_id} failed for MN {mobile_node.node_id}. Blacklisted until time {expiration_time}.")

    def is_blacklisted(self, mobile_node, ap, current_time):
        """
        Checks if an access point is currently blacklisted for a mobile node.
        """
        key = (mobile_node.node_id, ap.ap_id)
        if key in self.blacklist:
            if current_time < self.blacklist[key]:
                return True
            else:
                # Remove expired blacklist entry
                del self.blacklist[key]
        return False
