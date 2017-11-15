from ui import UI

"""
This is the file that turn on the application.
"""


def start_application():
    """
    This method will create an UI object and will start the application.
    :return:
    """
    ui = UI.UI()
    ui.main_menu()


start_application()
