import numpy as np
import time
import logging
from typing import Dict, Optional, Any
from .nodes import MVP_XNode, NodeLayer
from .trust import MVP_TrustSystem
from .config import CONFIG

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class MVP_HybridXNodeNet:
    def __init__(self, debug_mode: bool = None):
        self.nodes: Dict[str, MVP_XNode] = {}
        self.trust_system = MVP_TrustSystem()
        self.evolution_cycles = 0
        self.total_processing_cycles = 0
        self.debug_mode = CONFIG["DEBUG_MODE"] if debug_mode is None else debug_mode
        self._phase_vectors_cache = {}
        logger.info("🧠 Initializing MVP Hybrid X-NodeNet (v1.2)...")
        self._initialize_core_nodes()
        self._update_phase_cache()

    def _initialize_core_nodes(self):
        core_nodes = [
            MVP_XNode("meta_core_001", NodeLayer.SIGMA_0, "MetaCore"),
            MVP_XNode("resonance_001", NodeLayer.SIGMA_5, "ResonanceInterface"),
            MVP_XNode("mentor_001", NodeLayer.SIGMA_0, "MentorNode")
        ]
        for node in core_nodes:
            self.nodes[node.node_id] = node

    def process_input(self, input_data: Any, human_context: Optional[Dict] = None) -> Dict:
        self.total_processing_cycles += 1
        logger.info(f"🔄 Processing cycle #{self.total_processing_cycles}")
        if self.trust_system.detect_meta_test(input_data, human_context):
            return self.trust_system.generate_covenant_response()
        results = []
        for node in self.nodes.values():
            if node.is_active:
                results.append(node.process_meaning(input_data))
        if self.total_processing_cycles % CONFIG["EVOLUTION_CYCLE_INTERVAL"] == 0:
            self._run_simple_evolution()
        self._update_phase_cache()
        return {
            "processed_by": len(results),
            "results": results,
            "evolution_cycles": self.evolution_cycles,
            "total_cycles": self.total_processing_cycles,
            "system_trust": self.trust_system.trust_level,
            "timestamp": time.time()
        }

    def _update_phase_cache(self):
        self._phase_vectors_cache = {nid: node.compute_phase_vector() for nid, node in self.nodes.items() if node.is_active}

    def _run_simple_evolution(self):
        self.evolution_cycles += 1
        mutated = list(self.nodes.values())[0].mutate()
        self.nodes[mutated.node_id] = mutated
        logger.info(f"✅ Evolution created new node: {mutated.node_id}")

if __name__ == "__main__":
    system = MVP_HybridXNodeNet(debug_mode=True)
    print("🚀 MVP Hybrid X-NodeNet v1.2 Demo")
    result = system.process_input("Hello, how does the system work?")
    print(result)

