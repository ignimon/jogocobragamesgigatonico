import curses
import time
from random import randint
from curses import wrapper

fruit = ()
fruitIsAlive = False
exit = ord("q")
snake = [(10,20)]
score = 0

def fruitgen(lastSeg, win, y, x, key):
    global fruitIsAlive
    global fruit
    global snake
    global score
    if snake[0] == fruit or key == ord("p"):
        fruitIsAlive = False
        win.addstr(fruit[0], fruit[1], " ")
        fruit = ()
        segments = (lastSeg[0], lastSeg[1])
        snake.append(segments)
        score += 1
    if fruitIsAlive is False:
        fruit = (randint(5, y -5), randint(5, x -5))
        fruitIsAlive = True

def main(win):
    #initializes colors
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    winy, winx = win.getmaxyx()
    win.keypad(True)
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    curses.halfdelay(1)
    key = curses.KEY_RIGHT
    direction = key
    while(key != exit):
        win.erase()
        win.border()
        win.addstr(1, 2, "score: ")
        win.addstr(1, 10, str(score))
        if fruitIsAlive == True:
            win.addstr(fruit[0], fruit[1], "@", curses.color_pair(1))
        for seg in range(len(snake)):
            win.addstr(snake[seg][0], snake[seg][1], "#", curses.color_pair(2))
        win.refresh()
        key = win.getch()
        y = snake[0][0]
        x = snake[0][1]
        #in curses, y refers to the row, so going down will increase the y (vice versa).

        if key in [curses.KEY_DOWN, curses.KEY_UP, curses.KEY_LEFT, curses.KEY_RIGHT]:
            direction = key
        if direction == curses.KEY_DOWN:
            y += 1
        if direction == curses.KEY_UP:
            y -= 1
        if direction == curses.KEY_LEFT:
            x -= 1
        if direction == curses.KEY_RIGHT:
            x += 1

        # makes snake move
        last = snake.pop()
        snake.insert(0, (y, x))
        win.addstr(last[0], last[1], " ")
        fruitgen(last, win, winy, winx, key)

        if snake[0] in snake[1:]:
            break
        if snake[0][0] in [winy, 0] or snake[0][1] in [winx, 0]:
            break

    win.erase()
    win.addstr(winy //2, winx //2, "Your final score is: " + str(score))
    win.refresh()
    time.sleep(4)

wrapper(main)