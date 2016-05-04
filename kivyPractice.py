# # import App class and Widget class from kivy libraries
# from kivy.app import App
# from kivy.app import Widget
#
# # creating class that inherits from kivy App class
# class HelloWorld(App):
#     # some sort of __init__ for GUI?
#     # build is a method of App class, which we are overriding to return a Widget
#     def build(self):
#         # creating instance of Widget class to store as root in App class
#         # this must be the main window, and is of type Widget
#         self.root = Widget()
#         # returns the window into main so it can be run
#         return self.root
#
# # run must be a method of the App class, as we have not defined run() for HelloWorld
# HelloWorld().run()


from kivy.app import App
from kivy.lang import Builder

# class HelloKv(App):
#     def build(self):
#         # give the main window a title
#         self.title = "Hello Draga's World"
#         # load the kv code from the widget file written, and use it to build the main window
#         self.root = Builder.load_file('widget.kv')
#         return self.root

# HelloKv().run()

class ButtonEventDemo(App):
    def build(self):
       self.title = "Button Event Demo"
       self.root = Builder.load_file('widget.kv')
       return self.root

    def button_pressed(self):
        self.root.ids.first_label.text = "Post Press"

ButtonEventDemo().run()