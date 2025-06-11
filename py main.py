#simulating a basic self-driving car decision for traffic signs

def get_direction(color):
    color = color.lower()
    if color == "red":
        return "Pass on the RIGHT"
    elif color == "green":
        return "Pass on the LEFT"
    else:
        return "Invalid traffic sign color. Only red or green are allowed."

# Ask user for input
color_input = input("Enter the colour of the traffic sign (red or green): ")

# Get decision based on color
decision = get_direction(color_input)

print(decision)
