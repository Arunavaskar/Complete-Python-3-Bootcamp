print("                          \n\n¸„.-•~¹°”ˆ˜¨ Tic-Tac-Toe ¨˜ˆ”°¹~•-.„¸\n\n")

###### MARKER ONE
player_one = input("Player 1, State Your Name: ")
player_two = input("Player 2, State Your Name: ")
print(f'Hello {player_one} and {player_two}!\nLet us begin by choosing your unique markers..')
while True:
    playerone_marker = input(f"{player_one}, as Player 1 you get to choose your marker first.. 'X or O': ")


    if playerone_marker.lower() == "x":
        #print(marker)
        break

    elif  playerone_marker.lower() == "o":
        #print(marker)
        break
    #elif marker == "quite":
        #print("quited!")
        #break
    else:
        print("You need to choose between X or O\nTry Again!")
        continue

#MARKER TWO
playertwo_marker = ""
if playerone_marker == "x":
    playertwo_marker = "o"
elif playerone_marker == "o":
    playertwo_marker = "x"

print(f"So {player_two}, your marker is ",playertwo_marker)


board = """
      ░▒▓█  1           |2           |3
                        |            |    
                        |            |           
            ------------|------------|------------
            4           |5           |6
                        |            |    
                        |            |           
            ------------|------------|------------
            7           |8           |9
                        |            |    
                        |            |            █▓▒░

"""

print("\nHere is the Classic Tic-Tac-Toe board\n", board)
print("Rules are simple but attempted in a different way!\nDon't worry, it's no big deal.")
print("Each cell here is represented by there serial number.\nSo you will be asked to enter your desired position from the board to place your mark.")

########################################################################

B = {1: "a",2: "b",3: "c",4: "d",5: "e",6: "f",7: "g",8: "h",9: "i"}
blank_B = {1: "            ",2: "            ",3: "            ",4: "            ",5: "            ",6: "            ",7: "            ",8: "            ",9: "            "}

