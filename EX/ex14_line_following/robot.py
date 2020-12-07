"""Robothard."""
from PiBot import PiBot  # robot class
robot = PiBot()  # robot object

for i in range(2100):
    a = robot.get_left_line_sensors()
    b = robot.get_right_line_sensors()

    if a[0] > 90 and b[0] > 90:
        robot.set_wheels_speed(50)
        robot.sleep(0.01)
    else:
        robot.set_left_wheel_speed(2)
        robot.set_right_wheel_speed(0)
        robot.sleep(0.01)
robot.done()
