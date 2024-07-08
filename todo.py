from customtkinter import CTkButton
# import inspect
from database import add_todo_to_database


class Todo:

    # init a new TODO_
    def __init__(self, notices, people, place, date, time_start, time_end, title, done=0):
        self.title = title
        self.text = notices,
        self.people = people
        self.place = place
        self.date = date
        self.date_bin = int(date[0:1]) + int(date[3:4])
        self.time_start = time_start
        self.time_end = time_end
        self.done = done
        self.deleted = False
        self.len = None
        self.p1 = None
        self.p2 = None
        self.p3 = None
        self.CTk_Button_all = None
        self.CTk_Button_finished_all = None
        self.CTk_Button_finish = None
        self.CTk_Button_finished_finish = None
        self.CTk_Button_not_finish = None
        self.CTk_Button_finished_not_finish = None

    # delete the task
    def __del__(self):
        # caller = inspect.stack()[1]
        # print(f"Die Funktion wurde von {caller.function} aufgerufen.")

        print(f'deleted "{self.title}"')

        if self.deleted is True:
            return

        self.len = len(self.people)

        if self.len == 3:
            self.p3, self.p2, self.p1 = self.people[0:3]

        elif self.len == 2:
            self.p3 = ''
            self.p1, self.p2 = self.people[0:2]
        elif self.len == 1:
            self.p3 = ''
            self.p2 = ''
            self.p1 = self.people[0]
        else:
            self.p3, self.p2, self.p1 = '', '', ''

        # add task to database
        if type(self.text) is str:
            add_todo_to_database(
                [self.title, self.p1, self.date, self.time_start, self.time_end, self.text, self.place,
                 self.done, self.p2, self.p3])
        else:

            add_todo_to_database(
                [self.title, self.p1, self.date, self.time_start, self.time_end, self.text[0], self.place,
                 self.done, self.p2, self.p3])

    # task is marked as deleted
    def set_del(self):
        print('deleted')
        self.deleted = True

    # task is marked as done
    def task_finished(self):
        self.done = 1

    def task_unfinished(self):
        self.done = 0

    def create_but(self, tabview, func, func1, image, text, instance):
        # creates a new button object
        self.CTk_Button_all = CTkButton(
            master=tabview.tab('all'),
            text='    ' + text,
            command=lambda: func(instance),
            fg_color='#4A4A4A',
            hover_color='#4A4A4A'
        )

        # creates a new finish checkbox
        self.CTk_Button_finished_all = CTkButton(
            master=tabview.tab('all'),
            command=lambda: func1(instance),
            fg_color='#4A4A4A',
            hover_color='#4A4A4A',
            image=image,
            text='',
            corner_radius=0,
        )

        # creates a new button object
        self.CTk_Button_finish = CTkButton(
            master=tabview.tab('finished'),
            text='    ' + text,
            command=lambda: func(instance),
            fg_color='#4A4A4A',
            hover_color='#4A4A4A'
        )

        # creates a new finish checkbox
        self.CTk_Button_finished_finish = CTkButton(
            master=tabview.tab('finished'),
            command=lambda: func1(instance),
            fg_color='#4A4A4A',
            hover_color='#4A4A4A',
            image=image,
            text='',
            corner_radius=0,
        )

        # creates a new button object
        self.CTk_Button_not_finish = CTkButton(
            master=tabview.tab('unfinished'),
            text='    ' + text,
            command=lambda: func(instance),
            fg_color='#4A4A4A',
            hover_color='#4A4A4A'
        )

        # creates a new finish checkbox
        self.CTk_Button_finished_not_finish = CTkButton(
            master=tabview.tab('unfinished'),
            command=lambda: func1(instance),
            fg_color='#4A4A4A',
            hover_color='#4A4A4A',
            image=image,
            text='',
            corner_radius=0,
        )
