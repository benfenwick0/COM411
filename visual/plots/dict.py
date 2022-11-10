import matplotlib.pyplot as plt
import random

def data():
    paths = {}
    line_style = input("which input (:, -- or -)? ")
    colour = input("which colour (r, g or b)? ")
    marker_style = input("which style (o, s or ^)? ")
    paths['line_style'] = line_style
    paths['colour'] = colour
    paths['marker_style'] = marker_style

    return paths

def generate():
    print("how many lines would you like to display?")
    number = int(input())

    for number in range(number):
        values = data()
        x = random.sample(range(1, 10), 5)
        y = random.sample(range(1, 10), 5)
        format = f"{values['colour']}{values['line_style']}{values['marker_style']}"
        plt.plot(x, y, format)

    plt.show()

def run():
    print("Running...")
    generate()
    print("Done")

run()


