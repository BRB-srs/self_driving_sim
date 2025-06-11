#simulating a basic self-driving car decision for traffic signs

from traffic_sign import TrafficSign

colour = input("Enter the colour of the traffic sign (red or green): ").lower()

#using the TrafficSign class to decide
sign = TrafficSign(colour)
decision = sign.get_direction()

print(decision)
