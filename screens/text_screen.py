import sys
from tkinter import Canvas, Button, Entry, font

sys.path.append("../utilities")
sys.path.append("../assets")

from user_data import create_user, rename_user
from assets import root, WINDOW_COLOR, get_font_size, bind_hover_animation
import assets

INPUT_CHAR_LIMIT = 14
CHANGE_FONT_LIMIT = 12

text_entry_font = font.Font(family="Encode Sans", size=20)

class TextScreen:

    def __init__(self) -> None:
        self.button_bgs = {}
        self.buttons = {}

        self.canvas = Canvas( root, bg=WINDOW_COLOR,
            height=500, width = 800,
            bd=0, highlightthickness=0,
            relief="ridge")
        self.canvas.create_image(
            398,
            250,
            image=assets.textscreen["username_enter_banner"]
        )
        self.canvas.create_image(
            400,
            220,
            image=assets.textscreen["please_enter_name"]
        )
        self.canvas.create_image(
            400,
            273,
            image=assets.textscreen["enter_box"]
        )
        self.button_bgs["cancel_button"] = self.canvas.create_image(
            275,
            273,
            image=assets.buttons["square"]
        )
        self.buttons["cancel_button"] = Button(
            self.canvas, 
            fg="#000000",
            bg="#D9D9D9",
            activebackground="#D9D9D9",
            image=assets.textscreen["cancel"],
            anchor="center",
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.buttons["cancel_button"].place(x=250, y=252, width=51, height=43)

        self.button_bgs["confirm_button"] = self.canvas.create_image(
            525,
            273,
            image=assets.buttons["square"]
        )
        self.buttons["confirm_button"] = Button(
            self.canvas,
            fg="#000000",
            bg="#D9D9D9",
            activebackground="#D9D9D9",
            image=assets.textscreen["confirm"],
            anchor="center",
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.buttons["confirm_button"].place(x=500, y=252, width=51, height=43)

        bind_hover_animation(self.canvas, self.button_bgs,
                             self.buttons, assets.buttons["square"],
                             assets.buttons["square_selected"])
        
        def validate_input(current_input):
            if current_input == "":
                return True
            if len(current_input) > CHANGE_FONT_LIMIT:
                text_entry_font.configure(size=16)
            else:
                text_entry_font.configure(size=20)
            return len(current_input) <= INPUT_CHAR_LIMIT
        
        validate_cmd = root.register(validate_input)

        self.text_entry = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=text_entry_font,
            justify="center",
            validate="key",
            validatecommand=(validate_cmd, "%P"),
        )
        self.text_entry.place(x=313.0, y=251.0, width=176.0, height=44.0)
        self.text_entry.focus_set()

    def show_canvas(self) -> None:
        self.canvas.pack()

    def hide_canvas(self) -> None:
        self.text_entry.delete("0", "end")
        self.canvas.pack_forget()



if __name__ == "__main__":
    text = TextScreen()
    text.show_canvas()
    root.mainloop()
