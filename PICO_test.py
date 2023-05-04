from rc_car_classes import Potentiometer, Servo, Led

simulation_mode = True

sensor_simulation = True
actuator_simulation = True
E_stop_simulation = True

Test_pot_svalue = 1000


if simulation_mode == True:
    print('simulation mode')
    sensor_simulation = True
    actuator_simulation = True

Test_pot = Potentiometer(1, 100, 65400, sensor_simulation)
Test_servo = Servo(2, 100, 4, 5100, actuator_simulation, 1, 1200)
test_led = Led(100, actuator_simulation, 6,7,8)

print(Test_pot.read(sensor_simulation, Test_pot_svalue))
print(Test_servo.E_stop_check(actuator_simulation, False))
print(Test_servo.Drive('Forward', 101, 100, 1000, actuator_simulation, False))
print(test_led.Set_colour(actuator_simulation, 300, 600, 800))