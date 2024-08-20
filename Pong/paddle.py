from turtle import Turtle


HEIGHT = 5
WIDTH = 1
MOVING, DRAGGING = range(2)  # states
RIGHT_PADDLE_X = 380
LEFT_PADDLE_X = -380

class Paddle(Turtle):
    def __init__(self, screen_side: str, color):
        super().__init__()
        self.speed("fastest")
        self.screen_side = screen_side
        if screen_side.lower() == "left":
            self.teleport(LEFT_PADDLE_X, 0)
        else:
            self.teleport(RIGHT_PADDLE_X, 0)
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.width = WIDTH * 20
        self.height = HEIGHT * 20
        self.penup()
        self.is_player = False
    
    def control(self, screen):
        self.is_player = True
        def move_handler(y):
            onmove(screen, None)  # avoid overlapping events
            self.penup()
            if self.screen_side.lower() == "left":
                self.goto(LEFT_PADDLE_X, y)
            else:
                self.goto(RIGHT_PADDLE_X, y)
            onmove(screen, move_handler)

        def onmove(self, fun, add=None):
            """
            Bind fun to mouse-motion event on screen.

            Arguments:
            self -- the singular screen instance
            fun  -- a function with two arguments, the coordinates
                of the mouse cursor on the canvas.
            """
            if fun is None:
                self.cv.unbind('<Motion>')
            else:
                def eventfun(event):
                    fun(-self.cv.canvasy(event.y) / self.yscale)

                self.cv.bind('<Motion>', eventfun, add)

        # Initially we track the turtle's motion and left button clicks
        onmove(screen, move_handler)  # a la screen.onmove(move_handler)

    def move(self, ball, move_speed):
        if self.is_player == False:
            ycor = self.ycor()
            if ball.ycor() < ycor:
                ycor -= move_speed
                self.goto(self.xcor(), ycor)
            elif ball.ycor() > ycor:
                ycor += move_speed
                self.goto(self.xcor(), ycor)



        










