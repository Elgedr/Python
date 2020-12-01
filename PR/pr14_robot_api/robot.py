from PiBot import PiBot  # robot class
robot = PiBot()  # robot object

# distance_from_object = robot.get_front_middle_laser()
# print(distance_from_object)
#
# robot.set_wheels_speed(20)
# while distance_from_object > 0.01:
#     distance_from_object = robot.get_front_middle_laser()
#     robot.sleep(0.05)
# print("Hello!")
# print(robot.sleep(1))
# robot.set_wheels_speed(30)
# while robot.get_line_sensors() > 100:
#     robot.set_wheels_speed(30)
# robot.set_wheels_speed(0)

if __name__ == '__main__':

    print("Hello!")
    print(robot.sleep(1))
    robot.set_wheels_speed(30)
    robot.set_wheels_speed(30)
    robot.sleep(2)
    robot.set_wheels_speed(0)
    # while robot.get_line_sensors() > 100:
    #     robot.set_wheels_speed(30)
    # robot.set_wheels_speed(0)



# Stop the robot when done
robot.set_wheels_speed(0)

# print(robot.set_wheels_speed(30))  # percentage of robots max speed
# print(robot.sleep(2))
# print(robot.set_wheels_speed(0))
# print(robot.get_front_lasers())
#
# print(robot.get_rear_irs())
# print(robot.get_distance_sensors())
#
# print(robot.get_leftmost_line_sensor())
# print(robot.get_second_line_sensor_from_left())
# print(robot.get_third_line_sensor_from_left())
#
# print(robot.get_rightmost_line_sensor())
# print(robot.get_second_line_sensor_from_right())
# print(robot.get_third_line_sensor_from_right())
#
# print(robot.get_rotation())  # на сколько градусов он повернулся
# print(robot.WHEEL_DIAMETER)
