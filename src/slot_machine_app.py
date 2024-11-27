import tkinter as tk
import random
import time

class SlotMachineApp:
    def __init__(self, root):
        self.root = root
        self.items = ["Quantifier", "P(x)", "x"]
        self.animation_speed = 0.1

        self.statements = self.load_statements()

        self.create_widgets()

    def load_statements(self):
        with open('assets/statements.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]

    def create_widgets(self):
        self.root.title("Discrete Structures - Slot Machine")

        self.root.bind('<Escape>', lambda event: self.root.state('normal'))
        self.root.bind('<F11>', lambda event: self.root.state('zoomed'))

        self.statement_label = tk.Label(self.root, text="Statement: ", font=("Arial", 14))
        self.statement_label.pack(pady=20)

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True)

        self.slots_frame = tk.Frame(self.main_frame)
        self.slots_frame.grid(row=1, column=0, pady=20, padx=20)

        self.slots = []
        for i in range(3):
            slot_label = tk.Label(self.slots_frame, text=self.items[i], font=("Arial", 30), width=7, relief="solid", borderwidth=2)
            slot_label.grid(row=0, column=i, padx=15)
            self.slots.append(slot_label)

        self.shuffle_button = tk.Button(self.root, text="Shuffle Slots", font=("Arial", 12), command=self.shuffle_slots)
        self.shuffle_button.pack(pady=20)

    def shuffle_slots(self):
        def spin():
            for _ in range(10):
                for i, slot in enumerate(self.slots):
                    slot.config(text=random.choice(self.items))
                self.root.update()
                time.sleep(self.animation_speed)

            random.shuffle(self.items)
            for i, slot in enumerate(self.slots):
                slot.config(text=self.items[i])

            self.animate_statement()

        self.root.after(0, spin)

    def animate_statement(self):
        def change_statement():
            for _ in range(5):
                random_statement = random.choice(self.statements)
                self.statement_label.config(text=random_statement)
                self.root.update()
                time.sleep(self.animation_speed)

            random_statement = random.choice(self.statements)
            self.statement_label.config(text=random_statement)

        self.root.after(0, change_statement)
