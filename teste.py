import curses
from random import randint
from curses import wrapper

fruit = ()
fruitIsAlive = False
exit = ord("q")
snake = [(10,20)]

def fruitgen(lastSeg, win, y, x):
    global fruitIsAlive
    global fruit
    global snake
    if snake[0] == fruit:
        fruitIsAlive = False
        win.addstr(fruit[0], fruit[1], " ")
        fruit = ()
        segments = (lastSeg[0], lastSeg[1])
        snake.append(segments)
    if fruitIsAlive is False:
        fruit = (randint(5, y -5), randint(5, x -5))
        fruitIsAlive = True

def main(win):
    winy, winx = win.getmaxyx()
    win.keypad(True)
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    curses.halfdelay(1)
    key = curses.KEY_RIGHT
    direction = key
    while(key != exit):
        win.clear()
        win.border()
        if fruitIsAlive == True:
            win.addstr(fruit[0], fruit[1], "*")
        for seg in range(len(snake)):
            win.addstr(snake[seg][0], snake[seg][1], "#")
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
        fruitgen(last, win, winy, winx)

        if snake[0] in snake[1:]:
            break

wrapper(main)