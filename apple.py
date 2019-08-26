import random
import constantes

class Apple():
    def __init__(self,x,y):
        self.pos = [x,y]

    def move(self,snake):
        while True:
            self.pos = [
            random.randint(0,constantes.blocks[0]-1),
            random.randint(0,constantes.blocks[1]-1)
            ]
            if self.pos in snake.coords:
                continue
            break


    def insert(self,canvas):
        try:
            canvas.delete(self.image)
        except:
            pass
        self.image = canvas.create_oval(
        self.pos[0] * constantes.block_size_x,
        self.pos[1] * constantes.block_size_y,
        (self.pos[0]+1) * constantes.block_size_x,
        (self.pos[1]+1) * constantes.block_size_y,
        fill = 'red'
        )
