"""Robothard."""
from PiBot import PiBot  # robot class
robot = PiBot()  # robot object

# a = robot.get_left_line_sensors()
# b = robot.get_right_line_sensors()
#
# robot.set_wheels_speed(30)
# for u in range(500):
#     while a[0] > 0 and b[0] > 0:
#         robot.set_wheels_speed(50)
#         a = robot.get_left_line_sensors()
#         print(a)
#         robot.sleep(0.01)
#     else:
#         robot.set_left_wheel_speed(-20)
#         robot.set_right_wheel_speed(20)
#
#
#
# robot.set_wheels_speed(30)
# robot.sleep(0.05)
# robot.set_wheels_speed(0)
# a = robot.get_left_line_sensors()
#
# robot.set_wheels_speed(30)
# while a[0] > 0:
#     robot.set_wheels_speed(50)
#     a = robot.get_left_line_sensors()
#     print(a)
#     robot.sleep(0.01)
# for i in range(100):
#     a = robot.get_left_line_sensors()
#     b = robot.get_right_line_sensors()
#     while a[0] < 1024 and b[0] < 1024:
#         robot.set_wheels_speed(50)
#         robot.sleep(0.01)
#     else:
#          robot.set_left_wheel_speed(2)
#          robot.set_right_wheel_speed(0)
#          robot.sleep(0.2)

# print(robot.get_rotation())
# for i in range(50):
#     robot.set_wheels_speed(50)
#     robot.sleep(0.01)
for i in range(100):
    a = robot.get_left_line_sensors()
    b = robot.get_right_line_sensors()

    if a[0] > 90 and b[0] > 90:
        robot.set_wheels_speed(50)
        robot.sleep(0.01)
    else:
        robot.set_left_wheel_speed(2)
        robot.set_right_wheel_speed(0)
        robot.sleep(0.01)

# robot.set_wheels_speed(30)
# robot.sleep(0.05)
robot.set_wheels_speed(0)
robot.done()