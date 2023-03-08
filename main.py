import random
import  Curses 

screen = curses.initscr()
curses.curs_set(0)

screen_height,screen_widht = screen.getbegyx()
window = curses.newwin(screen_height, screen_widht,0,0)
window.keypad(1)
window.timeout(100)

snk_x = screen_widht // 4
snk_y = screen_height // 2

Snake = [
    [snk_y , snk_x],
    [snk_y , snk_x-1],
    [snk_y , snk_x-2]
]

food = [screen_height // 2,screen_widht // 2]

window.addch(food[0] , food[1] , curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key   
    if Snake[0][0] in [0 , screen_height] or Snake[0][1] in [0 , screen_widht] or Snake[0] in Snake[1:] :
        curses.endwin() #close
        quit() #Exit

    new_head = [Snake[0][0] , Snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1        
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1        
    

    Snake.insert(0, new_head)
    if Snake[0] ==food:
        food = None
        while food is None:
            New_food = [
                random.randint(1, screen_height-1),
                random.randint(1, screen_widht-1)
            ]
            food = New_food if New_food not in Snake else None
        window.addch(food[0] , food[1] , curses.ACS_PI)
    else:
        tail = Snake.pop()
        window.addch(tail[0],tail[1], ' ')

    window.addch(Snake[0][0] , Snake[0][1] , curses.ACS_CKBOARD)    