"""
A program that stores the book information:
Title, Author
Year, ISBN

User can:
view all records
search an entry
add entry
update entry
delete 
close
https://www.udemy.com/the-python-mega-course/learn/v4/t/lecture/4775396?start=0
"""

from tkinter import *
import app5_backend

#global selected_tuple

def view_command():
	#print(app5_backend.view_table())
	list_box.delete(0,END)
	for row in app5_backend.view_table():
		list_box.insert(END, row)

def search_command():
	#print(app5_backend.view_table())
	list_box.delete(0,END)
	for row in app5_backend.search(title=inputboxtitle_value.get(), author=inputboxauthor_value.get(), \
		year=inputboxyear_value.get(), isbn=inputboxISBN_value.get()):
		list_box.insert(END, row)

def add_command():
	#print(app5_backend.view_table())
	list_box.delete(0,END)
	app5_backend.insert(inputboxtitle_value.get(), inputboxauthor_value.get(), \
		inputboxyear_value.get(), inputboxISBN_value.get())
	list_box.insert(END, (inputboxtitle_value.get(), inputboxauthor_value.get(), \
		inputboxyear_value.get(), inputboxISBN_value.get()))

def update_command():
	#print(app5_backend.view_table())
	#id=selected_tuple[0]
	app5_backend.update(id=selected_tuple[0], title=inputboxtitle_value.get(), author=inputboxauthor_value.get(), \
		year=inputboxyear_value.get(), isbn=inputboxISBN_value.get())
	#pass
	# list_box.delete(0,END)
	# app5_backend.update(id=40,title=inputboxtitle_value.get(), author=inputboxauthor_value.get(), \
	# 	year=int(inputboxyear_value.get()), isbn=int(inputboxISBN_value.get()))
	#	list_box.insert(END, row)

def get_selected_row(event):
	
	try:
		index=list_box.curselection()[0]
		print(index)
		global selected_tuple
		selected_tuple=list_box.get(index)
		print(selected_tuple)
		# list_box.delete(0,END)
		# list_box.insert(0, selected_tuple)
		
		inputboxtitle.delete(0,END)
		inputboxtitle.insert(END,selected_tuple[1])
		inputboxauthor.delete(0,END)
		inputboxauthor.insert(END,selected_tuple[2])
		inputboxyear.delete(0,END)
		inputboxyear.insert(END,selected_tuple[3])
		inputboxISBN.delete(0,END)
		inputboxISBN.insert(END,selected_tuple[4])
	except IndexError:
		pass
	#return(selected_tuple[0])
	# inputboxtitle_value, inputboxauthor_value, inputboxyear_value, inputboxISBN_value=\
	# selected_tuple[1], selected_tuple[2], selected_tuple[3], selected_tuple[4]	
	#list_box.insert


def del_command():
	#print(app5_backend.view_table())
	#list_box.delete(0,END)
	app5_backend.delete(id=selected_tuple[0])
	#	list_box.insert(END, row)

# def close_command():
# 	#print(app5_backend.view_table())
# 	list_box.delete(0,END)


window=Tk()
window.wm_title('Book Store')

'''draw grid lines to get the coordinates of each component'''
label_title=Label(window, text='Title')
label_title.grid(row=0, column=0)

inputboxtitle_value=StringVar()
inputboxtitle=Entry(window, textvariable=inputboxtitle_value)
inputboxtitle.grid(row=0, column=1)

label_author=Label(window, text='Author')
label_author.grid(row=0, column=2)

inputboxauthor_value=StringVar()
inputboxauthor=Entry(window, textvariable=inputboxauthor_value)
inputboxauthor.grid(row=0, column=3)

label_year=Label(window, text='Year')
label_year.grid(row=1, column=0)

inputboxyear_value=StringVar()
inputboxyear=Entry(window, textvariable=inputboxyear_value)
inputboxyear.grid(row=1, column=1)

label_ISBN=Label(window, text='ISBN')
label_ISBN.grid(row=1, column=2)

inputboxISBN_value=StringVar()
inputboxISBN=Entry(window, textvariable=inputboxISBN_value)
inputboxISBN.grid(row=1, column=3)

button_veiwall=Button(window, text='View All', height=1, width=15, command=view_command)
button_veiwall.grid(row=2, column=3)

button_search=Button(window, text='Search entry', height=1, width=15, command=search_command)
button_search.grid(row=3, column=3)

button_add=Button(window, text='Add entry', height=1, width=15, command=add_command)
button_add.grid(row=4, column=3)

button_update=Button(window, text='Update', height=1, width=15, command=update_command)
button_update.grid(row=5, column=3)

button_del=Button(window, text='Delete', height=1, width=15, command=del_command)
button_del.grid(row=6, column=3)

button_close=Button(window, text='Close', height=1, width=15, command=window.destroy)
button_close.grid(row=7, column=3)

list_box=Listbox(window, height=8, width=30)
list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

#bind event type with specfic function
list_box.bind('<<ListboxSelect>>', get_selected_row)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list_box.configure(yscrollcommand=sb1.set)
sb1.configure(command=list_box.yview)

window.mainloop()