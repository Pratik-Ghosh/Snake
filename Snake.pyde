#setup our constants that we use throughout our code
global SQUARESIZE, WIDTH, HEIGHT
SQUARESIZE = 20
WIDTH = 40
HEIGHT = 30

class Snake(object):
    #initialise the snake object, setup the x,y coordinates
    # we use a PVector to store the x,y coords
    # snake objects have the attributes 'body' and 'direction'
    def __init__(self):
        x = int(random(0,WIDTH))
        y = int(random(0,HEIGHT))
        self.body = []
        self.body.append(PVector(x,y))
        self.body.append(PVector(x+1,y))
        self.body.append(PVector(x+1,y+1))
        self.body.append(PVector(x+1,y+2))
        self.body.append(PVector(x+1,y+3))
        self.body.append(PVector(x+2,y+3))
        self.direction = None
        self.addsegments = 0 
    # draw a square at the correct x,y coords to
    # represent the snake body
    def draw(self):
        fill("#24FF25")
        for segment in self.body:
            rect(SQUARESIZE * segment.x,
                 SQUARESIZE * segment.y,
                 SQUARESIZE, SQUARESIZE)
    
    #changes the direction that the snake is traveling
    #checks that the new direction is VALID
    #if the new direction is not valid, nothing will happen
    def change_direction(self, direction):
        if direction == UP and self.direction != DOWN:
            self.direction = UP
        elif direction == DOWN and self.direction != UP:
            self.direction = DOWN
        elif direction == LEFT and self.direction != RIGHT:
            self.direction = LEFT
        elif direction == RIGHT and self.direction != LEFT:
            self.direction = RIGHT
    
    # updates the snake location depending on the direction
    def update(self):
        #check the direction and update the PVector coords
        # e.g. if direction == UP, subtract 1 from y coord
        
        #set the variable head equal to the first PVector
        head = self.body[0]
        
        if self.direction == UP:
            new_head = PVector(head.x, head.y - 1) #store new head location
            self.body.insert(0, new_head) # insert new head
            if self.addsegments > 0:
                self.addsegments -= 1 
            else:
                self.body.pop(-1)
        elif self.direction == DOWN:
            new_head = PVector(head.x, head.y + 1)
            self.body.insert(0, new_head) # insert new head
            if self.addsegments > 0:
                self.addsegments -= 1 
            else:
                self.body.pop(-1)
        elif self.direction == LEFT:
            new_head = PVector(head.x - 1, head.y)
            self.body.insert(0, new_head) # insert new head
            if self.addsegments > 0:
                self.addsegments -= 1 
            else:
                self.body.pop(-1)
        elif self.direction == RIGHT:
            new_head = PVector(head.x + 1, head.y)
            self.body.insert(0, new_head) # insert new head
            if self.addsegments > 0:
                self.addsegments -= 1 
            else:
                self.body.pop(-1)
        
    def check_out_of_bounds(self):
        pass
    def check_self_collision(self):
        head = self.body[0]
        for i in range(1, len(self.body)):
            if head == self.body[i]:
                return True
            return False 
            
    def extend_length():
        pass

class Target(object):
    def __init__(self):
        self.position = PVector(int(random(0,40)), int(random(0,30)))
    def draw(self):
        fill(255,255,255)
        # x, y, w, h
        rect(self.position.x*SQUARESIZE, self.position.y*SQUARESIZE, SQUARESIZE, SQUARESIZE)
    def change_position(self):
        self.position = PVector(int(random(0,40)), int(random(0,30)))
    def check_for_snake_collision(self,snake):
        head = snake.body[0] 
        if head == self.position:
            snake.addsegments += 1
            return True
        return False 




def setup():
    global snake, target
    size(SQUARESIZE * WIDTH, SQUARESIZE * HEIGHT) #create the grid window
    background(0) #set black bg
    snake = Snake() #create snake object
    frameRate(30) #slow down the fps to 30
    target = Target()
    
def draw():
    global snake, target , gameover
    
    background(0) #clear the entire screen
    snake.draw() #draw the snake in its current location
    snake.update() #update the location of the snake
    target.draw()
    if target.check_for_snake_collision(snake):
        target.change_position()
    if snake.check_self_collision():
        gameover = True 
    frameRate(10)
# respond to any keyboard presses by sending the key pressed
#   to the method change_direction
def keyPressed():
    if keyCode==UP or keyCode==DOWN or keyCode==LEFT or keyCode==RIGHT:
        snake.change_direction(keyCode)




    
    
    
    
