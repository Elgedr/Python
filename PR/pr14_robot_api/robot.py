"""Robot."""
from PiBot import PiBot  # robot class
robot = PiBot()  # robot object

a = robot.get_left_line_sensors()

robot.set_wheels_speed(30)
while a[0] > 0:
    robot.set_wheels_speed(50)
    a = robot.get_left_line_sensors()
    print(a)
    robot.sleep(0.01)
for i in range(50):
    robot.set_wheels_speed(50)
    robot.sleep(0.01)


robot.set_wheels_speed(30)
robot.sleep(0.05)
robot.set_wheels_speed(0)
