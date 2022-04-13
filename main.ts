let bod1 = [0, 0]
let bod2 = [1, 1]
let i = 2
led.plotBrightness(2, 2, 127)
led.plot(bod1[0], bod1[1])
led.plot(bod2[0], bod2[1])
basic.pause(500)
basic.forever(function Spin() {
    spin_right()
    spin_down()
    spin_left()
    spin_up()
})
function spin_right() {
    
    while (i > 0) {
        led.unplot(bod1[0], bod1[1])
        led.unplot(bod2[0], bod2[1])
        bod1[1] += 2
        bod2[1] += 1
        led.plot(bod1[0], bod1[1])
        led.plot(bod2[0], bod2[1])
        basic.pause(500)
        i -= 1
    }
    i = 2
}

function spin_down() {
    
    while (i > 0) {
        led.unplot(bod1[0], bod1[1])
        led.unplot(bod2[0], bod2[1])
        bod1[0] += 2
        bod2[0] += 1
        led.plot(bod1[0], bod1[1])
        led.plot(bod2[0], bod2[1])
        basic.pause(500)
        i -= 1
    }
    i = 2
}

function spin_left() {
    
    while (i > 0) {
        led.unplot(bod1[0], bod1[1])
        led.unplot(bod2[0], bod2[1])
        bod1[1] -= 2
        bod2[1] -= 1
        led.plot(bod1[0], bod1[1])
        led.plot(bod2[0], bod2[1])
        basic.pause(500)
        i -= 1
    }
    i = 2
}

function spin_up() {
    
    while (i > 0) {
        led.unplot(bod1[0], bod1[1])
        led.unplot(bod2[0], bod2[1])
        bod1[0] -= 2
        bod2[0] -= 1
        led.plot(bod1[0], bod1[1])
        led.plot(bod2[0], bod2[1])
        basic.pause(500)
        i -= 1
    }
    i = 2
}

