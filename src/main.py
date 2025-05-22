import json
import threading
from time import sleep
import time
from searcher import OsuSearcher
from songlist import SongList
from credits import Credits
from sidebar import Sidebar
import flet as ft

searcher = OsuSearcher("/media/guhw/guhw/osu-wine/osu!")

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

def cool_time(total):
    minutes = total // 60
    seconds = total % 60
    return f"{minutes:02}:{seconds:02}"

def save_all(page: ft.Page):
    page.client_storage.set("guhw.ofm.id_cache",json.dumps(searcher.id_cache))
    page.client_storage.set("guhw.ofm.folder_cache",json.dumps(searcher.folder_cache))

def load_all(page: ft.Page):
    try:
        searcher.id_cache = json.loads(page.client_storage.get("guhw.ofm.id_cache"))
        searcher.folder_cache = json.loads(page.client_storage.get("guhw.ofm.folder_cache"))
    except:
        searcher.id_cache = {}
        searcher.folder_cache = {}


def main(page: ft.Page):
    load_all(page)
    page.title = "osu!fm"
    page.window.min_height = 600
    page.window.min_width = 1200

    page.appbar = ft.AppBar(
        leading=ft.Image(
            src="images/icon.png",
        ),
        title=ft.Text("osu!fm"),
        center_title=False,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
    )
    song_list = SongList(play_handler,favorite_handler)
    pages = [
        song_list,
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
    
    for i in searcher.id_cache.keys():
        song_list.add_song(i,searcher.id_cache[i]["title"],searcher.id_cache[i]["artist"],cool_time(searcher.id_cache[i]["length"]))
    
    def scanning_thread():
        global searcher
        last = time.time()
        new = []
        page.appbar.title = ft.Text("osu!fm (Searching songs)")
        page.update()
        while len(searcher.queue) > 0:
            new_id = searcher.step()
            if new_id:
                new.append(new_id)
            if time.time()-last > 1:
                for i in new:
                    song_list.add_song(i,searcher.id_cache[i]["title"],searcher.id_cache[i]["artist"],cool_time(searcher.id_cache[i]["length"]))
                
                song_list.update()
                page.appbar.title = ft.Text(f"osu!fm (Searching {len(searcher.queue)} songs)")
                page.update()
                last = time.time()
                save_all(page)
            sleep(0.01)
        page.appbar.title = ft.Text(f"osu!fm")
        page.update()
    threading.Thread(target=scanning_thread, daemon=True).start()

ft.app(target=main)