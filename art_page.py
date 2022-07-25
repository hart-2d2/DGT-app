from tkinter import *
from PIL import ImageTk, Image


class Main:

    def __init__(self, root):
        self.root = root
        self.root.title = "Artz"
        self.root.geometry("400x600+500+100")
        bg_img = Image.open('img/bg_img.jpg')  # background image
        self.bg_img_resized = bg_img.resize((398, 700))
        self.new_bg_img = ImageTk.PhotoImage(self.bg_img_resized)
        self.main()

    def main(self):
        my_canvas = Canvas(self.root, width=800, height=700, )
        my_canvas.pack(fill=BOTH, expand=True)

        # set image in canvas
        my_canvas.create_image(0, 0, image=self.new_bg_img, anchor="nw", )

        main_frame = Frame(self.root, height=450, width=259, highlightbackground='black', highlightthickness=2)

        main_window = my_canvas.create_window(210, 280, window=main_frame, )

        # adding a image
        mona_lisa_img = Image.open('img/mona_lisa.jpg')  # mona lisa image
        self.mona_lisa_img_resized = mona_lisa_img.resize((250, 250))
        self.mona_lisa_img = ImageTk.PhotoImage(self.mona_lisa_img_resized)
        self.mona_lisa_label = Label(main_frame, image=self.mona_lisa_img)
        self.mona_lisa_label.place(x=0, y=0)

        # adding text
        text_label = Label(main_frame,
                           text=" Welcome To\n No Art Blocks App! ",
                           font=("Bauhaus 93", 17))
        text_label.place(x=22, y=250)

        text_label_2 = Label(main_frame,
                             text="This app is all about overcoming art blocks,"
                                  " \nexplaining what art blocks exactly are,\n"
                                  "and how to get over these slumps ",
                             font=("Bauhaus 93", 9),
                             justify='left',
                             anchor=E)

        text_label_2.place(x=0, y=330)

        button = Button(main_frame, text="Next Page", bg='black', fg='white', justify=CENTER, font=("Bauhaus 93", 14))
        button.place(x=72, y=395)



root = Tk()
obj = Main(root)
root.mainloop()
