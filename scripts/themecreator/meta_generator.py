from tkinter import *
from tkinter.colorchooser import askcolor

linecolor = bgcolor = ()


def main():
    root = Tk()
    root.resizable(False, False)
    root.title('Customize Your Game')
    v = BooleanVar()
    output = []

    def color(which):
        global linecolor, bgcolor
        if which == "line":
            linecolor = askcolor()
        if which == "bg":
            bgcolor = askcolor()

    def forget_widget(widget):
        widget.grid_forget()

    def choice(value):
        lbl_color = Label(text="Set Background Color")
        btn_color = Button(text="Choose Color", command=lambda: color("bg"))
        lbl_color.grid(row=5, column=1, padx=5, pady=5)
        btn_color.grid(row=5, column=2, padx=5, pady=5)

        lbl_line_color = Label(text="Set Line Color")
        btn_line_color = Button(text="Choose Color", command=lambda: color("line"))
        lbl_line_color.grid(row=6, column=1, padx=5, pady=5)
        btn_line_color.grid(row=6, column=2, padx=5, pady=5)
        if not value:
            forget_widget(lbl_color)
            forget_widget(btn_color)
            forget_widget(lbl_line_color)
            forget_widget(btn_line_color)

    def destroy_stuff():
        output.extend([v.get(), linecolor, bgcolor, inp_gap.get(), inp_speed.get()])
        root.destroy()

    lbl_gap = Label(text="Set gap between lines")
    lbl_gap.grid(row=1, column=1, padx=5, pady=5)
    inp_gap = Entry()
    inp_gap.insert(END, '40')
    inp_gap.grid(row=1, column=2, padx=5, pady=5)

    lbl_speed = Label(text="Set Game Speed")
    lbl_speed.grid(row=3, column=1, padx=5, pady=5)
    inp_speed = Entry()
    inp_speed.insert(END, '1')
    inp_speed.grid(row=3, column=2, padx=5, pady=5)

    lbl_ask_bg_image = Label(text="Set Image For Background")
    lbl_ask_bg_image.grid(row=4, column=1, padx=5, pady=5)
    Radiobutton(root, text="No", variable=v, value=True, command=lambda: choice(v.get())).grid(row=4, column=3)
    Radiobutton(root, text="Yes", variable=v, value=False, command=lambda: choice(v.get())).grid(row=4, column=2)

    Button(text="Ok", command=lambda: destroy_stuff()).grid(row=7, column=1, padx=10, pady=10, ipady=2, ipadx=20)
    root.mainloop()

    return output


print(main())
