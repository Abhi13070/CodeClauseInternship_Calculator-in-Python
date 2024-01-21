import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Set up GUI elements
        self.root.geometry("600x600")  # Increase window size
        self.root.configure(bg='#3498db')  # Set background color

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.entry_var, font=('Helvetica', 18), justify='right', bd=10, insertwidth=4, width=14)
        self.entry.grid(row=0, column=0, columnspan=4, pady=20)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, font=('Helvetica', 14), bg='#2ecc71', fg='#ffffff',
                      command=lambda btn=button: self.button_click(btn)).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure rows and columns to expand proportionally
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        current_expression = self.entry_var.get()

        if value == '=':
            try:
                result = eval(current_expression)
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set('Error')
        elif value == 'C':
            self.entry_var.set('')
        else:
            current_expression += str(value)
            self.entry_var.set(current_expression)

# Create the main window
root = tk.Tk()
app = Calculator(root)

# Run the main loop
root.mainloop()
