import flet as ft
from screenshot_query import take_screenshot, send_query_with_screenshot


def main(page: ft.Page):
    # Set window size and title
    page.title = "Boggart"
    page.window.width = 500
    page.window.height = 600
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.icon = "assets/icon.png"
    
    page.bgcolor = ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=["#f5f7fa", "#c3cfe2"],
    )

    # Chat messages container
    messages = ft.Column(
        spacing=10,
        expand=True,
        scroll=ft.ScrollMode.AUTO,  # Enable scrolling
    )

    # Function to adjust the blank container height
    def adjust_blank_space():
        # Calculate the height dynamically
        blank_space_height = max(0, page.window.height - (len(messages.controls) * 60))  # Adjust 50 based on message height
        if len(messages.controls) > 0 and isinstance(messages.controls[-1], ft.Container):
            messages.controls[-1].height = blank_space_height
        else:
            messages.controls.append(ft.Container(height=blank_space_height))
        page.update()

    # Function to handle sending messages
    def send_message(e):
        if message_input.value.strip():
            user_message = message_input.value
            message_input.value = ""
            # User message aligned to the right
            messages.controls.insert(-1,
                ft.Row(
                    controls=[
                        ft.Container(
                            ft.Container(
                                content=ft.Text(
                                    user_message,
                                    size=16,
                                    color="#000000",
                                    selectable=True,
                                ),
                                bgcolor="#f0e4ff",  
                                border_radius=ft.border_radius.all(15),  # Rounded corners
                                padding=ft.padding.all(10),  # Padding inside the container
                            ),
                            padding=ft.padding.only(left=50),  # Padding for the background
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    wrap=True,
                    width=page.window.width,
                    key="1",
                )
            )

            # Adjust the blank space at the bottom
            adjust_blank_space()

            # Display loading indicator
            messages.controls.insert(-1,
                ft.Row(
                    controls=[
                        ft.Container(
                            ft.ProgressRing(width=20, height=20, color="#875ae6", tooltip="Thinking..."),
                            padding=ft.padding.only(left=20),
                        )
                    ],
                    wrap=True,
                    width=page.window.width,
                    alignment=ft.MainAxisAlignment.START,
                )
            )

            messages.scroll_to(key="1", duration=500)

            page.update()

            # Take a screenshot and send the query with the screenshot
            try:
                screenshot = take_screenshot()
                response = send_query_with_screenshot(user_message, screenshot)

                # Stream and display the response as it is generated
                reply = ""
                for chunk in response:
                    for choice in chunk.choices:
                        if choice.finish_reason != "stop":
                            messages.controls.pop(-2)
                            reply += choice.delta.content

                            # Display the reply aligned to the left
                            messages.controls.insert(-1,
                                ft.Row(
                                    controls=[
                                        ft.Markdown(
                                            reply,
                                            selectable=True,
                                            extension_set="gitHubWeb",
                                            #code_theme="atom-one-dark",
                                        )
                                    ],
                                    wrap=True,
                                    width=page.window.width,
                                    alignment=ft.MainAxisAlignment.START,
                                )
                            )

                            
                            page.update()
                            
            except Exception as ex:
                # Display error message
                messages.controls.insert(-1,
                    ft.Row(
                        controls=[
                            ft.Text(
                                f"Error: {ex}",
                                size=16,
                                color="#ff0000",
                                selectable=True,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    )
                )
            finally:
                page.update()

    # Text input field
    message_input = ft.TextField(
        hint_text="Type your message...",
        expand=True,
        border_radius=ft.border_radius.all(20),
        border_width=0,
        bgcolor="#ffffff",
        text_size=14,
        on_submit=send_message,
        multiline=True,
        min_lines=1,
        max_lines=12,
        shift_enter=True,
        border=None,  
    )

    # Settings icon
    #settings_icon = ft.IconButton(
     #   icon=ft.Icons.SETTINGS,
    #    icon_size=20,
    #    tooltip="Settings",
    #)

    # Input row containing the text field and buttons
    input_row = ft.Row(
        controls=[
            message_input,
            #settings_icon,
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
                    #bgcolor="#f0f0f0",
                    border_radius=ft.border_radius.all(30),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.Colors.GREY,
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                     )
                ),
            ],
            expand=True,
        )
    )

ft.app(main)