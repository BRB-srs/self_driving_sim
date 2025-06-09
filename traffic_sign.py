
class TrafficSign:
    def __init__(self, color):
        self.color = color.lower()

    def get_direction(self):
        if self.color == "red":
            return "Pass on the RIGHT"
        elif self.color == "green":
            return "Pass on the LEFT"
        else:
            return "Invalid traffic sign color. Only red or green are allowed."
