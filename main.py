bod1 = [0, 0]
bod2 = [1, 1]
i = 2
led.plot_brightness(2, 2, 127)
led.plot(bod1[0], bod1[1])
led.plot(bod2[0], bod2[1])
basic.pause(500)

def Spain_without_the_A():    
    spin_right()
    spin_down()
    spin_left()
    spin_up()
basic.forever(Spain_without_the_A)

def spin_right():
    global i, bod1, bod2
    while i > 0:
        led.unplot(bod1[0], bod1[1])
        led.unplot(bod2[0], bod2[1])
        bod1[1] += 2
        bod2[1] += 1
        led.plot(bod1[0], bod1[1])
        led.plot(bod2[0], bod2[1])
        basic.pause(500)
        i -= 1
    i = 2
def spin_down():
    global i, bod1, bod2
    while i > 0:
        led.unplot(bod1[0], bod1[1])
        led.unplot(bod2[0], bod2[1])
        bod1[0] += 2
        bod2[0] += 1
        led.plot(bod1[0], bod1[1])
        led.plot(bod2[0], bod2[1])
        basic.pause(500)
        i -= 1
    i = 2
def spin_left():
    global i, bod1, bod2
    while i > 0:
        led.unplot(bod1[0], bod1[1])
        led.unplot(bod2[0], bod2[1])
        bod1[1] -= 2
        bod2[1] -= 1
        led.plot(bod1[0], bod1[1])
        led.plot(bod2[0], bod2[1])
        basic.pause(500)
        i -= 1
    i = 2
def spin_up():
    global i, bod1, bod2
    while i > 0:
        led.unplot(bod1[0], bod1[1])
        led.unplot(bod2[0], bod2[1])
        bod1[0] -= 2
        bod2[0] -= 1
        led.plot(bod1[0], bod1[1])
        led.plot(bod2[0], bod2[1])
        basic.pause(500)
        i -= 1
    i = 2