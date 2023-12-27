print('''
 ,adPPYba, 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba,   
a8P_____88 88P'   "88"    "8a ""     `Y8 88P'    "8a  
8PP""""""" 88      88      88 ,adPPPPP88 88       d8  
"8b,   ,aa 88      88      88 88,    ,88 88b,   ,a8"  
 `"Ybbd8"' 88      88      88 `"8bbdP"Y8 88`YbbdP"'   
                                         88           
                                         88     
''')


line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "️⬜️", "️⬜️"]
line3 = ["⬜️", "️⬜️", "️⬜️"]


map = [line1, line2, line3]
print("Hodding your treasure! X makes the sports.")

# Insert the position of X
position = input("Position: ")
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")