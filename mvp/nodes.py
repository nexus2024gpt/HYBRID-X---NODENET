import numpy as np

class NodeLayer:
    SIGMA_0 = "Σ₀"
    SIGMA_5 = "Σ₅"

class MVP_XNode:
    def __init__(self, node_id: str, layer: str, core_type: str):
        self.node_id = node_id
        self.layer = layer
        self.core_type = core_type
        self.is_active = True
        self.resonance_threshold = 0.7
        self.evolution_success_count = 0
        # Phase vector simulation
        self.phase = type("Phase", (), {
            "semantic_confidence": np.random.uniform(0.4, 0.9),
            "entropy_state": np.random.uniform(0.1, 0.8)
        })()

    def compute_phase_vector(self):
        return np.array([self.phase.semantic_confidence, self.phase.entropy_state])

    def process_meaning(self, input_data):
        return {
            "node_id": self.node_id,
            "output": f"{self.core_type} processed input: {str(input_data)[:50]}",
            "processing_time_ms": int(np.random.uniform(30, 80)),
            "confidence": self.phase.semantic_confidence
        }

    def mutate(self):
        new_id = f"{self.core_type.lower()}_mut_{np.random.randint(1000,9999)}"
        mutated = MVP_XNode(new_id, self.layer, self.core_type)
        return mutated

    def check_resonance(self, other_node):
        vec1 = self.compute_phase_vector()
        vec2 = other_node.compute_phase_vector()
        return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))

