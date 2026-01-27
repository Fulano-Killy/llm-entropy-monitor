class EntropyMonitor:

    """

    Module for Real-Time Semantic Density Analysis in LLM Streams.

    Prevents deterministic loops by monitoring Shannon Entropy thresholds.

    """

    def __init__(self, entropy_threshold=1.2, window_size=5):

        # Umbral termodinámico estándar para lenguaje natural

        self.threshold = entropy_threshold

        self.window_size = window_size

        self.token_buffer = []



    def _calculate_shannon_entropy(self, sequence):

        """

        Computes H(X) = -sum(p(x) * log2(p(x))) for the current window.

        """

        if not sequence: return 0.0

        

        counts = Counter(sequence)

        total_count = len(sequence)

        probs = [count / total_count for count in counts.values()]

        

        # Shannon Entropy formula

        entropy = -sum(p * math.log2(p) for p in probs)

        return entropy



    def analyze_stream(self, new_token):

        """

        Ingests a token and returns the system state: 'STABLE' or 'CRITICAL'.

        """

        self.token_buffer.append(new_token)

        

        # Maintain sliding window size

        if len(self.token_buffer) > self.window_size:

            self.token_buffer.pop(0)

            

        current_entropy = self._calculate_shannon_entropy(self.token_buffer)

        

        # Diagnostics print (Optional: Remove for production)

        # print(f"Token: {new_token} | H(S): {current_entropy:.4f}")



        if len(self.token_buffer) == self.window_size:

            if current_entropy < self.threshold:

                return {

                    "status": "CRITICAL",

                    "action": "INJECT_STOCHASTIC_NOISE",

                    "reason": "Low entropy detected (Loop probability > 95%)"

                }

        

        return {"status": "STABLE", "entropy": current_entropy}



# --- Quick Test Block ---

if __name__ == "__main__":
