import matplotlib.pyplot as plt 
import math

gravity = 9.8
speed = float(input("Enter launch speed (m/s): "))
angle = float(input("Enter launch angle (degrees): "))
angle_rad = math.radians(angle)

vx = speed * math.cos(angle_rad)
vy = speed * math.sin(angle_rad)

x = 0
y = 0

x_list = []
y_list = []

while y >= 0:
    x_list.append(x)
    y_list.append(y)
    x = x + vx
    y = y + vy
    vy = vy - gravity

print("Max distance: " + str(round(max(x_list))) + " m")
print("Max height: " + str(round(max(y_list))) + " m")

plt.figure(figsize = (10, 6))
plt.plot(x_list, y_list, color ='blue')
plt.title("Projectile Motion Simulator")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.savefig("projectile_graph.png")
plt.show()