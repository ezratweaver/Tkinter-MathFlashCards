import sys
from tkinter import Canvas, Button, font
from typing import List

sys.path.append("../utilities")
sys.path.append("../assets")

from user_data import get_userlist_banner, check_for_users, MAX_USERS
from assets import root, WINDOW_COLOR, userscreen_banners, get_font_size
import assets
import memory


START_POSITIONS = {
    0 : 250,
    1 : 218, 2 : 186,
    3 : 154, 4 : 121,
    5 : 88, 6 : 88
}

USER_BUTTON_DIMENSIONS = (43, 160)

user_title_font = font.Font(family="Encode Sans", size=20)

class UserScreen:

    def __init__(self) -> None:
        self.canvas = Canvas(
            root, bg=WINDOW_COLOR,
            height=500, width = 800,
            bd=0, highlightthickness=0,
            relief="ridge")
        
        memory.all_users = check_for_users()

    def print_banner(self, usercount) -> None:
        self.userlist_banner = self.canvas.create_image(
            400,
            250,
            image=get_userlist_banner(usercount, userscreen_banners)
        )

    def print_user_buttons(self, usercount: int):
        """
        Create and configure user buttons in the graphical user interface.

        Args:
            self: The instance of the class.
            usercount: An integer representing the number of users for whom buttons 
                        need to be created.
        """
        y_start_pos = START_POSITIONS.get(usercount)
        self.title_buttons = []
        self.title_buttons_bg = []
        self.action_buttons = []
        self.action_buttons_bg = []
        if usercount >= MAX_USERS:  # Add an extra button if MAX_USERS has not been
            usercount = MAX_USERS - 1                     #reached, otherwise dont.

        for x in range(usercount + 1):
            self.title_buttons_bg.append(self.canvas.create_image(
                434,
                y_start_pos,
                image=assets.buttons["long"]))
            self.action_buttons_bg.append(self.canvas.create_image(
                314,
                y_start_pos,
                image=assets.buttons["square"]))
            self.title_buttons.append(Button(
                self.canvas,
                fg="#000000",
                bg="#D9D9D9",
                activebackground="#D9D9D9",
                anchor="center",
                borderwidth=0,
                highlightthickness=0,
                relief="flat"))
            self.title_buttons[x].place(x = 354, y = y_start_pos - 21,
                                 width=160.0, height=43.0)
            self.action_buttons.append(Button(
                self.canvas,
                fg="#000000",
                bg="#D9D9D9",
                activebackground="#D9D9D9",
                image=assets.userscreen_useradd,
                anchor="center",
                borderwidth=0,
                highlightthickness=0,
                relief="flat"))
            self.action_buttons[x].place(x = 289, y = y_start_pos - 21,
                                    width=50.0, height=43.0)
            y_start_pos = y_start_pos + 65

        for x, user in enumerate(memory.all_users):
            font_size = get_font_size(user["displayname"], self.title_buttons[x],
                                       user_title_font, root)
            self.title_buttons[x].config(text=f"{user['displayname']}", 
                                    font=("Encode Sans", font_size))
            self.action_buttons[x].config(image=assets.userscreen_userprofile)

        for x, title_button in enumerate(self.title_buttons):
            title_button.bind("<Enter>", lambda event, x=x: 
                assets.button_event_map(event, self.canvas,
                                        self.title_buttons_bg[x], assets.buttons["long_selected"]))
            title_button.bind("<Leave>" , lambda event, x=x: 
                assets.button_event_map(event, self.canvas,
                                        self.title_buttons_bg[x], assets.buttons["long"]))

        for x, action_button in enumerate(self.action_buttons):
            action_button.bind("<Enter>", lambda event, x=x: 
                assets.button_event_map(event, self.canvas,
                                        self.action_buttons_bg[x], assets.buttons["square_selected"]
                                        ))
            action_button.bind("<Leave>" , lambda event, x=x: 
                assets.button_event_map(event, self.canvas,
                                        self.action_buttons_bg[x], assets.buttons["square"]))

    def show_canvas(self) -> None:
        memory.all_users = check_for_users()
        usercount = len(memory.all_users)
        self.print_banner(usercount)
        self.print_user_buttons(usercount)
        self.canvas.pack()

    def hide_canvas(self) -> None:
        self.canvas.delete("all")
        [x.destroy() for x in self.action_buttons]
        [x.destroy() for x in self.title_buttons]
        self.canvas.pack_forget()


if __name__ == "__main__":
    userscreen = UserScreen()
    userscreen.show_canvas()
    root.title("Userscreen")
    root.mainloop()

