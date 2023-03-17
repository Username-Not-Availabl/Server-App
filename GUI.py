import customtkinter
class GUI(customtkinter.CTkBaseClass):
# class GUI(tk.Tk):

    def __new__(cls):
        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("dark-blue")

        GUI.instance = customtkinter.CTk()
        return super()

    @classmethod
    def init(cls, title = "Application v0.0.0 Alpha", dimensions = (300, 200), offsets = (0, 0)):
        cls()
        GUI.instance.title(title)

        GUI.instance.width, GUI.instance.height = dimensions
        GUI.instance.offset_x, GUI.instance.offset_y = offsets
        GUI.instance.geometry(f"{GUI.instance.width}x{GUI.instance.height} + {GUI.instance.offset_x} + {GUI.instance.offset_y}")
    
 
    @staticmethod
    def attach(cls, **class_arguments):
        GUI.current_branch = cls(**class_arguments)
        class extension:
            def _with(self, **arguments):
                GUI.current_branch.pack(**arguments)
                return GUI.current_branch

        return extension()
    
    @classmethod
    def run(cls):
        GUI.instance.mainloop()
