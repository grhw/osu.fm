import flet as ft

class Credits(ft.ListView):
    def __init__(self):
        super().__init__()
        self.controls = [
            ft.Text("made by @guhw (discord, osu) / guhw.dev"),
        ]
        self.alignment = ft.alignment.center
        self.expand = True