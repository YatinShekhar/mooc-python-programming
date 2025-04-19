def line(integer, string):

    if string == "":
        print("*"*integer)
    else:
        print(string[0]*integer)

def shape(width, triangle_character, height, rectangle_character):

    num = 1
    while num <= width:
        line(num, triangle_character)
        num += 1
    
    num = 1
    while num <= height:
        line(width, rectangle_character)
        num += 1
        

if __name__ == "__main__":
    
    shape(5, "x", 2, "o")
