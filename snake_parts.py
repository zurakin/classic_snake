import constantes


class Part():
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def insert(self,canvas):
        self.image = canvas.create_rectangle(
        constantes.block_to_pixel((self.x , 0))[0],
        constantes.block_to_pixel((0 , self.y))[1],
        constantes.block_to_pixel((self.x+1 , 0))[0],
        constantes.block_to_pixel((0 , self.y+1))[1],
        fill = self.color
        )

    def delete(self,canvas):
        canvas.delete(self.image)



class Head(Part):
    def __init__(self,x,y):
        Part.__init__(self,x,y)
        self.color = 'blue'

    def move(self,x,y,canvas):
        self.x += x
        self.y += y
        canvas.move(
        self.image ,
        constantes.block_to_pixel([x,y])[0] ,
        constantes.block_to_pixel([x,y])[1]
        )



class Body(Part):
    def __init__(self,x,y):
        Part.__init__(self,x,y)
        self.color = 'yellow'
