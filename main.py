while True:
    try:
        if not snake.dead:
            break
    except:
        pass

    import tkinter
    import time
    import constantes
    import snake
    import apple


    keys = []
    cheat = False

    def score():
        tscore.config(state=tkinter.NORMAL)
        tscore.delete('1.0',tkinter.END)
        tscore.insert(tkinter.END,'score is {}'.format(len(snake.body)-2))
        tscore.config(state = tkinter.DISABLED)

    def execute(*args):
        pre_key = 'w'
        binds = {
        'a':snake.move_left,
        'w':snake.move_up,
        's':snake.move_down,
        'd':snake.move_right
        }

        while True:
            if snake.dead :
                break
            snake.check_lost()
            score()
            apple.insert(canvas)
            time.sleep(constantes.tscale)
            snake.check_apple(apple,cheat)

            ##control the snake
            try:
                binds[keys[-1]]()
                window.update()
                pre_key = keys[-1]
                keys.pop()
            except:
                binds[pre_key]()
                window.update()
            window.update()
        time.sleep(3)
        window.destroy()


    def wkey(*args):
        global keys
        keys.insert(0,'w')

    def akey(*args):
        global keys
        keys.insert(0,'a')

    def skey(*args):
        global keys
        keys.insert(0,'s')

    def dkey(*args):
        global keys
        keys.insert(0,'d')

    def grow_cheat(*args):
        global cheat
        cheat = True

    def d_grow_cheat(*args):
        global cheat
        cheat = False


    ##create window
    window = tkinter.Tk()
    window.title('Snake game')

    ##create Canvas
    canvas = tkinter.Canvas(window,width = constantes.width , height = constantes.height,bg = 'green')
    canvas.grid()

    ##scoreboard
    tscore = tkinter.Text(window, width = 20 ,height = 1)
    tscore.grid(row = 1,column = 0)

    ##create snake and apple
    snake = snake.Snake(int(constantes.blocks[0]/2),int(constantes.blocks[0]/2),canvas = canvas)
    apple = apple.Apple(1,1)
    apple.move(snake)
    apple.insert(canvas)
    snake.insert()
    ##key binds
    window.bind("<Return>",execute)
    # window.bind("<Key>", input)
    window.bind("<Up>", wkey)
    window.bind("<Left>",akey)
    window.bind("<Right>",dkey)
    window.bind("<Down>",skey)
    window.bind("<Shift-Up>",grow_cheat)
    window.bind("<Shift-Down>",d_grow_cheat)

    window.mainloop()
