import flet as ft
from flet import Icons, Colors

def main(page: ft.Page):
    page.title = "Static Flet UI"
    page.window_width = 400
    page.window_height = 800
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Simulated mobile screen content
    mobile_screen = ft.Container(
        width=300,
        height=600,
        border_radius=30,
        bgcolor=Colors.WHITE,
        border=ft.border.all(1, Colors.GREY_300),
        padding=20,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                # Row with image and text aligned to the left
                ft.Row(
                    alignment=ft.MainAxisAlignment.START,  # Align to the left
                    spacing=10,
                    controls=[
                        ft.Image(
                            src="icon.png",
                            width=50,
                            height=30,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Text("Dinah Lyn M.Pelimer ", size=16, weight="bold")
                    ]
                ),
               
                # Bottom static navigation
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        ft.Column(controls=[ft.Icon(Icons.HOME), ft.Text("Home", size=12)]),
                        ft.Column(controls=[ft.Icon(Icons.CHAT), ft.Text("Chat", size=12)]),
                        ft.Column(controls=[ft.Icon(Icons.SETTINGS), ft.Text("Settings", size=12)]),
                    ]
                )
            ]
        )
    )

    page.add(mobile_screen)

ft.app(target=main)
