def on_button_pressed_a():
    pins.servo_write_pin(AnalogPin.P0, 0)
    basic.pause(500)
    pins.servo_write_pin(AnalogPin.P0, 90)
    basic.pause(500)
    pins.servo_write_pin(AnalogPin.P0, 180)
    basic.pause(500)
    pins.servo_write_pin(AnalogPin.P0, 0)
    basic.pause(500)
input.on_button_pressed(Button.A, on_button_pressed_a)

pins.analog_set_period(AnalogPin.P0, 20000)

def on_forever():
    pass
basic.forever(on_forever)
