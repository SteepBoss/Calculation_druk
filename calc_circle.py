# Поле запечатки стандартного формата SRA3 450x320mm -> 306x430mm
MAX_PRINT_SIZE = (306, 430)
# Поле подрезки плоттером стандартного формата SRA3 450x320mm -> 296x406mm
MAX_PLOT_A3_SIZE = (296, 406)
MAX_PLOT_A3_SIZE_1 = (296, 406)
MAX_PLOT_A3_SIZE_2 = (296, 406)
# Поле подрезки плоттером стандартного формата SRB3 488x330mm -> 296x406mm 488x330mm -> 280x448mm
MAX_PLOT_B3_SIZE = (284, 452)
# Минимальный размер который может резать стандартный резак Ideal 444

def n_circles_in_rectangle(B: int, L: int, diameter: int, distance: int) -> int:
    radius = diameter / 2
    # diameter = radius*2
    n_circles = 0

    if ((diameter + distance) <= B and (diameter + distance) <= L):
        posX = (diameter / 2)
        posY = (diameter / 2)

        while (posY + radius <= L):
            while (posX + radius <= B):
                n_circles += 1
                posX = posX + (diameter + distance)

            posX = radius
            posY = posY + diameter + distance

    return n_circles
print(n_circles_in_rectangle(*MAX_PLOT_A3_SIZE, diameter=50, distance=4))
