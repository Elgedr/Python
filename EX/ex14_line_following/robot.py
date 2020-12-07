"""Robothard."""
from PiBot import PiBot  # robot class
robot = PiBot()  # robot object

a = robot.get_left_line_sensors()
b = robot.get_leftmost_line_sensor()

robot.set_wheels_speed(30)
for u in range(500):
    while a[0] > 0 and b[0] > 0:
        robot.set_left_wheel_speed(-2)
        robot.set_wheels_speed(2)
        a = robot.get_left_line_sensors()
        print(a)
        robot.sleep(0.01)


robot.set_wheels_speed(30)
robot.sleep(0.05)
robot.set_wheels_speed(0)
