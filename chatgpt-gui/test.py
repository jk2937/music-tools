import tkinter as tk

# Define the GUI class
class SequencerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Step Sequencer")

        # Define the sequencer pattern as a list of lists
        self.pattern = [[0] * 16 for _ in range(8)]

        # Create the grid of buttons for the sequencer
        self.buttons = []
        for row in range(8):
            button_row = []
            for col in range(16):
                button = tk.Button(root, text="", width=2, height=1,
                                   bg="grey", activebackground="white",
                                   command=lambda row=row, col=col: self.toggle_button(row, col))
                button.grid(row=row, column=col, padx=1, pady=1)
                button_row.append(button)
            self.buttons.append(button_row)

        # Create the play button
        self.play_button = tk.Button(root, text="Play", width=10, command=self.play)
        self.play_button.grid(row=8, column=0, columnspan=16, pady=10)

    # Define the function to toggle a button on/off
    def toggle_button(self, row, col):
        if self.pattern[row][col] == 0:
            self.pattern[row][col] = 1
            self.buttons[row][col].configure(bg="green")
        else:
            self.pattern[row][col] = 0
            self.buttons[row][col].configure(bg="grey")

    # Define the function to play the sequencer
    def play(self):
        # Add your code here to play the sequencer pattern
        pass

# Create the root window and start the GUI
root = tk.Tk()
app = SequencerGUI(root)
root.mainloop()

