import os
import time
os.system('clear')


def placement_board_1():
    placement_board_1 = [
        #0 #1 #2 #3 #4
        [0, 0, 0, 0, 0],  # row 0
        [0, 0, 0, 0, 0],  # row 1
        [0, 0, 0, 0, 0],  # row 2
        [0, 0, 0, 0, 0],  # row 3
        [0, 0, 0, 0, 0]]  # row 4
    return placement_board_1


def placement_board_2():
    placement_board_2 = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]
    return placement_board_2


def ship_placement_1(placement_board_1):
    valid_input = [
                    'a1', 'a2', 'a3', 'a4', 'a5',
                    'b1', 'b2', 'b3', 'b4', 'b5',
                    'c1', 'c2', 'c3', 'c4', 'c5',
                    'd1', 'd2', 'd3', 'd4', 'd5',
                    'e1', 'e2', 'e3', 'e4', 'e5']

    used_input = []
    print("Ship size: 1x1")
    cordinate_ship1 = input("Enter a valid cordinate (eg. a2): ")
    while cordinate_ship1 not in valid_input:
        print("Enter a valid input!")
        cordinate_ship1 = input("Enter a valid cordinate (eg. a2): ")
    if cordinate_ship1 in valid_input:
        used_input.append(cordinate_ship1)
    print("Ship size: 2x1")
    cordinate_ship2 = input("Enter a valid cordinate (eg. a2): ")
    while cordinate_ship2 in used_input or cordinate_ship2 not in valid_input:
        print("Enter a valid input!")
        cordinate_ship2 = input("Enter a valid cordinate (eg. a2): ")
    if cordinate_ship2 in valid_input:
        used_input.append(cordinate_ship2)
    ships_cord = used_input
    return ships_cord


def ship_placement_2(placement_board_2):
    valid_input = [
                    'a1', 'a2', 'a3', 'a4', 'a5',
                    'b1', 'b2', 'b3', 'b4', 'b5',
                    'c1', 'c2', 'c3', 'c4', 'c5',
                    'd1', 'd2', 'd3', 'd4', 'd5',
                    'e1', 'e2', 'e3', 'e4', 'e5']
    used_input = []
    print("Ship size: 1x1")
    cordinate_ship1 = input("Enter a valid cordinate (eg. a2): ")
    while cordinate_ship1 not in valid_input:
        print("Enter a valid input!")
        cordinate_ship1 = input("Enter a valid cordinate (eg. a2): ")
    if cordinate_ship1 in valid_input:
        used_input.append(cordinate_ship1)
    print("Ship size: 2x1")
    cordinate_ship2 = input("Enter a valid cordinate (eg. a2): ")
    while cordinate_ship2 in used_input or cordinate_ship2 not in valid_input:
        print("Enter a valid input!")
        cordinate_ship2 = input("Enter a valid cordinate (eg. a2): ")
    if cordinate_ship2 in valid_input:
        used_input.append(cordinate_ship2)

    cord_1 = []
    for character in cordinate_ship1:
        cord_1 += character
    row1 = cord_1[0]
    col1 = cord_1[1]
    if row1 == 'a':
        row1 = 0
    elif row1 == 'b':
        row1 = 1
    elif row1 == 'c':
        row1 = 2
    elif row1 == 'd':
        row1 = 3
    elif row1 == 'e':
        row1 = 4
    if col1 == '1':
        col1 = 0
    elif col1 == '2':
        col1 = 1
    elif col1 == '3':
        col1 = 2
    elif col1 == '4':
        col1 = 3
    elif col1 == '5':
        col1 = 4

    cord_2 = []
    for character in cordinate_ship2:
        cord_2 += character
    row2 = cord_2[0]
    col2 = cord_2[1]
    if row2 == 'a':
        row2 = 0
    elif row2 == 'b':
        row2 = 1
    elif row2 == 'c':
        row2 = 2
    elif row2 == 'd':
        row2 = 3
    elif row2 == 'e':
        row2 = 4
    if col2 == '1':
        col2 = 0
    elif col2 == '2':
        col2 = 1
    elif col2 == '3':
        col2 = 2
    elif col2 == '4':
        col2 = 3
    elif col2 == '5':
        col2 = 4


def get_mark(ships_cord):

    cord_1 = []
    for character in ships_cord[0]:
        cord_1 += character
    row1 = cord_1[0]
    col1 = cord_1[1]
    if row1 == 'a':
        row1 = 0
    elif row1 == 'b':
        row1 = 1
    elif row1 == 'c':
        row1 = 2
    elif row1 == 'd':
        row1 = 3
    elif row1 == 'e':
        row1 = 4
    if col1 == '1':
        col1 = 0
    elif col1 == '2':
        col1 = 1
    elif col1 == '3':
        col1 = 2
    elif col1 == '4':
        col1 = 3
    elif col1 == '5':
        col1 = 4

    cord_2 = []
    for character in ships_cord[1]:
        cord_2 += character
    row2 = cord_2[0]
    col2 = cord_2[1]
    if row2 == 'a':
        row2 = 0
    elif row2 == 'b':
        row2 = 1
    elif row2 == 'c':
        row2 = 2
    elif row2 == 'd':
        row2 = 3
    elif row2 == 'e':
        row2 = 4
    if col2 == '1':
        col2 = 0
    elif col2 == '2':
        col2 = 1
    elif col2 == '3':
        col2 = 2
    elif col2 == '4':
        col2 = 3
    elif col2 == '5':
        col2 = 4

    ship1 = row1, col1
    ship2 = row2, col2
    return ship1, ship2


placement_board_1 = placement_board_1()
ships_cord = ship_placement_1(placement_board_1)
ship1, ship2 = get_mark(ships_cord)
print(ship1)
print(ship2)
