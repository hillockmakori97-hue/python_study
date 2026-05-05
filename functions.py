def hello():
    print('hello Alex')
#calling
hello

def triangle_area():
    base=10
    height=20
    area=0.5*base*height
    print(area)
triangle_area()
hello()



#area of triangle
def area_triange(length,width):
    area=length*width
    print(area)


def even_number(number):
    if number%2==0:
        res="even"
    else:
        res="Odd"
    return res


even_number(9)
