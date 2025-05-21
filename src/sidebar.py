import flet as ft

class Sidebar(ft.NavigationRail):
    def __init__(self,selected_index,on_change):
        super().__init__(selected_index=selected_index)
        self.label_type = ft.NavigationRailLabelType.ALL
        self.min_width = 200
        self.min_extended_width = 200
        self.leading = ft.Column(
            [
                ft.Slider(25,min=0,max=100,label="Volume"),
                ft.Text("Title",text_align=ft.TextAlign.CENTER,width=200,weight=ft.FontWeight.BOLD,size=20),
                ft.Text("Artist",text_align=ft.TextAlign.CENTER,width=200),
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.Icons.REPEAT
                        ),
                        ft.IconButton(
                            icon=ft.Icons.CHEVRON_LEFT
                        ),
                        ft.IconButton(
                            icon=ft.Icons.PLAY_CIRCLE_FILL_OUTLINED
                        ),
                        ft.IconButton(
                            icon=ft.Icons.CHEVRON_RIGHT
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER, width=200
                ),
                ft.ProgressBar(width=200,value=0),
            ]
        )
        
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