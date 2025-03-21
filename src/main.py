import flet as ft

def main(page: ft.Page):
    # Set window size and title
    page.title = "Minimalist Chat UI"
    page.window_width = 400
    page.window_height = 500
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=["#f5f7fa", "#c3cfe2"],
    )

    # Chat messages container
    messages = ft.Column(
        spacing=10,
        expand=True,
        scroll=ft.ScrollMode.AUTO,
    )

    # Function to handle sending messages
    def send_message(e):
        if message_input.value.strip():
            # Simplified message rendering for troubleshooting
            messages.controls.append(
                ft.Text(
                    message_input.value,
                    size=16,
                    color="#000000",  # Black text for visibility
                )
            )
            messages.controls.append(
                ft.Text(
                    "This is a placeholder reply.",
                    size=16,
                    color="#000000",  # Black text for visibility
                )
            )
            message_input.value = ""
            page.update()  # Ensure the page is updated to reflect changes

    # Text input field
    message_input = ft.TextField(
        hint_text="Type your message...",
        expand=True,
        border_radius=ft.border_radius.all(20),
        bgcolor="#ffffff",
        text_size=14,
        on_submit=send_message,  # Send message on Enter key press
    )

    # Settings icon
    settings_icon = ft.IconButton(
        icon=ft.Icons.SETTINGS,
        icon_size=20,
        tooltip="Settings",
    )

    # Input row containing the text field and buttons
    input_row = ft.Row(
        controls=[
            message_input,
            settings_icon,
            ft.ElevatedButton(
                text="Send",
                on_click=send_message,
                height=40,
                bgcolor="#4CAF50",
                color="white",
            ),
        ],
        spacing=10,
    )

    # Add components to the page
    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    content=messages,
                    expand=True,
                    padding=ft.padding.all(10),
                ),
                ft.Container(
                    content=input_row,
                    padding=ft.padding.symmetric(horizontal=10, vertical=5),
                    bgcolor="#f0f0f0",
                    border_radius=ft.border_radius.all(10),
                ),
            ],
            expand=True,
        )
    )

ft.app(main)