from searcher import OsuSearcher
from songlist import SongList
from credits import Credits
from sidebar import Sidebar
import flet as ft

cur_ind = 0
def play_handler(id):
    print("play",id)

def favorite_handler(id):
    print("favorite",id)


def repeat_toggle(button):
    print("repeat toggle",button)

def back():
    print("back")

def play_pause():
    print("play/pause")

def skip():
    print("skip")

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
    
    pages = [
        SongList(play_handler,favorite_handler),
        Credits()
    ]
    
    def page_change(data):
        global cur_ind
        ind = int(data.data)
        pages[cur_ind].visible = False
        pages[ind].visible = True
        pages[ind].update()
        pages[cur_ind].update()
        cur_ind = ind
    
    content = ft.Row(
            [
                Sidebar(0,page_change, repeat_toggle,back,play_pause,skip),
                ft.VerticalDivider(width=1),
            ],
            expand=True,
        )
    
    for i in pages:
        i.visible = False
        content.controls.append(i)
    
    page.add(
        content
    )
    pages[0].visible = True
    pages[0].update()
    


ft.app(target=main)