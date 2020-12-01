from PiBot import PiBot  # robot class
robot = PiBot()  # robot object

print(robot.set_wheels_speed(30))
print(robot.sleep(2))
print(robot.set_wheels_speed(0))


