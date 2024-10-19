class Controller:
    def __init__(self, Kp: float, Kd: float):
        self.Kp = Kp
        self.Kd = Kd

    def compute_action(self, observation: float, reference: float, vel_y: float) -> float:
        return self.Kp * (reference - observation) + self.Kd * (0 - vel_y) #test
    