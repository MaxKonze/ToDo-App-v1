from customtkinter import CTkFrame, CTkLabel


def create_all_elements(root):
    show_Frame = CTkFrame(
        root
    )

    title_Frame = CTkFrame(
        show_Frame
    )

    people_Frame = CTkFrame(
        show_Frame
    )

    date_Frame = CTkFrame(
        show_Frame
    )

    time_Frame = CTkFrame(
        show_Frame
    )

    place_Frame = CTkFrame(
        show_Frame
    )

    notices_Frame = CTkFrame(
        show_Frame
    )

    show_title = CTkLabel(
        title_Frame,
        font=('', 30),
        fg_color="transparent",
        padx=10
    )

    show_people = CTkLabel(
        people_Frame,
        font=('', 20),
        fg_color="transparent",
        padx=10
    )

    show_people2 = CTkLabel(
        people_Frame,
        font=('', 20),
        fg_color="transparent",
        padx=10
    )

    show_date = CTkLabel(
        date_Frame,
        font=('', 30),
        fg_color="transparent",
        padx=10
    )

    show_time = CTkLabel(
        time_Frame,
        font=('', 30),
        fg_color="transparent",
        padx=10,
        text=''
    )

    show_place = CTkLabel(
        place_Frame,
        font=('', 30),
        fg_color="transparent",
        padx=10
    )

    show_notes = CTkLabel(
        notices_Frame,
        font=('', 20),
        fg_color="transparent",
        padx=10,
        justify="left"
    )

    return [show_Frame, title_Frame, people_Frame, date_Frame, time_Frame, place_Frame, notices_Frame, show_title,
            show_people, show_people2, show_date, show_time, show_place, show_notes]
