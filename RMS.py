import tkinter as tk

from tkinter import messagebox

root=tk.Tk()
root.title("Restaurant Management System")

root.geometry("500x500")

menu={
    "Burger":3,
    "Pizza":5,
    "Pasta":2,
    "Coke":3,
    "Sandwich":1
    }

quantities={}

tk.Label(
    root,
    text="Restaurant Manageent System",
    font=("Arial",18,"bold")
).pack(pady=15)

for item,price in menu.items():

    frame=tk.Frame(root)
    frame.pack(pady=5)

    tk.Label(
        frame,
        text=f"{item}-${price}",
        width=20,
        anchor="w"
    ).pack(side="left")

    entry=tk.Entry(frame,width=5)
    entry.pack(side="left")

    quantities[item]=entry

def  place_order():
    total=0
    summary="Order Summary:\n\n"

    for items, entry in quantities.items():
        if entry.get().isdigit():

            quantity=int(entry.get())

            cost= quantity*menu[item]

            total+=cost

            if quantity > 0:
                summary += f"{item}:{quantity} x ${menu[item]} = ${cost}\n"

    if total > 0:
        summary += f"\nTotal Cost: ${total}"

        messagebox.showinfo("Order Placed",summary)

    else:
        messagebox.showerror(
            "Error",
            "Please order at least one item"
        )

tk.Button(
    root,
    text="Place Order",
    command=place_order,
    font=("Ariel",12,"bold")
).pack(pady=20)

root.mainloop()