from tkinter import*
from Backend import Database
database=Database()

def get_2(event):
    try:
        global selected_tuple
        index=lstbox.curselection()[0]
        selected_tuple=lstbox.get(index)
        title_entry.delete(0,END)
        title_entry.insert(END,selected_tuple[1])
        author_entry.delete(0,END)
        author_entry.insert(END,selected_tuple[2])
        year_entry.delete(0,END)
        year_entry.insert(END,selected_tuple[3])
        isbn_entry.delete(0,END)
        isbn_entry.insert(END,selected_tuple[4])
    except IndexError:
        pass



#################################################BUTTON FUNCTIONS######################################################################
def view_funct():
    lstbox.delete(0,END)
    for i in database.view_db():
        lstbox.insert(END,i)################please make sure looping variable and variable after end is same ##########

def search_funct():
    lstbox.delete(0,END)
    for search in database.search_db(title_entry_var.get(),author_entry_var.get(),year_entry_var.get(),isbn_entry_var.get()):
        lstbox.insert(END,search)

def add_funct():
    database.add_db(title_entry_var.get(),author_entry_var.get(),year_entry_var.get(),isbn_entry_var.get())
    lstbox.delete(0,END)
    lstbox.insert(END,(title_entry_var.get(),author_entry_var.get(),year_entry_var.get(),isbn_entry_var.get()))

def delete_funct():
    database.delete_db(selected_tuple[0])

def update_funct():
    database.update_db(title_entry_var.get(),author_entry_var.get(),year_entry_var.get(),isbn_entry_var.get(),selected_tuple[0])
    

#################################################
window=Tk()
####### all TITLE RELATED################
title_label=Label(window,text="Title")
title_label.grid(row=0,column=0)

title_entry_var=StringVar()
title_entry=Entry(window,textvariable=title_entry_var)
title_entry.grid(row=0,column=1)
##############ENDS HERE#######################
'''                 '''



#################AUTHOR#######################
author_label=Label(window,text="Author")
author_label.grid(row=0,column=2)

author_entry_var=StringVar()
author_entry=Entry(window,textvariable=author_entry_var)
author_entry.grid(row=0,column=3)
#####################ENDS#############
'''                                 '''
###################YEAR###############

year_label=Label(window,text='Year')
year_label.grid(row=1, column=0)

year_entry_var=StringVar()
year_entry=Entry(window,textvariable=year_entry_var)
year_entry.grid(row=1,column=1)
################ENDS############
'''                          '''

#############ISBN##############

isbn_label=Label(window,text="ISBN")
isbn_label.grid(row=1,column=2)

isbn_entry_var=StringVar()
isbn_entry=Entry(window,textvariable=isbn_entry_var)
isbn_entry.grid(row=1,column=3)
##########END#################
'''                        '''

#########LSITBOX##############
lstbox=Listbox(window,width=45)
lstbox.grid(row=2,rowspan=6,column=0,columnspan=2)
lstbox.bind('<<ListboxSelect>>',get_2)

##########END#################
'''                        '''
##########SCROLLBAR###########
scrl_br=Scrollbar(window)
scrl_br.grid(row=2,rowspan=6,column=2)
lstbox.configure(yscrollcommand=scrl_br.set)
scrl_br.configure(command=lstbox.yview)
############END################

###############BUTTONS START HERE#######################################################################################################
########################################################################################################################################

###########View all############

view_button=Button(window,text="View all",width=15,command=view_funct)
view_button.grid(row=2,column=3)
###############END##############

##########SEARCH################

search_button=Button(window,text="Search Entry",width=15,command=search_funct)
search_button.grid(row=3,column=3)
###############END###############



###########ADD###################

add_button=Button(window,text="ADD ENTRY",width=15,command=add_funct)
add_button.grid(row=4,column=3)
#########################################

##############UPDATE#####################

update_button=Button(window,text="Update",width=15,command=update_funct)
update_button.grid(row=5,column=3)
###################################################

################Delete################

del_button=Button(window,text="Delete",width=15,command=delete_funct)
del_button.grid(row=6,column=3)
###################################

###############CLOSE##############

close_button=Button(window,text="Close",width=15,command=window.destroy)
close_button.grid(row=7,column=3)
#########################################################
window.mainloop()
