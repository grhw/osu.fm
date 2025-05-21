import flet as ft

class Song(ft.Row):
    def __init__(self,title,artist,length):
        super().__init__()
        self.controls = [
            ft.IconButton(ft.Icons.ARROW_RIGHT),
            ft.Text(title,weight=ft.FontWeight.BOLD),
            ft.Text(artist),
            ft.Text(length),
            ft.IconButton(ft.Icons.FAVORITE_BORDER),
        ]
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.expand = True

class SongList(ft.ListView):
    def __init__(self):
        super().__init__()
        self.controls = [
            Song("WOW","who","0:00"),
        ]
        self.alignment = ft.alignment.center
        self.expand = True