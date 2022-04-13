stred = [2,2]
ctverec = [[1,0], [2,0], [1,1], [2,1]]
carka_ctverec = [[1,0], [2,0], [1,1], [2,1]]
#šlo by to ještě přepočítávat skrze střed
zrcadlit()

def zobraz():
    
    basic.clear_screen()
    led.plot_brightness(stred[0], stred[1], 150)

    for i in ctverec:
        led.plot(i[0], i[1])

    for e in carka_ctverec:
       led.plot(e[0], e[1])

def zrcadlit():

    for i in range(ctverec.length):

        for e in range(0,2):
            carka_ctverec[i][e] = ctverec[i][e] + 2*(stred[e]-ctverec[i][e]) #vzorec od Kelbasy

    zobraz()

def tlacitko_a():

    ctverec[1][0] += 1
    ctverec[2][1] += 1
    ctverec[3][0] += 1
    ctverec[3][1] += 1

    if(ctverec[3][0] == 5):
        ctverec[1][0] -= 3
        ctverec[2][1] -= 3
        ctverec[3][0] -= 3
        ctverec[3][1] -= 3

    zrcadlit()

input.on_button_pressed(Button.A, tlacitko_a)