from tkinter import *
import time
from tkinter import messagebox

GAME_WIDTH = 800
GAME_HEIGHT = 600
PADDLE_SPEED = 20
BALL_SIZE = 20
BALL_SPEED = 5
PADDLE_COLOR = "green"
BALL_COLOR = "red"
BACKGROUND_COLOR = "black"
pressedStatus = {"Up": False, "Down": False, "w": False, "s": False, "W": False, "S": False}


class Ball:

    def __init__(self, canvas, paddle, paddle2):
        self.canvas = canvas
        self.ball = self.canvas.create_oval(400, 300, 400 + BALL_SIZE, 300 + BALL_SIZE, fill=BALL_COLOR, tag="ball")
        self.w = BALL_SPEED
        self.w1 = -BALL_SPEED
        self.paddle = paddle
        self.paddle2 = paddle2

    def collision(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.paddle)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def collision2(self, pos):
        paddle2_pos = self.canvas.coords(self.paddle2.paddle2)

        if pos[2] >= paddle2_pos[0] and pos[0] <= paddle2_pos[2]:
            if pos[3] >= paddle2_pos[1] and pos[3] <= paddle2_pos[3]:
                return True
            return False

    def move_ball(self):

        self.canvas.move(self.ball, self.w, self.w1)
        pos = self.canvas.coords(self.ball)

        if pos[0] <= 0:
            global b_score
            b_score += 1
            score_label_b.config(text="Score B : " + str(b_score))
            self.canvas.coords(self.ball, 400, 300, 400 + BALL_SIZE, 300 + BALL_SIZE)
            self.w = BALL_SPEED
            time.sleep(1)

        if pos[2] >= GAME_WIDTH:
            global a_score
            a_score += 1
            score_label_a.config(text="Score A : " + str(a_score))

            self.canvas.coords(self.ball, 400, 300, 400 + BALL_SIZE, 300 + BALL_SIZE)
            self.w = -BALL_SPEED
            time.sleep(1)

        if pos[1] <= 0:
            self.w1 = BALL_SPEED

        if pos[3] >= GAME_HEIGHT:
            self.w1 = -BALL_SPEED

        if self.collision(pos):
            self.w = BALL_SPEED

        if self.collision2(pos):
            self.w = -BALL_SPEED


class Paddle:

    def __init__(self, canvas):

        self.canvas = canvas
        self.paddle = self.canvas.create_rectangle(0, 400, 25, 260, fill=PADDLE_COLOR, tag="paddle")
        self.canvas.bind('<KeyPress-w>', self.pressed_up)
        self.canvas.bind('<KeyPress-W>', self.pressed_up)

        self.canvas.bind('<KeyRelease-w>', self.released_up)
        self.canvas.bind('<KeyRelease-W>', self.released_up)

        self.canvas.bind('<KeyPress-s>', self.pressed_down)
        self.canvas.bind('<KeyPress-S>', self.pressed_down)

        self.canvas.bind('<KeyRelease-s>', self.released_down)
        self.canvas.bind('<KeyRelease-S>', self.released_down)


    def released_down(self, a):

        pressedStatus["s"] = False
        pressedStatus["S"] = False

    def released_up(self, a):

        pressedStatus["w"] = False
        pressedStatus["W"] = False

    def pressed_up(self, a):

        pressedStatus["w"] = True
        pressedStatus["W"] = True

    def pressed_down(self, a):

        pressedStatus["s"] = True
        pressedStatus["S"] = True

    def up(self):

        self.y = 0
        self.y -= PADDLE_SPEED
        pos = self.canvas.coords(self.paddle)

        if pos[1] <= 0:
            self.y = 0

        if pressedStatus["w"]:
            self.canvas.move(self.paddle, 0, self.y)

    def down(self):

        self.y1 = 0
        self.y1 += PADDLE_SPEED
        pos = self.canvas.coords(self.paddle)

        if pos[3] >= GAME_HEIGHT:
            self.y1 = 0

        if pressedStatus["s"]:
            self.canvas.move(self.paddle, 0, self.y1)


class Paddle2:

    def __init__(self, canvas):
        self.canvas = canvas
        self.paddle2 = self.canvas.create_rectangle(800, 400, 775, 260, fill=PADDLE_COLOR, tag="paddle")
        self.canvas.bind('<KeyPress-Up>', self.pressed_up)
        self.canvas.bind('<KeyRelease-Up>', self.released_up)

        self.canvas.bind('<KeyPress-Down>', self.pressed_down)
        self.canvas.bind('<KeyRelease-Down>', self.released_down)

    def released_down(self, a):

        pressedStatus["Down"] = False

    def released_up(self, a):

        pressedStatus["Up"] = False

    def pressed_up(self, a):

        pressedStatus["Up"] = True

    def pressed_down(self, a):

        pressedStatus["Down"] = True

    def up(self):

        self.y2 = 0
        self.y2 -= PADDLE_SPEED
        pos = self.canvas.coords(self.paddle2)

        if pos[1] <= 0:
            self.y2 = 0

        if pressedStatus["Up"]:
            self.canvas.move(self.paddle2, 0, self.y2)

    def down(self):

        self.y3 = 0
        self.y3 += PADDLE_SPEED
        pos = self.canvas.coords(self.paddle2)

        if pos[3] >= GAME_HEIGHT:
            self.y3 = 0

        if pressedStatus["Down"]:
            self.canvas.move(self.paddle2, 0, self.y3)


def score():
    global a_score
    global b_score

    if a_score >= 10:
        messagebox.showinfo("Game Over", "A wins")
        a_score = 0
        b_score = 0
        score_label_a.config(text="Score A : " + str(a_score))
        score_label_b.config(text="Score B : " + str(b_score))

    if b_score >= 10:
        messagebox.showinfo("Game Over", "B wins")
        b_score = 0
        a_score = 0
        score_label_a.config(text="Score A : " + str(a_score))
        score_label_b.config(text="Score B : " + str(b_score))


window = Tk()
window.resizable(False, False)
window.title("Pong Game")

a_score = 0
b_score = 0

frame = Frame(window, bg="black")
frame.pack(fill=BOTH)

score_label_a = Label(frame, font=('Arial', 20), text="Score A : " + str(a_score), bg="black", fg="white")
score_label_a.grid(row=0, column=0, padx=140)

score_label_b = Label(frame, font=('Arial', 20), text="Score B : " + str(b_score), bg="black", fg="white")
score_label_b.grid(row=0, column=1, padx=100)

canvas = Canvas(window, height=GAME_HEIGHT, width=GAME_WIDTH, bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.pack()
canvas.focus_set()

line = canvas.create_line(400,0,400,600, fill="white", dash=(20,1),width=10)


window.update()

screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()
window_height = window.winfo_height()
window_width = window.winfo_width()

height_mid = int((screen_height - window_height) / 2)
width_mid = int((screen_width - window_width) / 2)

window.geometry("{}x{}+{}+{}".format(window_width, window_height, width_mid, height_mid))

paddle = Paddle(canvas)
paddle2 = Paddle2(canvas)
ball = Ball(canvas, paddle, paddle2)

while True:
    ball.move_ball()
    paddle2.up()
    paddle2.down()
    paddle.up()
    paddle.down()
    score()

    window.update_idletasks()
    window.update()
    time.sleep(0.01)

window.mainloop()
