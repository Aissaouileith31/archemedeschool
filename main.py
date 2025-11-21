import flet as ft 

import flet as ft
from app_file.pages.login import login
from app_file.pages.home_page import home

def main_location(page: ft.Page):
    page.session.set("username", None)

    def route_change(e):
        page.clean()
        print("🔄 Route changed to:", page.route)

        try:
            if page.route == "/":
                login(page)
            elif page.route == "/home":
                username = page.session.get("username")
                if username is None:
                    print("⚠️ No username found, redirecting to login")
                    page.go("/")
                    return
                home(page, username)
            else:
                page.add(ft.Text("404: Page not found"))
        except Exception as ex:
            print("Error:", ex)

    # 🔹 Assign route change function BEFORE navigating
    page.on_route_change = route_change

    # 🔹 Go to the current route at startup
    page.go(page.route)



ft.app(target=main_location, assets_dir="assets/")
