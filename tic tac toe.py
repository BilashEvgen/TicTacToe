import turtle as t
screen = t.Screen()
t.speed(0)
t.ht()

game_over = False
list_of_y = [150, 50, -50]
list_of_x = [-150, -50, 50]
status_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
all = [[-150, 150], [-50, 150], [50, 150], [-150, 50], [-50, 50], [50, 50], [-150, -50], [-50, -50], [50, -50]]
list_of_victory = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
turn = 1

x1 = -150
y1 = -150

def drow_line(startindex, endindex):
    if endindex - startindex == 2:
        start_x = all[startindex][0]
        start_y = all[startindex][1] - 50
        end_x = all[endindex][0] + 100
        end_y = all[endindex][1] - 50
        
    elif endindex - startindex == 6:
        start_x = all[startindex][0] + 50
        start_y = all[startindex][1]
        end_x = all[endindex][0] + 50
        end_y = all[endindex][1] - 100
        
    elif endindex - startindex == 8:
        start_x = all[startindex][0]
        start_y = all[startindex][1]
        end_x = all[endindex][0] + 100
        end_y = all[endindex][1] - 100
        
    elif endindex - startindex == 4:
        start_x = all[startindex][0] + 100
        start_y = all[startindex][1]
        end_x = all[endindex][0]
        end_y = all[endindex][1] - 100
    
    t.pu()
    t.goto(start_x, start_y)
    t.pd()
    t.goto(end_x, end_y)

def chek_draw():
    global game_over
    draw = True
    
    for elem in status_list:
        if elem == 0:
            draw = False
    
    if draw == True:
        t.pu()
        t.goto(0, 200)
        t.write(arg="Нічия", align="center", font=["Arial", 24, "normal"], move = True)
        game_over = True

def check_victory():
    global game_over
    
    for victory in list_of_victory:
        if status_list[victory[0]] == status_list[victory[1]] == status_list[victory[2]]:
            if status_list[victory[0]] != 0:
                game_over = True
                drow_line(startindex=victory[0], endindex=victory[2])
                t.pu()
                t.goto(0, 200)
                t.write(arg="Переміг гравець №", align="center", font=["Arial", 24, "normal"], move = True)
                t.pd()
                if turn == 1:
                    t.color("red")
                    t.write("1", font=["Arial", 24, "normal"])
                elif turn == 2:
                    t.color("blue")
                    t.write("2", font=["Arial", 24, "normal"])
    
    if game_over == False:
        chek_draw()

def paint_square():
    
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    
    i = 0
    while i < 4:
        t.fd(100)
        t.left(90)
        i += 1

def print_x(x, y):
    t.width(5)
    t.color("red")
    t.pu()
    t.goto(x, y)
    t.pd()
    t.goto(x + 100, y - 100)
    t.pu()
    t.goto(x + 100, y)
    t.pd()
    t.goto(x, y - 100)
    t.color("black")

def print_o(x, y):
    t.width(5)
    t.color("blue")
    t.pu()
    t.goto(x + 50, y - 100)
    t.pd()
    t.circle(50)
    t.color("black")

def click(x: float, y: float):
    global turn
    
    if game_over == False:
        i = 0
        for cory in list_of_y:
            if cory > y and y > cory - 100:
                for corx in list_of_x:
                    if corx < x and x < corx + 100:
                        for el in all:
                            if el[0] == corx:
                                if el[1] == cory:
                                    if status_list[i] == 0:
                                        if turn == 1:
                                            print_x(corx, cory)
                                            status_list[i] = 1
                                            check_victory()
                                            turn = 2
                                        elif turn == 2:
                                            print_o(corx, cory) 
                                            status_list[i] = 2
                                            check_victory()
                                            turn = 1
                            i += 1

q = 0
while q < 3:
    w = 0
    while w < 3:
        paint_square()
        x1 += 100
        w += 1
    x1 = -150
    y1 += 100
    q += 1

screen.onscreenclick(click)
screen.mainloop()