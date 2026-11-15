class RecessionModel:
    def predict_interval(self, q):
        return q, q * 1.1
