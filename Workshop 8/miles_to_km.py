from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class MileConverter(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_km.kv')
        Window.size = 600,200

    def handle_up(self):
        current_km = self.root.ids.mile_input.text
        try:
            current_km = int(current_km)
        except ValueError:
                self.root.ids.km_output.color = 1,0,0,1
                self.root.ids.km_output.text = 'Enter a whole number please'
                self.root.ids.mile_input.text = ''
        else:
                self.root.ids.mile_input.text = str(current_km + 1)
                self.root.ids.km_output.text = ""

    def handle_down(self):
        current_km = self.root.ids.mile_input.text
        try:
            current_km = int(current_km)
        except ValueError:
                self.root.ids.km_output.color = 1,0,0,1
                self.root.ids.km_output.text = 'Enter a whole number please'
                self.root.ids.mile_input.text = ''
        else:
                self.root.ids.mile_input.text = str(current_km - 1)
                self.root.ids.km_output.text = ""

    def handle_convert(self):
        try:
            current_miles = int(self.root.ids.mile_input.text)
        except ValueError:
            self.root.ids.km_output.color = 1,0,0,1
            self.root.ids.km_output.text = 'Enter a whole number please'
            self.root.ids.mile_input.text = ''
        else:
            km = current_miles * 1.61
            self.root.ids.km_output.color = 0,1,0,1
            self.root.ids.km_output.text = '{:,.2f}km'.format(float(km))

MileConverter().run()