while True:
    while True:

        playerone_position = int(input(f"{player_one}, enter the position you want, from 1 to 9: "))
        if playerone_position in range(1,10):
            break
        else:
            print("You need to choose from 1 to 9, Try Again!")
            continue
    for key, value in B.items():
        if key == playerone_position:
            #blank_B[key] = "      "+marker+"     "
            if value == playertwo_marker:
                continue
            else:
                blank_B[key] = "      "+playerone_marker+"     "

    print(f"""
        1           |2           |3
        {blank_B[1]}|{blank_B[2]}|{blank_B[3]} 
                    |            |
        ------------|------------|------------
        4           |5           |6
        {blank_B[4]}|{blank_B[5]}|{blank_B[6]}
                    |            |
        ------------|------------|------------
        7           |8           |9
        {blank_B[7]}|{blank_B[8]}|{blank_B[9]}
                    |            |
    """) 
    
    if blank_B[1].lower() == blank_B[5].lower() == blank_B[9].lower() == "      x     ":
        print(f"{player_one} wins\n")
        print( """       
        1   X       |2           |3
              X     |            |            
                 X  |            |
        ------------|------------|------------
        4           |5  X        |6
                    |      X     |            
                    |         X  |
        ------------|------------|------------
        7           |8           |9  X
                    |            |     X      
                    |            |        X
                    """)
        break
    elif blank_B[1].lower() == blank_B[5].lower() == blank_B[9].lower() == "      o     ":
        print(f"{player_one} wins\n")
        print( """       
        1   O       |2           |3
              O     |            |            
                 O  |            |
        ------------|------------|------------
        4           |5  O        |6
                    |      O     |            
                    |         O  |
        ------------|------------|------------
        7           |8           |9  O
                    |            |     O      
                    |            |        O
                    """)
        break
    
    elif blank_B[7].lower() == blank_B[5].lower() == blank_B[3].lower() == "      x     ":
        print(f"{player_one} wins\n")
        print( """       
        1           |2           |3      X
                    |            |    X           
                    |            | X
        ------------|------------|------------
        4           |5        X  |6
                    |      X     |            
                    |  X         |
        ------------|------------|------------
        7         X |8           |9   
               X    |            |           
            X       |            |        
                    """)
        break
    elif blank_B[7].lower() == blank_B[5].lower() == blank_B[3].lower() == "      o     ":
        print(f"{player_one} wins\n")
        print( """       
        1           |2           |3      O
                    |            |    O           
                    |            | O
        ------------|------------|------------
        4           |5        O  |6
                    |      O     |            
                    |  O         |
        ------------|------------|------------
        7         O |8           |9   
               O    |            |           
            O       |            |        
                    """)
        break
    
    elif blank_B[4].lower() == blank_B[5].lower() == blank_B[6].lower() == "      x     ":
        print(f"{player_one} wins\n")
        print( """       
        1           |2           |3       
                    |            |                
                    |            |  
        ------------|------------|------------
        4           |5           |6
         X   X  X   |  X   X  X  |  X   X  X              
                    |            |
        ------------|------------|------------
        7           |8           |9   
                    |            |           
                    |            |        
                    """)
        break
    elif blank_B[4].lower() == blank_B[5].lower() == blank_B[6].lower() == "      o     ":
        print(f"{player_one} wins\n")
        print( """       
        1           |2           |3       
                    |            |                
                    |            |  
        ------------|------------|------------
        4           |5           |6
         O   O  O   |  O   O  O  |  O   O  O              
                    |            |
        ------------|------------|------------
        7           |8           |9   
                    |            |           
                    |            |        
                    """)
        break
    
    elif blank_B[2].lower() == blank_B[5].lower() == blank_B[8].lower() == "      x     ":
        print(f"{player_one} wins\n")
        print( """       
        1           |2    X      |3       
                    |     X      |                
                    |     X      |  
        ------------|------------|------------
        4           |5    X      |6
                    |     X      |               
                    |     X      |
        ------------|------------|------------
        7           |8    X      |9   
                    |     X      |           
                    |     X      |        
                    """)
        break
    elif blank_B[2].lower() == blank_B[5].lower() == blank_B[8].lower() == "      o     ":
        print(f"{player_one} wins\n")
        print( """       
        1           |2    O      |3       
                    |     O      |                
                    |     O      |  
        ------------|------------|------------
        4           |5    O      |6
                    |     O      |               
                    |     O      |
        ------------|------------|------------
        7           |8    O      |9   
                    |     O      |           
                    |     O      |        
                    """)
        break
    elif blank_B[1].lower() == blank_B[2].lower() == blank_B[3].lower() == "      x     ":
        print(f"{player_one} wins\n")
        break

    elif blank_B[1].lower() == blank_B[2].lower() == blank_B[3].lower() == "      o     ":
        print(f"{player_one} wins\n")
        break

    elif blank_B[3].lower() == blank_B[6].lower() == blank_B[9].lower() == "      x     ":
        print(f"{player_one} wins\n")
        break

    elif blank_B[3].lower() == blank_B[6].lower() == blank_B[9].lower() == "      o     ":
        print(f"{player_one} wins\n")
        break

    elif blank_B[9].lower() == blank_B[8].lower() == blank_B[7].lower() == "      x     ":
        print(f"{player_one} wins\n")
        break

    elif blank_B[9].lower() == blank_B[8].lower() == blank_B[7].lower() == "      o     ":
        print(f"{player_one} wins\n")
        break

    elif blank_B[7].lower() == blank_B[4].lower() == blank_B[1].lower() == "      x     ":
        print(f"{player_one} wins\n")
        break

    elif blank_B[7].lower() == blank_B[4].lower() == blank_B[1].lower() == "      o     ":
        print(f"{player_one} wins\n")
        break


    while True:

        playertwo_position = int(input(f"{player_two}, enter the position you want, from 1 to 9: "))
        if playertwo_position in range(1,10):
            break
        else:
            print("You need to choose from 1 to 9, Try Again!")
            continue
    for key, value in B.items():
        if key == playertwo_position:
            #blank_B[key] = "      "+marker+"     "
            if value == playerone_marker:
                continue
            else:
                blank_B[key] = "      "+playertwo_marker+"     "
    print(f"""
        1           |2           |3
        {blank_B[1]}|{blank_B[2]}|{blank_B[3]}
                    |            |
        ------------|------------|------------
        4           |5           |6
        {blank_B[4]}|{blank_B[5]}|{blank_B[6]}
                    |            |
        ------------|------------|------------
        7           |8           |9
        {blank_B[7]}|{blank_B[8]}|{blank_B[9]}
                    |            |
    """)

    if blank_B[1].lower() == blank_B[5].lower() == blank_B[9].lower() == "      x     ":
        print(f"{player_two} wins\n")
        print( """       
        1   X       |2           |3
              X     |            |            
                 X  |            |
        ------------|------------|------------
        4           |5  X        |6
                    |      X     |            
                    |         X  |
        ------------|------------|------------
        7           |8           |9  X
                    |            |     X      
                    |            |        X
                    """)
        break
    elif blank_B[1].lower() == blank_B[5].lower() == blank_B[9].lower() == "      o     ":
        print(f"{player_two} wins\n")
        print( """       
        1   O       |2           |3
              O     |            |            
                 O  |            |
        ------------|------------|------------
        4           |5  O        |6
                    |      O     |            
                    |         O  |
        ------------|------------|------------
        7           |8           |9  O
                    |            |     O      
                    |            |        O
                    """)
        break
    
    elif blank_B[7].lower() == blank_B[5].lower() == blank_B[3].lower() == "      x     ":
        print(f"{player_two} wins\n")
        print( """       
        1           |2           |3      X
                    |            |    X           
                    |            | X
        ------------|------------|------------
        4           |5        X  |6
                    |      X     |            
                    |  X         |
        ------------|------------|------------
        7         X |8           |9   
               X    |            |           
            X       |            |        
                    """)
        break
    elif blank_B[7].lower() == blank_B[5].lower() == blank_B[3].lower() == "      o     ":
        print(f"{player_two} wins\n")
        print( """       
        1           |2           |3      O
                    |            |    O           
                    |            | O
        ------------|------------|------------
        4           |5        O  |6
                    |      O     |            
                    |  O         |
        ------------|------------|------------
        7         O |8           |9   
               O    |            |           
            O       |            |        
                    """)
        break
    
    elif blank_B[4].lower() == blank_B[5].lower() == blank_B[6].lower() == "      x     ":
        print(f"{player_two} wins\n")
        print( """       
        1           |2           |3       
                    |            |                
                    |            |  
        ------------|------------|------------
        4           |5           |6
         X   X  X   |  X   X  X  |  X   X  X              
                    |            |
        ------------|------------|------------
        7           |8           |9   
                    |            |           
                    |            |        
                    """)
        break
    elif blank_B[4].lower() == blank_B[5].lower() == blank_B[6].lower() == "      o     ":
        print(f"{player_two} wins\n")
        print( """       
        1           |2           |3       
                    |            |                
                    |            |  
        ------------|------------|------------
        4           |5           |6
         O   O  O   |  O   O  O  |  O   O  O              
                    |            |
        ------------|------------|------------
        7           |8           |9   
                    |            |           
                    |            |        
                    """)
        break
    
    elif blank_B[2].lower() == blank_B[5].lower() == blank_B[8].lower() == "      x     ":
        print(f"{player_two} wins\n")
        print( """       
        1           |2    X      |3       
                    |     X      |                
                    |     X      |  
        ------------|------------|------------
        4           |5    X      |6
                    |     X      |               
                    |     X      |
        ------------|------------|------------
        7           |8    X      |9   
                    |     X      |           
                    |     X      |        
                    """)
        break
    elif blank_B[2].lower() == blank_B[5].lower() == blank_B[8].lower() == "      o     ":
        print(f"{player_two} wins\n")
        print( """       
        1           |2    O      |3       
                    |     O      |                
                    |     O      |  
        ------------|------------|------------
        4           |5    O      |6
                    |     O      |               
                    |     O      |
        ------------|------------|------------
        7           |8    O      |9   
                    |     O      |           
                    |     O      |        
                    """)
        break
    elif blank_B[1].lower() == blank_B[2].lower() == blank_B[3].lower() == "      x     ":
        print(f"{player_one} wins\n")
        break

    elif blank_B[1].lower() == blank_B[2].lower() == blank_B[3].lower() == "      o     ":
        print(f"{player_one} wins\n")
        break

    elif blank_B[3].lower() == blank_B[6].lower() == blank_B[9].lower() == "      x     ":
        print(f"{player_one} wins\n")
        break

    elif blank_B[3].lower() == blank_B[6].lower() == blank_B[9].lower() == "      o     ":
        print(f"{player_one} wins\n")
        break

    elif blank_B[9].lower() == blank_B[8].lower() == blank_B[7].lower() == "      x     ":
        print(f"{player_one} wins\n")
        break

    elif blank_B[9].lower() == blank_B[8].lower() == blank_B[7].lower() == "      o     ":
        print(f"{player_one} wins\n")
        break

    elif blank_B[7].lower() == blank_B[4].lower() == blank_B[1].lower() == "      x     ":
        print(f"{player_one} wins\n")
        break

    elif blank_B[7].lower() == blank_B[4].lower() == blank_B[1].lower() == "      o     ":
        print(f"{player_one} wins\n")
        break
