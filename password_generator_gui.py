#!/usr/bin/env python3
"""Secure Password Generator GUI using Tkinter."""

import tkinter as tk
from tkinter import messagebox
import secrets
import string

# Define character sets as constants
CHAR_SETS = {
    "Uppercase A-Z": string.ascii_uppercase,
    "Lowercase a-z": string.ascii_lowercase,
    "Digits 0-9": string.digits,
    "Symbols !@#$…": string.punctuation,
}


class PasswordGeneratorApp:
    """GUI application for generating secure passwords."""

    def __init__(self, master):
        """Initialize the GUI components."""
        self.master = master
        master.title("Secure Password Generator")

        # Configure grid weights for resizing
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=0)
        master.rowconfigure(1, weight=0)
        master.rowconfigure(2, weight=0)
        master.rowconfigure(3, weight=0)
        master.rowconfigure(4, weight=1)

        # Password length selection
        length_frame = tk.Frame(master)
        length_frame.grid(padx=10, pady=5, sticky="ew")
        tk.Label(length_frame, text="Password length:").pack(side="left")
        self.length_var = tk.IntVar(value=12)
        self.spin_length = tk.Spinbox(
            length_frame,
            from_=6,
            to=64,
            textvariable=self.length_var,
            width=5,
        )
        self.spin_length.pack(side="left", padx=(5, 0))

        # Character set checkboxes
        self.check_vars = {}
        check_frame = tk.Frame(master)
        check_frame.grid(padx=10, pady=5, sticky="ew")
        for label in CHAR_SETS:
            var = tk.BooleanVar(value=True)
            chk = tk.Checkbutton(
                check_frame, text=label, variable=var,
                command=self.update_generate_button
            )
            chk.pack(side="left", padx=5)
            self.check_vars[label] = var

        # Generate button
        self.btn_generate = tk.Button(
            master, text="Generate", command=self.generate_password
        )
        self.btn_generate.grid(padx=10, pady=5, sticky="ew")

        # Error message label
        self.error_label = tk.Label(master, text="", fg="red")
        self.error_label.grid(padx=10, sticky="w")

        # Password display entry
        entry_frame = tk.Frame(master)
        entry_frame.grid(padx=10, pady=5, sticky="ew")
        entry_frame.columnconfigure(0, weight=1)
        self.password_var = tk.StringVar()
        self.entry_password = tk.Entry(
            entry_frame, textvariable=self.password_var, state="readonly"
        )
        self.entry_password.grid(row=0, column=0, sticky="ew")

        # Copy to clipboard button
        self.btn_copy = tk.Button(
            entry_frame, text="Copy to clipboard", command=self.copy_password
        )
        self.btn_copy.grid(row=0, column=1, padx=(5, 0))

        # Initial update to set button state
        self.update_generate_button()

    def update_generate_button(self):
        """Enable or disable the Generate button based on selections."""
        # Check if at least one character set is selected
        if any(var.get() for var in self.check_vars.values()):
            self.btn_generate.config(state="normal")
            self.error_label.config(text="")
        else:
            self.btn_generate.config(state="disabled")
            self.error_label.config(
                text="Select at least one character set"
            )

    def generate_password(self):
        """Generate a secure password and display it."""
        length = self.length_var.get()
        # Build the pool of characters from selected sets
        pool = "".join(
            CHAR_SETS[label] for label, var in self.check_vars.items()
            if var.get()
        )
        # Generate password using secrets.choice for security
        password = "".join(secrets.choice(pool) for _ in range(length))
        self.password_var.set(password)

    def copy_password(self):
        """Copy the generated password to the clipboard."""
        password = self.password_var.get()
        if password:
            self.master.clipboard_clear()
            self.master.clipboard_append(password)
            # Notify user of successful copy
            messagebox.showinfo("Copied", "Password copied to clipboard!")


def main():
    """Run the password generator application."""
    root = tk.Tk()
    PasswordGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()