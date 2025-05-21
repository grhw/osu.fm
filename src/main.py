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
    
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=200,
        min_extended_width=200,
        leading=ft.Column(
            [
                ft.Text("Title",text_align=ft.TextAlign.CENTER,width=200,weight=ft.FontWeight.BOLD,size=20),
                ft.Text("Artist",text_align=ft.TextAlign.CENTER,width=200),
                ft.Row(
                    [
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
        ),
        group_alignment=-0.9,
        destinations=[
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
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )
    
    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column(
                    [ft.Text("Body!")],
                    alignment=ft.MainAxisAlignment.START,
                    expand=True,
                ),
            ],
            expand=True,
        )
    )


ft.app(target=main)