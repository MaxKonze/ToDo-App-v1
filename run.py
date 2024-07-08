import customtkinter
from utilities import datum_als_datetime
from customtkinter import *
from tkinter import PhotoImage
from todo import *
from new_todo import add_todo
from datetime import datetime
from database import *
from gui_items import create_all_elements
from change_todo_infos import change_info

if __name__ == '__main__':
    # general settings for the gui
    customtkinter.set_default_color_theme('blue')
    customtkinter.set_appearance_mode('system')

    # create a new root
    root = CTk()

    y_all, y_finish, y_not_finish = 0, 0, 0
    open_todo = None

    add = PhotoImage(file='images/add_FILL0_wght400_GRAD0_opsz24.png')
    unfinished = PhotoImage(file='images/radio_button_unchecked_FILL0_wght400_GRAD0_opsz24.png')
    finished = PhotoImage(file='images/check_circle_FILL0_wght400_GRAD0_opsz24.png')
    close = PhotoImage(file='images/close_FILL0_wght400_GRAD0_opsz24.png')
    delete = PhotoImage(file='images/delete_FILL0_wght400_GRAD0_opsz24.png')

    # geometry and title for the gui
    root.geometry('1280x720')
    root.title('TODO')

    show_Frame, title_Frame, people_Frame, date_Frame, time_Frame, place_Frame, notices_Frame, show_title, show_people, show_people2, show_date, show_time, show_place, show_notes = create_all_elements(
        root)

    show_Frame.place(relx=0.19, rely=0.02, relheight=0.97, relwidth=0.8)
    show_notes.place(relx=0, rely=0, anchor=NW)
    show_place.place(relx=0, rely=0.5, anchor=W)
    show_time.place(relx=0, rely=0.5, anchor=W)
    show_date.place(relx=0, rely=0.5, anchor=W)
    show_people2.place(relx=0.3, rely=0, anchor=NW)
    show_people.place(relx=0, rely=0, anchor=NW)
    show_title.place(relx=0, rely=0.2)


    def close_info():

        # closes all the info
        title_Frame.place_forget()
        people_Frame.place_forget()
        date_Frame.place_forget()
        time_Frame.place_forget()
        place_Frame.place_forget()
        notices_Frame.place_forget()
        close_Button.place_forget()


    def change():

        new_info = change_info(open_todo)
        open_todo.title, open_todo.people, open_todo.text, open_todo.place, open_todo.date, open_todo.time_start, open_todo.time_end = new_info

        close_info()
        place_all_buttons(open_todo)
        place_buttons()
        place_buttons_all()

        show_info(open_todo)


    close_Button = CTkButton(
        title_Frame,
        image=close,
        text='',
        fg_color='transparent',
        hover=False,
        command=close_info
    )

    change_Button = CTkButton(
        notices_Frame,
        text='Ändern',
        # fg_color='transparent',
        hover=False,
        command=change
    )

    # places the buttons in the finished and unfinished tab
    def place_buttons():
        y_2, y_1 = 0, 0
        finished_todos, not_finished_todos = [], []

        # removes all buttons
        for todo in to_load:
            todo.CTk_Button_not_finish.place_forget()
            todo.CTk_Button_finished_not_finish.place_forget()

            todo.CTk_Button_finish.place_forget()
            todo.CTk_Button_finished_finish.place_forget()

            if todo.done == 0:
                not_finished_todos.append((todo.date, todo))
            else:
                finished_todos.append((todo.date, todo))

        # sorts the list by dates
        sor_finished_todos = sorted(finished_todos, key=datum_als_datetime)
        sor_not_finished_todos = sorted(not_finished_todos, key=datum_als_datetime)

        # replaces all buttons
        for todo_ in sor_not_finished_todos:
            todo_[1].CTk_Button_not_finish.place(relx=0.05, rely=0 + y_1, relheight=0.08, relwidth=0.9)
            todo_[1].CTk_Button_finished_not_finish.place(relx=0.05, rely=0 + y_1 + 0.013, relwidth=0.2)
            y_1 += 0.09

        for todo_ in sor_finished_todos:
            todo_[1].CTk_Button_finish.place(relx=0.05, rely=0 + y_2, relheight=0.08, relwidth=0.9)
            todo_[1].CTk_Button_finished_finish.place(relx=0.05, rely=0 + y_2 + 0.013, relwidth=0.2)
            y_2 += 0.09

    # a function to place the buttons in the all tab
    def place_buttons_all():
        y = 0
        dates, dates_ = [], []

        # delete all buttons
        for t in to_load:
            t.CTk_Button_all.place_forget()
            t.CTk_Button_finished_all.place_forget()
            dates.append((t.date, t))

        # sorts the buttons b y order
        dates_sor = sorted(dates, key=datum_als_datetime)

        # replaces all buttons
        for todo_ in dates_sor:
            todo_[1].CTk_Button_all.place(relx=0.05, rely=0 + y, relheight=0.08, relwidth=0.9)
            todo_[1].CTk_Button_finished_all.place(relx=0.05, rely=0 + y + 0.013, relwidth=0.2)
            y += 0.09

    # a function that deletes a task if sb presses the del button
    def del_todo():
        global to_load

        open_todo.set_del()
        close_info()

        todos = to_load
        to_load = []

        for t in todos:
            if t != open_todo:
                to_load.append(t)

        print(to_load)

        open_todo.CTk_Button_not_finish.place_forget()
        open_todo.CTk_Button_finished_not_finish.place_forget()

        open_todo.CTk_Button_finish.place_forget()
        open_todo.CTk_Button_finished_finish.place_forget()

        open_todo.CTk_Button_all.place_forget()
        open_todo.CTk_Button_finished_all.place_forget()

        place_buttons()
        place_buttons_all()

    delete_Button = CTkButton(
        title_Frame,
        image=delete,
        text='',
        fg_color='transparent',
        hover=False,
        bg_color='transparent',
        command=del_todo
    )


    def show_info(open__todo):
        global open_todo

        people, people2 = '', ''

        open_todo = open__todo

        # set title Label to the title
        show_title.configure(text=f'Titel: {open__todo.title}')

        # insert the members into one to two rows
        for i, person in enumerate(open__todo.people):
            if i <= 4:
                if person != '':
                    people = f'{people}• {person}\n'
            else:
                people2 = f'{people2}• {person}\n'
        show_people.configure(text=people)
        show_people2.configure(text=people2)

        # set date Label to the date and the day in the week
        date = datetime(int(open__todo.date[6] + open__todo.date[7] + open__todo.date[8] + open__todo.date[9]),
                        int(open__todo.date[3] + open__todo.date[4]), int(open__todo.date[0] + open__todo.date[1]))
        show_date.configure(text=open__todo.date + ', ' + date.strftime('%A'))

        # set time Label to the time or the hole day
        if open__todo.time_start == 'hole':
            show_time.configure(text=f'Ganztägig am {open__todo.date}')
        elif open__todo.time_start == '':
            pass
        else:
            show_time.configure(text=f'{open__todo.time_start} - {open__todo.time_end}')

        # set the place Label to the place
        show_place.configure(text=f'Ort: {open__todo.place}')

        # set the note Label to the notes
        if type(open__todo.text) is str:
            show_notes.configure(text=open__todo.text)
        else:
            show_notes.configure(text=open__todo.text[0])

        # place all the Frames
        title_Frame.place(relx=0.01, rely=0.01, relheight=0.1, relwidth=0.98)
        people_Frame.place(relx=0.01, rely=0.12, relheight=0.2, relwidth=0.98)
        date_Frame.place(relx=0.01, rely=0.33, relheight=0.1, relwidth=0.98)
        time_Frame.place(relx=0.01, rely=0.44, relheight=0.2, relwidth=0.98)
        place_Frame.place(relx=0.01, rely=0.65, relheight=0.1, relwidth=0.98)
        notices_Frame.place(relx=0.01, rely=0.76, relheight=0.2, relwidth=0.98)

        close_Button.place(relx=0.95, rely=0.5, anchor=CENTER)
        delete_Button.place(relx=0.89, rely=0.5, anchor=CENTER, relwidth=0.05)
        change_Button.place(relx=0.95, rely=0.8, anchor=CENTER, relwidth=0.07)


    def change_icon(todo):
        global y_finish, y_not_finish

        # change the icon of the task to finished / unfinished
        if todo.done == 0:
            todo.CTk_Button_finished_all.configure(image=finished)
            todo.CTk_Button_finished_finish.configure(image=finished)
            todo.CTk_Button_finished_not_finish.configure(image=finished)
            todo.task_finished()
            place_buttons()

        else:
            todo.CTk_Button_finished_all.configure(image=unfinished)
            todo.CTk_Button_finished_finish.configure(image=unfinished)
            todo.CTk_Button_finished_not_finish.configure(image=unfinished)
            todo.task_unfinished()
            place_buttons()


    def place_all_buttons(todo):
        global y_all, y_finish, y_not_finish

        if todo.done == 1:
            # create the new buttons in the class
            todo.create_but(tabview, show_info, change_icon, finished, todo.title, todo)
        else:
            # create the new buttons in the class
            todo.create_but(tabview, show_info, change_icon, unfinished, todo.title, todo)


    def new_todo():
        global to_load

        n = add_todo()
        todo1 = Todo(n[2], n[1], n[3], n[4], n[5], n[6], n[0])

        place_all_buttons(todo1)
        to_load.append(todo1)

        place_buttons()
        place_buttons_all()


    # initialize todo_list
    todo_list_Frame = CTkFrame(
        master=root,
    )
    todo_list_Frame.place(relx=0.02, rely=0.02, relheight=0.9)

    tabview = CTkTabview(
        master=todo_list_Frame, width=180,
    )
    tabview.place(relx=0.05, rely=0, relheight=0.98)
    tabview.add('unfinished')
    tabview.add('finished')
    tabview.add('all')

    # initialize add_todo
    add_todo_Frame = CTkFrame(
        master=root,
    )
    add_todo_Frame.place(relx=0.02, rely=0.94, relheight=0.05)

    # initialize new todo_Button
    add_todo_Button = CTkButton(
        master=add_todo_Frame,
        text='add TODO',
        font=('', 20),
        image=add,
        text_color='black',
        compound=LEFT,
        command=new_todo
    )
    add_todo_Button.place(x=0, y=0, relheight=1, relwidth=1)

    # load all todos
    to_load = load_todos()
    print(to_load)

    # place a button for every task
    for todo in to_load:
        place_all_buttons(todo)

    place_buttons()

    place_buttons_all()

    root.mainloop()


