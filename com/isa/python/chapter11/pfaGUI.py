# !/usr/bin/env python
# excerpt from the book
# "From what you have seen so far, you can see that PFA takes on the flavors of templating and "style-sheeting"
# in terms of providing defaults in a more functional programming environment."

# partial class instantiation, similar to partial function application
# can reassign fixed arguments if needed and if they are formal parameters
from functools import partial
import Tkinter

root = Tkinter.Tk()
MyButton = partial(Tkinter.Button, root,
                   fg='white', bg='blue')
b1 = MyButton(text='Button 1')
b2 = MyButton(text='Button 2')
qb = MyButton(text='QUIT', bg='red',
              command=root.quit)
b1.pack()
b2.pack()
qb.pack(fill=Tkinter.X, expand=True)
root.title('PFAs!')
root.mainloop()
