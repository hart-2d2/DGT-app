from tkinter import *
from PIL import ImageTk, Image


class Main:

    def __init__(self, root):
        self.root = root
        self.root.title = "Artz"
        self.root.geometry("800x700+500+100")
        bg_img = Image.open('img/bg_img.jpg')  # background image
        self.bg_img_resized = bg_img.resize((800, 700))
        self.new_bg_img = ImageTk.PhotoImage(self.bg_img_resized)
        self.main()

    def main(self):
        my_canvas = Canvas(self.root, width=800, height=700)
        my_canvas.pack(fill=BOTH, expand=True)

        # set image in canvas
        my_canvas.create_image(0, 0, image=self.new_bg_img, anchor="nw", )

        main_frame = Frame(self.root, height=450, width=205)
        main_window = my_canvas.create_window(300, 300, window=main_frame)

        # adding a image
        mona_lisa_img = Image.open('img/mona_lisa.jpg') # mona lisa image
        self.mona_lisa_img_resized = mona_lisa_img.resize((200, 250))
        self.mona_lisa_img = ImageTk.PhotoImage(self.mona_lisa_img_resized)
        self.mona_lisa_label = Label(main_frame, image=self.mona_lisa_img)
        self.mona_lisa_label.place(x=0, y=0)

        # adding text
        text_label = Label(main_frame, text=" Explore some ideas that \n will help  you with your \nart block",
                           font=("SourceSerifPro", 10, 'bold'))
        text_label.place(x=0, y=400)


root = Tk()
obj = Main(root)
root.mainloop()
