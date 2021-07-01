""" Converter Trial 2 v2
based on 05_Converter_trial2v1
Completing the temp convert function at line 84
"""

from tkinter import *
from functools import partial  # To prevent unwanted additional windows
import random


class Converter:
    def __init__(self):
        # Formatting variables
        background_color = "light blue"

        # Converter Frame
        self.converter_frame = Frame(width=300, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font="Arial 16 bold",
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be "
                                                  "converted and then push "
                                                  "one of the buttons "
                                                  "below...",
                                             font="Arial 10 italic", wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3), orchid3 | khaki1
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  command=lambda: self.temp_convert(-459),
                                  bg="Khaki1", padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  command=lambda: self.temp_convert(-273),
                                  bg="Orchid1", padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame,
                                     text="Conversion goes here...",
                                     font="Arial, 14 bold",
                                     background=background_color, fg="purple",
                                     pady=10)
        self.converted_label.grid(row=4)

        # History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame,
                                       font="Arial 12 bold",
                                       text="Calculation History",
                                       width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, to):
        print(to)

        converted = 0  # Adding converted to be used later

        error = "#ffafaf"  # Pale pink background for when entry box has errors

        # Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)

            # Check amount is valid
            if to_convert < to:
                self.converted_label.configure(text="Too cold!!", fg="red")
                self.to_convert_entry.configure(bg=error)

            else:
                # Convert to F
                if to == -273:
                    converted = to_convert * 9 / 5 + 32

                # Convert to C
                if to == -459:
                    converted = (to_convert - 32) * 5 / 9

                # Round!!
                if converted % 1 == 0:
                    converted = int(converted)
                else:
                    converted = round(converted, 1)

                # Display answer
                self.to_convert_entry.configure(bg="white")
                if to == -273:
                    self.converted_label.configure(text=
                                                   "{} degrees C is {} degrees F"
                                                   .format(to_convert,
                                                           converted),
                                                   fg="blue")
                else:
                    self.converted_label.configure(text=
                                                   "{} degrees F is {} degrees C"
                                                   .format(to_convert,
                                                           converted),
                                                   fg="blue")
            # Add answer to list for History
            history.append(converted)
        except ValueError:
            self.converted_label.configure(text="Enter a number!!", fg="red")
            self.to_convert_entry.configure(bg=error)


# main routine
history = []
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()

