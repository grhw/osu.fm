import flet as ft

class Song(ft.Row):
    def __init__(self,id,title,artist,length,play_handler,favorite_handler):
        super().__init__()
        self.controls = [
            ft.IconButton(ft.Icons.ARROW_RIGHT,on_click=lambda z: play_handler(id)),
            ft.Text(title,weight=ft.FontWeight.BOLD),
            ft.Text(artist),
            ft.Text(length),
            ft.IconButton(ft.Icons.FAVORITE_BORDER,on_click=lambda z: favorite_handler(id)),
        ]
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.expand = True

class SongList(ft.ListView):
    def __init__(self,play_handler,favorite_handler):
        super().__init__()
        self.controls = []
        self.alignment = ft.alignment.center
        self.expand = True
        self.play = play_handler
        self.favorite = favorite_handler
    
    def add_song(self,id,title,artist,length):
        self.controls.append(
            Song(id,title,artist,length,self.play,self.favorite)
        )