from Utils.Widgets.CustomDialog import CustomDialog


class DialogProvider:

    @staticmethod
    def present_error(message: str, title: str):
        dlg = CustomDialog(message, title)
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

    @staticmethod
    def present_error_modal(message: str, title: str):
        dlg = CustomDialog(message, title)
        dlg.setModal(True)
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")
