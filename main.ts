input.onButtonPressed(Button.A, function () {
    if (角度 < 180) {
        角度 += 90
    } else {
        角度 = 0
    }
    pins.servoWritePin(AnalogPin.P0, 角度)
    basic.pause(500)
})
input.onButtonPressed(Button.B, function () {
    pins.servoWritePin(AnalogPin.P0, 0)
})
let 角度 = 0
pins.analogSetPeriod(AnalogPin.P0, 20000)
