import customtkinter
from customtkinter import *
from database import load_contacts, add_contact, remove_contact

dict_people = {
    'p1': [None, 0.22, None],
    'p2': [None, 0.42, None],
    'p3': [None, 0.62, None]
}
all_todos = []


def add_todo():
    ret = None
    contacts = []
    contacts_new = []

    def save():
        nonlocal ret

        # collect the data to return them
        title = title_Entry.get()
        people = [dict_people[p][2] for p in dict_people if dict_people[p][0] is not None]
        notices = notices_Text.get('1.0', 'end')
        place = place_Entry.get()
        date = date_Entry.get()

        # check if the hole day is selected
        if time_hole_day_switch.get() == 1:
            time_start = 'hole'
            time_end = 'hole'
        else:
            time_start = time_start_Entry.get()
            time_end = time_end_Entry.get()

        ret = [title, people, notices, place, date, time_start, time_end]

    def try_save():
        nums = '1234567890'
        nums1 = '1230'

        # check the date the users inputted
        try:
            if len(date_Entry.get()) >= 11:
                raise IndexError
            if date_Entry.get()[2] == '.' and date_Entry.get()[5] == '.' and date_Entry.get()[0] in nums1 and \
                    date_Entry.get()[1] in nums and date_Entry.get()[3] in nums1 and date_Entry.get()[4] in nums and date_Entry.get()[9] in nums and date_Entry.get()[6] in nums and date_Entry.get()[7] in nums and date_Entry.get()[8] in nums:
                save()
                add_win.quit()
            else:
                raise IndexError

                # create a window to enter a valid date
        except IndexError:
            dialog = CTkInputDialog(
                text='Das Datum ist falsch oder nicht in der richtigen Form (z.B. "01.01.2000") \n Bitte gebe ein neues Datum ein:',
                title='Datum ernaut eingeben'
            )

            date_Entry.delete(0, customtkinter.END)
            date_Entry.insert(0, dialog.get_input())

    # change time to hole day or time start to time end
    def change_time():
        if time_hole_day_switch.get() == 1:
            time_end_Entry.place_forget()
            time_start_Entry.place_forget()

        else:
            time_start_Entry.place(relx=0.01, rely=0.4)
            time_end_Entry.place(relx=0.14, rely=0.4)

    # activate the button to save
    def change_state(_):

        if date_Entry.get() != '' and title_Entry.get() != '':
            save_Button.configure(state='normal')

    # delete the placeholder in the notice text box
    def delete_place_holder(_):
        notices_Text.delete('1.0', 'end', )

    # delete a member
    def del_item(instance):
        dict_people[instance][0].place_forget()
        dict_people[instance][0] = None

    # place a new member
    def place_person_button(place):
        global dict_people

        dict_people[place][0] = CTkButton(
            master=main_Frame,
            text=f'{people_combobox_1.get()}',
            command=lambda: del_item(place),
            font=('', 20)
        )
        dict_people[place][0].place(relx=dict_people[place][1], rely=0.2, relwidth=0.18)
        dict_people[place][2] = people_combobox_1.get()

    # trigger the func to place a new person
    def add_person(_=''):

        if remove_checkbox.get() == 1:
            remove_contact(people_combobox_1.get())
            people_combobox_1.set('Teilnehmer')

            contacts_new = []
            for contact_new in load_contacts():
                contacts_new.append(contact_new[0])

            people_combobox_1.configure(values=contacts_new)
            return

        if str(type(_)) == "<class 'tkinter.Event'>":
            add_contact(people_combobox_1.get())
            contacts_new = []
            for contact_new in load_contacts():
                contacts_new.append(contact_new[0])

            print(contacts_new)
            people_combobox_1.configure(values=contacts_new)

        if dict_people['p1'][0] is None:
            place_person_button('p1')
        elif dict_people['p2'][0] is None:
            place_person_button('p2')
        elif dict_people['p3'][0] is None:
            place_person_button('p3')
        else:
            pass

    # create a new window to create a new task and set geo and title
    add_win = CTk()

    add_win.geometry('1280x720')
    add_win.title('neues TODO')

    # initialize a Frame to hold everything
    main_Frame = CTkFrame(
        master=add_win,
    )
    main_Frame.place(relx=0.045, rely=0.025, relheight=0.95, relwidth=0.95)

    icon_Frame = CTkFrame(
        master=add_win,
    )
    icon_Frame.place(relx=0.01, rely=0.025, relheight=0.95, relwidth=0.03)

    # initialize a button to save the content
    save_Button = CTkButton(
        master=main_Frame,
        text='Speichern',
        state='disabled',
        command=try_save
    )

    # initialize a field to enter the title
    title_Entry = CTkEntry(
        master=main_Frame,
        placeholder_text='Title hinzufügen',
        font=('', 25)
    )
    title_Entry.bind('<Key>', change_state)

    for contact in load_contacts():
        contacts.append(contact[0])
    print(contacts)

    # initialize a field to enter the persons
    people_combobox_1 = CTkComboBox(
        master=main_Frame,
        values=contacts,
        font=('', 20),
        command=add_person
    )
    people_combobox_1.set('Teilnehmer')
    people_combobox_1.bind('<Return>', add_person)

    # initialize a field to enter the date
    date_Entry = CTkEntry(
        master=main_Frame,
        placeholder_text='Datum',
        font=('', 20)
    )
    date_Entry.bind('<Key>', change_state)

    # initialize a field to enter the start of the event
    time_start_Entry = CTkEntry(
        master=main_Frame,
        placeholder_text='Beginn',
        font=('', 20)
    )

    # initialize a field to enter the end of the event
    time_end_Entry = CTkEntry(
        master=main_Frame,
        placeholder_text='Ende',
        font=('', 20)
    )

    # initialize a switch to change between the hole day and only a few hours
    time_hole_day_switch = CTkSwitch(
        master=main_Frame,
        command=change_time,
        text='ganztägig',
        font=('', 20)
    )

    # initialize a field to enter the place of the event
    place_Entry = CTkEntry(
        master=main_Frame,
        placeholder_text='Ort',
        font=('', 20)
    )

    # initialize a field to enter notices
    notices_Text = CTkTextbox(
        master=main_Frame,
        font=('', 20),
    )
    notices_Text.insert('0.0', 'Notizen')
    notices_Text.bind('<FocusIn>', delete_place_holder)

    # initialize checkbox to remove contacts
    remove_checkbox = CTkCheckBox(
        master=main_Frame,
        text='Kontakt Entfernungs-Modus',
        font=('', 20)
    )

    # place the content
    save_Button.place(relx=0.01, rely=0.01)
    title_Entry.place(relx=0.01, rely=0.1, relwidth=0.4)
    people_combobox_1.place(relx=0.01, rely=0.2, relwidth=0.2)
    date_Entry.place(relx=0.01, rely=0.3)
    time_start_Entry.place(relx=0.01, rely=0.4)
    time_end_Entry.place(relx=0.14, rely=0.4)
    time_hole_day_switch.place(relx=0.14, rely=0.306)
    place_Entry.place(relx=0.01, rely=0.5, relwidth=0.3)
    notices_Text.place(relx=0.01, rely=0.6, relwidth=0.3, relheight=0.2)
    remove_checkbox.place(relx=0.5, rely=0.1)

    add_win.mainloop()

    # destroy the window
    add_win.destroy()

    # return the information
    return ret
