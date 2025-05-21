from credits import Credits
from sidebar import Sidebar
from songlist import SongList
import flet as ft

def main(page: ft.Page):
    page.title = "osu!fm"

    page.appbar = ft.AppBar(
        leading=ft.Image(
            src="images/icon.png",
        ),
        title=ft.Text("osu!fm"),
        center_title=False,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
    )
    
    page.add(
        ft.Row(
            [
                Sidebar(0,print),
                ft.VerticalDivider(width=1),
                SongList()
            ],
            expand=True,
        )
    )


ft.app(target=main)