import flet as ft
from oldmain import take_screenshot, send_query_with_screenshot

def main(page: ft.Page):
    # Set window size and title
    page.title = "Minimalist Chat UI"
    page.window.width = 500
    page.window.height = 600
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
            user_message = message_input.value
            message_input.value = ""
            # User message aligned to the right
            messages.controls.append(
                ft.Row(
                    controls=[
                        ft.Text(
                            user_message,
                            size=16,
                            color="#000000",  # Black text for visibility
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END,  # Align to the right
                )
            )
            page.update()  # Update the page to show the user's message

            # Take a screenshot and send the query with the screenshot
            try:
                screenshot = take_screenshot()
                response = send_query_with_screenshot(user_message, screenshot)

                # Stream and display the response as it is generated
                reply = ""
                for chunk in response:
                    for choice in chunk.choices:
                        if choice.finish_reason != "stop":
                            reply += choice.delta.content
                            page.update()

                # Display the reply aligned to the left
                messages.controls.append(
                    ft.Row(
                        controls=[
                            ft.Text(
                                reply,
                                size=16,
                                color="#000000",  # Black text for visibility
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,  # Align to the left
                    )
                )
            except Exception as ex:
                # Display error message
                messages.controls.append(
                    ft.Row(
                        controls=[
                            ft.Text(
                                f"Error: {ex}",
                                size=16,
                                color="#ff0000",  # Red text for errors
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    )
                )
            finally:
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