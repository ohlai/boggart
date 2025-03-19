import tkinter as tk
from tkinter import scrolledtext
import customtkinter as ctk

class ChatInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Boggart Chat")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e1e")

        self.chat_frame = ctk.CTkFrame(self.root, width=780, height=500, corner_radius=15, fg_color="#2e2e2e")
        self.chat_frame.pack(pady=10)

        self.chat_display = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD, bg="#2e2e2e", fg="#ffffff", font=("Helvetica", 12), state=tk.DISABLED)
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.input_frame = ctk.CTkFrame(self.root, width=780, height=50, corner_radius=15, fg_color="#2e2e2e")
        self.input_frame.pack(pady=10)

        self.user_input = ctk.CTkEntry(self.input_frame, width=680, height=40, corner_radius=15, fg_color="#3e3e3e", text_color="#ffffff", font=("Helvetica", 12))
        self.user_input.pack(side=tk.LEFT, padx=10, pady=5)

        self.send_button = ctk.CTkButton(self.input_frame, text="Send", width=80, height=40, corner_radius=15, fg_color="#6a0dad", text_color="#ffffff", font=("Helvetica", 12), command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=10, pady=5)

    def send_message(self):
        user_message = self.user_input.get()
        if user_message:
            self.display_message(user_message, "user")
            self.user_input.delete(0, tk.END)
            # Here you would add the code to send the message to the AI and get the response
            ai_response = "This is a placeholder response from Boggart."
            self.display_message(ai_response, "ai")

    def display_message(self, message, sender):
        self.chat_display.config(state=tk.NORMAL)
        if sender == "user":
            self.chat_display.insert(tk.END, f"User: {message}\n", "user")
        else:
            self.chat_display.insert(tk.END, f"Boggart: {message}\n", "ai")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.yview(tk.END)

if __name__ == "__main__":
    root = ctk.CTk()
    chat_interface = ChatInterface(root)
    root.mainloop()
