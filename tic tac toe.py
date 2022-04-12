import random
import time
from termcolor import colored, cprint

def show_board() :
    for row in game :
        for item in row :
            print(item, end=(" ") )
        print()    


def p1vp2() :
    while True :
        print("Player1")
        while True :
            row = int(input("row :"))
            col = int(input("col :"))
            if game [row][col] == '-' :
                game[row][col] = colored('X','red')
                break
            else :
                print("deghat")
        show_board()
        
        if game[0][0] == colored('X','red') and game[0][1] == colored('X','red') and game[0][2] == colored('X','red') :
            print("Player1 win") 
            break 
        elif game[1][0] == colored('X','red') and game[1][1] == colored('X','red') and game[1][2] == colored('X','red') :
            print("Player1 win") 
            break
        elif game[2][0] == colored('X','red') and game[2][1] == colored('X','red') and game[2][2] == colored('X','red') :
           print("Player1 win")  
           break
        elif game[0][0] == colored('X','red') and game[1][0] == colored('X','red') and game[2][0] == colored('X','red') :
           print("Player1 win")  
           break  
        elif game[0][1] == colored('X','red') and game[1][1] == colored('X','red') and game[2][1] == colored('X','red') :
           print("Player1 win")
           break
        elif game[0][2] == colored('X','red') and game[1][2] == colored('X','red') and game[2][2] == colored('X','red') :
            print("Player1 win")
            break
        elif game[0][0] == colored('X','red') and game[1][1] == colored('X','red') and game[2][2] == colored('X','red') :
            print("Player1 win") 
            break
        elif game[0][2] == colored('X','red') and game[1][1] == colored('X','red') and game[2][0] == colored('X','red') :
          print("Player1 win")
          break
    
        print("Player2")
        while True :
            row = int(input("row :"))
            col = int(input("col :"))
            if game [row][col] == '-' :
                game[row][col] = colored('O','blue')
                break
            else :
                print("deghat")
        show_board()
        if game[0][0] == colored('O','blue') and game[0][1] == colored('O','blue') and game[0][2] == colored('O','blue') :
                print("Player2 win") 
                break 
        elif game[1][0] == colored('O','blue') and game[1][1] == colored('O','blue') and game[1][2] == colored('O','blue') :
            print("Player2 win") 
            break
        elif game[2][0] == colored('O','blue') and game[2][1] == colored('O','blue') and game[2][2] == colored('O','blue') :
           print("Player2 win")  
           break
        elif game[0][0] == colored('O','blue') and game[1][0] == colored('O','blue') and game[2][0] == colored('O','blue') :
           print("Player2 win")  
           break  
        elif game[0][1] == colored('O','blue') and game[1][1] == colored('O','blue') and game[2][1] == colored('O','blue') :
           print("Player2 win")
           break
        elif game[0][2] == colored('O','blue') and game[1][2] == colored('O','blue') and game[2][2] == colored('O','blue') :
            print("Player2 win")
            break
        elif game[0][0] == colored('O','blue') and game[1][1] == colored('O','blue') and game[2][2] == colored('O','blue') :
            print("Player2 win") 
            break
        elif game[0][2] == colored('O','blue') and game[1][1] == colored('O','blue') and game[2][0] == colored('O','blue') :
          print("Player2 win")
          break                 
        

def p1vrand() :
    while True :
        print("Player1")
        while True :
            row = int(input("row :"))
            col = int(input("col :"))
            if game [row][col] == '-' :
                game[row][col] = colored('X','red')
                break
            else :
                print("deghat")
        show_board()
        if game[0][0] == colored('X','red') and game[0][1] == colored('X','red') and game[0][2] == colored('X','red') :
            print("Player1 win") 
            break 
        elif game[1][0] == colored('X','red') and game[1][1] == colored('X','red') and game[1][2] == colored('X','red') :
            print("Player1 win") 
            break
        elif game[2][0] == colored('X','red') and game[2][1] == colored('X','red') and game[2][2] == colored('X','red') :
           print("Player1 win")  
           break
        elif game[0][0] == colored('X','red') and game[1][0] == colored('X','red') and game[2][0] == colored('X','red') :
           print("Player1 win")  
           break  
        elif game[0][1] == colored('X','red') and game[1][1] == colored('X','red') and game[2][1] == colored('X','red') :
           print("Player1 win")
           break
        elif game[0][2] == colored('X','red') and game[1][2] == colored('X','red') and game[2][2] == colored('X','red') :
            print("Player1 win")
            break
        elif game[0][0] == colored('X','red') and game[1][1] == colored('X','red') and game[2][2] == colored('X','red') :
            print("Player1 win") 
            break
        elif game[0][2] == colored('X','red') and game[1][1] == colored('X','red') and game[2][0] == colored('X','red') :
          print("Player1 win")
          break
    
    
        print("computer")
        while True :
            row = random.randint(0,2)
            col = random.randint(0,2)
            if game [row][col] == '-' :
                game[row][col] = colored('O','blue')
                break
            else :
                print("deghat")
        show_board()
        if game[0][0] == colored('O','blue') and game[0][1] == colored('O','blue') and game[0][2] == colored('O','blue') :
                print("Player2 win") 
                break 
        elif game[1][0] == colored('O','blue') and game[1][1] == colored('O','blue') and game[1][2] == colored('O','blue') :
            print("Player2 win") 
            break
        elif game[2][0] == colored('O','blue') and game[2][1] == colored('O','blue') and game[2][2] == colored('O','blue') :
           print("Player2 win")  
           break
        elif game[0][0] == colored('O','blue') and game[1][0] == colored('O','blue') and game[2][0] == colored('O','blue') :
           print("Player2 win")  
           break  
        elif game[0][1] == colored('O','blue') and game[1][1] == colored('O','blue') and game[2][1] == colored('O','blue') :
           print("Player2 win")
           break
        elif game[0][2] == colored('O','blue') and game[1][2] == colored('O','blue') and game[2][2] == colored('O','blue') :
            print("Player2 win")
            break
        elif game[0][0] == colored('O','blue') and game[1][1] == colored('O','blue') and game[2][2] == colored('O','blue') :
            print("Player2 win") 
            break
        elif game[0][2] == colored('O','blue') and game[1][1] == colored('O','blue') and game[2][0] == colored('O','blue') :
          print("Player2 win")
          break                       
        
        
while True :
    
    start = time.time()
    game = [['-','-','-'],
        ['-','-','-'],
        ['-','-','-']]

    show_board()
    print("1 - player 1 with player 2")    
    print("2 - player 1 with computer")  
    
    a = int(input("please insert number :")) 
    
    if a == 1 :
        p1vp2()
         
    elif a == 2 :
        p1vrand()
    
    print("Run Time: " + str( time.time() - start ))        