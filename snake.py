import snake_parts
import constantes

class Snake():
    def __init__(self,x,y,canvas):
        self.canvas = canvas
        self.head = snake_parts.Head(x,y)
        self.body = [snake_parts.Body(x-2,y),snake_parts.Body(x-1,y)]
        self.lenght = len(self.body)
        self.coords = [[self.head.x , self.head.y]]
        self.coords.extend([[b.x,b.y] for b in self.body])
        self.growing = False
        self.dead = False


    def move_up(self):
        self.follow_head()
        self.head.move(x = 0 ,y = -1 ,canvas = self.canvas)

    def move_down(self):
        self.follow_head()
        self.head.move(x = 0 ,y = 1 ,canvas = self.canvas)

    def move_right(self):
        self.follow_head()
        self.head.move(x = 1 ,y = 0 ,canvas = self.canvas)

    def move_left(self):
        self.follow_head()
        self.head.move(x = -1 ,y = 0 ,canvas = self.canvas)


    def follow_head(self):
        self.body.append(snake_parts.Body(self.head.x,self.head.y))
        if self.growing == False:
            self.body[0].delete(canvas = self.canvas)
            del(self.body[0])
        self.body[-1].insert(canvas = self.canvas)


    def insert(self):
        self.head.insert(canvas = self.canvas)
        for b in self.body :
            b.insert(canvas = self.canvas)

    def check_apple(self,apple,cheat):
        if [self.head.x,self.head.y] == apple.pos:
            apple.move(self)
            self.growing = True
        elif not cheat:
            self.growing = False

    def check_lost(self):
        coords = []
        coords.extend([[b.x,b.y] for b in self.body])
        if (not (0<= self.head.x <constantes.blocks[0] and 0<= self.head.y <constantes.blocks[1])) or ([self.head.x, self.head.y] in coords):
            print("you died , score is {}".format(len(self.body)-2))
            self.dead = True
