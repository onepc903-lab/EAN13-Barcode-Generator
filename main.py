import tkinter as tk
from tkinter import ttk
import barcode
from barcode.writer import ImageWriter
from tkinter import messagebox
root = tk.Tk()
root.title("EAN13 Barcode Generator")
root.geometry("700x500")

title = ttk.Label(
    root,
    text="EAN13 Barcode Generator Pro",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)

ttk.Label(root, text="Product Name").pack()
product_entry = ttk.Entry(root, width=50)
product_entry.pack(pady=5)

ttk.Label(root, text="EAN-13 Number").pack()
barcode_entry = ttk.Entry(root, width=50)
barcode_entry.pack(pady=5)

def generate_barcode():
    number = barcode_entry.get().strip()

    if len(number) != 12 or not number.isdigit():
        messagebox.showerror(
            "Error",
            "Please enter exactly 12 digits.\nThe 13th check digit will be generated automatically."
        )
        return

    ean = barcode.get("ean13", number, writer=ImageWriter())
    filename = ean.save("barcode")

    messagebox.showinfo(
        "Success",
        f"Barcode saved successfully:\n{filename}"
    )

generate_btn = ttk.Button(
    root,
    text="Generate Barcode",
    command=generate_barcode
)
generate_btn.pack(pady=20)

root.mainloop()
