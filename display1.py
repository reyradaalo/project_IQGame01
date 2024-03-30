from tkinter import *
from PIL import Image, ImageTk

class IQGameApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("IQ Game")
        self.root.geometry("1920x1080")

        bg = Image.open("Web_Photo_Editor.png")
        bg = bg.resize((1920, 1080), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(bg)

        # Background img on label
        self.background_label = Label(self.root, image=self.bg_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame for buttons
        self.button_frame = Frame(self.root, bg="#00FF01")
        self.button_frame.place(relx=0.5, rely=0.9, anchor="center")

        # Button style
        self.button_font = ("Helvetica", 16)
        self.button_padding = 10

        # Buttons
        self.start_button = Button(self.button_frame, text="Start", font=self.button_font, padx=self.button_padding, pady=self.button_padding)
        self.start_button.pack(side="left", padx=20)

        self.restart_button = Button(self.button_frame, text="Restart", font=self.button_font, padx=self.button_padding, pady=self.button_padding)
        self.restart_button.pack(side="left", padx=20)

        self.exit_button = Button(self.button_frame, text="Exit", font=self.button_font, padx=self.button_padding, pady=self.button_padding, command=self.root.quit)
        self.exit_button.pack(side="left", padx=20)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = IQGameApp()
    app.run()
