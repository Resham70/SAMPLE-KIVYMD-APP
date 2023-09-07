from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import BoxLayout

class RoomMaterialsCalculatorApp(MDApp):
    def build(self):
        self.title = "Room Materials Calculator"
        
        # Create the main layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=5)
        
        # Create input fields
        length_label = MDLabel(text="Length:")
        self.length_entry = MDTextField()
        width_label = MDLabel(text="Width:")
        self.width_entry = MDTextField()
        
        # Create calculate button
        calculate_button = MDRaisedButton(text="Calculate", on_release=self.calculate)
        
        # Create output labels
        self.Main_Tee_output_label = MDLabel()
        self.channel_output_label = MDLabel()
        self.wall_angle_output_label = MDLabel()
        self.four_foot_channel_output_label = MDLabel()
        self.two_foot_channel_output_label = MDLabel()
        self.board_needed_output_label = MDLabel()
        
        # Add widgets to the layout
        layout.add_widget(length_label)
        layout.add_widget(self.length_entry)
        layout.add_widget(width_label)
        layout.add_widget(self.width_entry)
        layout.add_widget(calculate_button)
        layout.add_widget(self.Main_Tee_output_label)
        #layout.add_widget(self.channel_output_label)
        layout.add_widget(self.wall_angle_output_label)
        layout.add_widget(self.four_foot_channel_output_label)
        layout.add_widget(self.two_foot_channel_output_label)
        layout.add_widget(self.board_needed_output_label)
        
        return layout
    
    def calculate(self, *args):
        # Get user input from text fields
        length = float(self.length_entry.text)
        width = float(self.width_entry.text)

        # Calculate square footage of room
        sq_ft = length * width

        # Calculate length of 12-foot channel needed
        Main_Tee_length = (length / 4) * width / 12

        # Calculate length of 12-foot channel needed
       # channel_length = (width / 4) * length / 12

        # Calculate length of 10-foot wall angle needed
        wall_angle_length = (length + width) * 2 / 10

        # Calculate length of 4-foot channel needed
        four_foot_channel_length = (length / 2) * (width / 4)

        # Calculate length of 2-foot channel needed
        two_foot_channel_length = ((length / 2) + 1) * (width / 4)

        # Calculate board needed
        board_needed = (length * width) / 4

        # Update output labels
        self.Main_Tee_output_label.text = f"12-feet main tee needed: {Main_Tee_length:.2f} pieces"
       # self.channel_output_label.text = f"12-feet channel needed: {channel_length:.2f} pieces"
        self.wall_angle_output_label.text = f"10-foot wall angle needed: {wall_angle_length:.2f} pieces"
        self.four_foot_channel_output_label.text = f"4-long cross tee needed: {four_foot_channel_length:.2f} pieces"
        self.two_foot_channel_output_label.text = f"2-short cross tee needed: {two_foot_channel_length:.2f} pieces"
        self.board_needed_output_label.text = f"2/2 board needed: {board_needed:.2f} pieces"

if name == "main":
    RoomMaterialsCalculatorApp().run()