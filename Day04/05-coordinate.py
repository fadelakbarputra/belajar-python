row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
coordinate = str(input("Enter coloumn then row: \n"))

x_axis = int(coordinate[0]) - 1
y_axis = int(coordinate[1]) - 1



map[y_axis][x_axis]= 'X'
print(f"{row1}\n{row2}\n{row3}")