import flet as ft

class SongPlayer(ft.Column):
    def __init__(self,repeat,back,play_pause,skip,volume):
        super().__init__()
        self.repeat = repeat
        
        self.buttons = ft.Row(
                [
                    self.repeat,
                    ft.IconButton(
                        icon=ft.Icons.CHEVRON_LEFT, on_click=lambda z: back()
                    ),
                    ft.IconButton(
                        icon=ft.Icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda z: play_pause()
                    ),
                    ft.IconButton(
                        icon=ft.Icons.CHEVRON_RIGHT, on_click=lambda z: skip()
                    )
                ], alignment=ft.MainAxisAlignment.CENTER, width=200
            )
        
        self.volume = ft.Slider(25,min=0,max=100,label="Volume",on_change=lambda z: volume(self.volume.value))
        self.progress = ft.ProgressBar(width=200,value=0)
        self.controls = []
        self.set("Title","Artist")
        
    
    def set(self,title,artist):
        self.controls = [
            self.volume,
            ft.Text(title,text_align=ft.TextAlign.CENTER,width=200,weight=ft.FontWeight.BOLD,size=20),
            ft.Text(artist,text_align=ft.TextAlign.CENTER,width=200),
            self.buttons,
            self.progress
        ]

class Sidebar(ft.NavigationRail):
    def __init__(self,selected_index,on_change, repeat_toggle,back,play_pause,skip,volume):
        super().__init__(selected_index=selected_index)
        self.label_type = ft.NavigationRailLabelType.ALL
        self.min_width = 200
        self.min_extended_width = 200
        self.repeat = ft.IconButton(
            icon=ft.Icons.REPEAT, on_click=lambda z: repeat_toggle(self.repeat)
        )
        self.leading = SongPlayer(self.repeat,back,play_pause,skip,volume)
        
        self.destinations = [
            ft.NavigationRailDestination(
                icon=ft.Icons.MUSIC_NOTE_OUTLINED,
                selected_icon=ft.Icons.MUSIC_NOTE,
                label="Songs",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.FAVORITE_BORDER,
                selected_icon=ft.Icons.FAVORITE,
                label="Credits",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ]
        
        self.on_change = on_change