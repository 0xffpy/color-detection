import tkinter as tk
from PIL import ImageTk, Image
from functools import partial

import numpy as np


def genrating_ranodm_color():
    # R, G, B
    return np.array((np.random.randint(0, 255, dtype=np.uint8), np.random.randint(0, 255, dtype=np.uint8),
                     np.random.randint(0, 255, dtype=np.uint8)))


# now displaying the color
def labeling_color(r, g, b):
    array = np.full(shape=(300, 300, 3), fill_value=[r, g, b])
    return array


def create_image(r, g, b):
    numpy_image = labeling_color(r, g, b)
    image = Image.fromarray(numpy_image)
    return ImageTk.PhotoImage(image)


class Node:
    __features: list = None
    __labels: list = None

    def __init__(self):
        self.__features = []
        self.__labels = []

    def add_feature(self, feature):
        self.__features.append(feature)
        print("The rgb values has been added", feature)

    def add_label(self, label):
        self.__labels.append(label)
        print("The label value has been added", label)

    def get_feature(self):
        return self.__features

    def get_labels(self):
        return self.__labels

    def purge(self):
        self.__features = None
        self.__labels = None

    def add_to_file(self):
        file = open("file_trying.txt", "w")
        for i, z in zip(self.__features, self.__labels):
            rgb_values_file = str(i[0]) + "," + str(i[1]) + "," + str(i[2]) + "," + z
            print(rgb_values_file)
            file.write(rgb_values_file+"\n")
        file.close()

    def __str__(self):
        return "".join(["The rgb value is " + i.__str__() + " The label is " + j + "\n" for i, j in
                        zip(self.__features, self.__labels)])


class Board(tk.Tk):
    __color: str = None
    __WIDTH = 1920
    __HEIGHT = 1080
    features_labels: Node = None

    def __init__(self, feature_labels):
        super().__init__()
        self.features_labels = feature_labels
        self.rgb_values = None
        self.title("Data set for colors")
        self.geometry('1920x1080')
        self.config(background="#7d75eb")
        tk.Label(self,
                 text="It is the color color detection",
                 bg="#7d75eb",
                 font=('Helvetica', 50, 'bold italic'),
                 fg="#2e2222").pack(side=tk.TOP)
        self.color_buttons()
        self.image_holder()
        self.destroy_button()
        self.skip_button()

    def image_holder(self):
        # we will create a frame
        self.rgb_values = genrating_ranodm_color()
        image = create_image(self.rgb_values[0], self.rgb_values[1], self.rgb_values[2])
        self.frame = tk.Frame(self,
                              width=500,
                              height=500)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)
        label = tk.Label(self.frame, image=image)
        label.image = image
        label.pack()

    def color_buttons(self):
        width = int(self.__WIDTH / 5)
        height = int(self.__HEIGHT / 10)
        start_height = 800
        start_width = 5
        bottom_blue = tk.Button(self,
                                text="click me if blue",
                                bg="BLUE",
                                command=partial(self.__set_color, "blue"))
        bottom_blue.pack()
        bottom_blue.place(x=5 + width * 0,
                          y=start_height + height * 0)
        bottom_black = tk.Button(self,
                                 text="Click me if black",
                                 bg="BLACK",
                                 command=partial(self.__set_color, "black"))
        bottom_black.pack()
        bottom_black.place(x=5 + width * 1,
                           y=start_height + height * 0)
        bottom_white = tk.Button(self,
                                 text="Click me if white",
                                 bg="WHITE",
                                 command=partial(self.__set_color, "white"))
        bottom_white.pack()
        bottom_white.place(x=5 + width * 2,
                           y=start_height + height * 0)
        bottom_green = tk.Button(self,
                                 text="Click me if green",
                                 bg="GREEN",
                                 command=partial(self.__set_color, "green"))
        bottom_green.pack()
        bottom_green.place(x=5 + width * 3,
                           y=start_height + height * 0)
        bottom_red = tk.Button(self,
                               text="Click me if red",
                               bg="RED",
                               command=partial(self.__set_color, "red"))
        bottom_red.pack()
        bottom_red.place(x=5 + width * 4,
                         y=start_height + height * 0)
        bottom_gray = tk.Button(self,
                                text="Click me if gray",
                                bg="gray",
                                command=partial(self.__set_color, "gray"))
        bottom_gray.pack()
        bottom_gray.place(x=5 + width * 0,
                          y=start_height + height * 1)
        bottom_violet = tk.Button(self,
                                  text="Click me if violet",
                                  bg="PURPLE",
                                  command=partial(self.__set_color, "violet"))
        bottom_violet.pack()
        bottom_violet.place(x=5 + width * 1,
                            y=start_height + height * 1)
        bottom_yellow = tk.Button(self,
                                  text="Click me if yellow",
                                  bg="YELLOW",
                                  command=partial(self.__set_color, "yellow"))
        bottom_yellow.pack()
        bottom_yellow.place(x=5 + width * 2,
                            y=start_height + height * 1)
        bottom_orange = tk.Button(self,
                                  text="Click me if orange",
                                  bg="ORANGE",
                                  command=partial(self.__set_color, "orange"))
        bottom_orange.pack()
        bottom_orange.place(x=5 + width * 3,
                            y=start_height + height * 1)

        bottom_brown = tk.Button(self,
                                 text="Click me if brown",
                                 bg="BROWN",
                                 command=partial(self.__set_color, "brown"))
        bottom_brown.pack()
        bottom_brown.place(x=5 + width * 4,
                           y=start_height + height * 1)

    def __set_color(self, color):
        self.__color = color
        self.features_labels.add_feature(self.rgb_values)
        self.features_labels.add_label(self.__color)
        self.frame = None
        self.image_holder()

    def destroy_button(self):
        destroy_button = tk.Button(self,
                                   text="Click me if your bored",
                                   bg="RED",
                                   command=self.destroy)
        destroy_button.pack()
        destroy_button.place(x=1500,
                             y=self.__HEIGHT / 5)

    def skip_button(self):
        skip_button = tk.Button(self,
                                text="Click to skip",
                                bg="GREEN",
                                command=self.skip)
        skip_button.pack()
        skip_button.place(x=1800,
                          y=self.__HEIGHT/5)

    def skip(self):
        self.image_holder()

    def get_label(self):
        return self.__color

    def destroy(self):
        super().destroy()


if __name__ == "__main__":
    node = Node()
    bord = Board(node)
    bord.mainloop()
    node.add_to_file()
    print(node)
