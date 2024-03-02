
def triangle_area(height, length):
    return height*length/2

if __name__ == '__main__':
    height = input("Podaj wysokość: ")
    lenght = input("Podaj długość: ")
    print("Pole trójkąta:" + str(triangle_area(int(height), int(lenght))))



