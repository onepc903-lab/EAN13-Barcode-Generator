import tkinter as tk

root = tk.Tk()
root.title("EAN13 Barcode Label Generator")
root.geometry("900x600")

label = tk.Label(
    root,
    text="EAN13 Barcode Label Generator Pro",
    font=("Arial", 20, "bold")
)
label.pack(pady=20)

root.mainloop()
