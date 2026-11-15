class HazeNet:
    def __init__(self, channels=64):
        self.channels = channels

    @classmethod
    def from_config(cls, path):
        return cls()

    def fit(self):
        return {'status': 'trained'}
