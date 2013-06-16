from swampy import Gui
    
# create some new Gui object
g = Gui.Gui()

# give it a title
g.title('Gui')

# create a label widget
label = g.la(text='Press the button.')

# add a button
g.bu(text='Press me!')

# add another button
def make_label():
    g.la(text='Thank you.')

button2 = g.bu(text='No, press me!', command=make_label)

# allows user to enter a single line of text
entry = g.en(text='Default text.')

# allows user to enter multiple lines of text
text = g.te(width=100, height=5)
text.insert(END, 'A line of text.')

# create a canvas
canvas = g.ca(width=500, height=500)
canvas.config(bg='white')

# draw a circle
item = canvas.circle([0,0], 100, fill='red')
item.config(outline='orange', width=10)

# draw a rectangle
bbox = [[0,0],[200,100]]
canvas.rectangle(bbox, fill='blue', outline='orange', width=10)

# draw an oval
canvas.oval(bbox, outline='orange', width=10)

# draw some polygon
canvas.polygon([[0, 100], [100, 200], [200, 100]], fill='red', 
               outline='orange', width=10)
               
# runs the event loop (which is infinite!)
g.mainloop()

# solution to exercise 1
def make_label():
    exercise1.la(text='Nice job!')

def make_button():
    exercise1.bu(text='Now, press this button.', command=make_label)
    
exercise1 = Gui.Gui()
exercise1.title('Exercise 1')
exercise1.bu(text='Press this button!', command=make_button)
exercise1.mainloop()

# solution to exercise 2
def draw_circle():
    canvas.circle([0,0], 100, fill='red')
    
exercise2 = Gui.Gui()
exercise2.title('Exercise 2')

canvas = exercise2.ca(width=500, height=500)
button = exercise2.bu(text='Draw a circle', command=draw_circle)

exercise2.mainloop()

# solution to exercise 3
exercise3 = Gui.Gui()
exercise3.title('Exercise 2')
canvas = exercise3.ca(width=500, height=500)
circle = None

def draw_circle():
    global circle
    circle = canvas.circle([0,0], 100, fill='red')
 
def edit_circle():
    # modify the created circle
    circle.config(fill=entry.get())
        
button = exercise3.bu(text='Draw a circle', command=draw_circle)

entry = exercise3.en(text='Enter your preferred color here.')
button2 = exercise3.bu(text='Modify color', command=edit_circle)

exercise3.mainloop()