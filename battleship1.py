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


def ship_placement():
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
        row1, col1 = get_mark(cordinate_ship1)
        ship_1 = put_ships_board(row1, col1, placement_board_1)
        os.system('clear')
        print_board_1(placement_board_1)
    print("Ship size: 2x1")
    cordinate_ship2 = input("Enter a valid cordinate (eg. a2): ")
    while cordinate_ship2 in used_input or cordinate_ship2 not in valid_input:
        print("Enter a valid input!")
        cordinate_ship2 = input("Enter a valid cordinate (eg. a2): ")
    if cordinate_ship2 in valid_input:
        used_input.append(cordinate_ship2)
        row1, col1 = get_mark(cordinate_ship2)
        # TODO: v or h
        # TODO: check if it's valid
        ship_2 = put_ships_board(row1, col1, placement_board_1)
        Vertical_or_Horizontal(ship_2, placement_board_1)
        os.system('clear')
        print_board_1(placement_board_1)

    return ship_1, ship_2


def put_ships_board(row1, col1, placement_board_1):
    placement_board_1 = list(placement_board_1)
    placement_board_1[row1][col1] = "S"
    return placement_board_1


def get_mark(text_cord):
    row1 = text_cord[0]
    col1 = text_cord[1]
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

    return row1, col1


def print_board_1(placement_board_1):

    print('   1  ''   2  ''  3 ''   4 ''   5 ')
    print(' --------------------------')
    print(' |    |    |    |    |    |')
    print('A|', placement_board_1[0][0], ' |', placement_board_1[0][1], ' |', placement_board_1[0][2], ' |', placement_board_1[0][3], ' |', placement_board_1[0][4], ' |')
    print(' |    |    |    |    |    |')
    print(' --------------------------')
    print(' |    |    |    |    |    |')
    print('B|', placement_board_1[1][0], ' |', placement_board_1[1][1], ' |', placement_board_1[1][2], ' |', placement_board_1[1][3], ' |', placement_board_1[1][4], ' |')
    print(' |    |    |    |    |    |')
    print(' --------------------------')
    print(' |    |    |    |    |    |')
    print('C|', placement_board_1[2][0], ' |', placement_board_1[2][1], ' |', placement_board_1[2][2], ' |', placement_board_1[2][3], ' |', placement_board_1[2][4], ' |')
    print(' |    |    |    |    |    |')
    print(' --------------------------')
    print(' |    |    |    |    |    |')
    print('D|', placement_board_1[3][0], ' |', placement_board_1[3][1], ' |', placement_board_1[3][2], ' |', placement_board_1[3][3], ' |', placement_board_1[3][4], ' |')
    print(' |    |    |    |    |    |')
    print(' --------------------------')
    print(' |    |    |    |    |    |')
    print('E|', placement_board_1[4][0], ' |', placement_board_1[4][1], ' |', placement_board_1[4][2], ' |', placement_board_1[4][3], ' |', placement_board_1[4][4], ' |')
    print(' |    |    |    |    |    |')
    print(' --------------------------')


def Vertical_or_Horizontal(ship, placement_board_1):
    print(ship)
    v_h = input("Vertical or Horizontal? (v or h): ").lower()
    if v_h == "v" or "vertical":
        ship[1] += 1
        print(ship)



placement_board_1 = placement_board_1()
print_board_1(placement_board_1)
ship_1, ship_2 = ship_placement()
