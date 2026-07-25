import tkinter as tk
from tkinter import ttk

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

generate_btn = ttk.Button(root, text="Generate Barcode")
generate_btn.pack(pady=20)

root.mainloop()
