from Tkinter import *
root = Tk()
C_entry = Entry(root, width=4)
C_entry.pack(side='left')
Cunit_label = Label(root, text='Celcius')
Cunit_label.pack(side='left')

def compute():
    C = float(C_entry.get())
    K = (-273.15) + C
    K_label.configure(text='%g' %K)


compute = Button(root, text=' is ', command=compute)
compute.pack(side='left', padx=5)

K_label = Label(root, width=6)
K_label.pack(side='left')
Kunit_label = Label(root, text='Kelvin')
Kunit_label.pack(side='left')

root.mainloop()
