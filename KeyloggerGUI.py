import customtkinter as ctk
from Keylogger import KeyloggerEngine
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.engine = KeyloggerEngine()
        self.engine.set_callback(self.update_live_display)

        self.title("VOIS Cybersecurity Lab")
        self.geometry("500x650")

        # UI Components
        self.label = ctk.CTkLabel(self, text="Keystroke Monitor Pro", font=("Roboto", 24, "bold"))
        self.label.pack(pady=20)

        # Live Display Area
        self.text_area = ctk.CTkTextbox(self, width=420, height=200, corner_radius=10, font=("Consolas", 12))
        self.text_area.pack(pady=10)
        self.text_area.configure(state="disabled")

        # Status Display
        self.status_frame = ctk.CTkFrame(self, width=420, height=50)
        self.status_frame.pack(pady=10)
        self.status_text = ctk.CTkLabel(self.status_frame, text="Ready for Analysis", text_color="#3498db")
        self.status_text.place(relx=0.5, rely=0.5, anchor="center")

        # Control Buttons
        self.start_btn = ctk.CTkButton(self, text="▶ START SESSION", command=self.start_rec, 
                                       fg_color="#2ecc71", hover_color="#27ae60", font=("Roboto", 14, "bold"))
        self.start_btn.pack(pady=10)

        self.stop_btn = ctk.CTkButton(self, text="■ STOP & ANALYZE", command=self.stop_rec, 
                                      fg_color="#e74c3c", hover_color="#c0392b", font=("Roboto", 14, "bold"))
        self.stop_btn.pack(pady=10)

        self.folder_btn = ctk.CTkButton(self, text="📂 OPEN LOGS", command=self.engine.open_log_folder, 
                                        fg_color="transparent", border_width=2)
        self.folder_btn.pack(pady=10)

        self.footer = ctk.CTkLabel(self, text="Internship Project: Generative AI & Cybersecurity", font=("Roboto", 10), text_color="gray")
        self.footer.pack(side="bottom", pady=15)

    def update_live_display(self, key):
        clean_key = key.replace("Key.", " ").replace("'", "")
        self.text_area.configure(state="normal")
        self.text_area.insert("end", f"{clean_key}")
        self.text_area.see("end")
        self.text_area.configure(state="disabled")

    def start_rec(self):
        self.text_area.configure(state="normal")
        self.text_area.delete("1.0", "end")
        self.text_area.configure(state="disabled")
        self.engine.start()
        self.status_text.configure(text="● MONITORING ACTIVE", text_color="#2ecc71")

    def stop_rec(self):
        stats = self.engine.stop()
        self.status_text.configure(text="SESSION ARCHIVED", text_color="#3498db")
        
        # Show professional analytics popup
        if stats:
            report = (f"Session Analytics:\n\n"
                      f"Total Keystrokes: {stats['total_keys']}\n"
                      f"Typing Speed: {stats['wpm']} WPM\n"
                      f"Duration: {stats['duration']} seconds")
            messagebox.showinfo("Security Report", report)

if __name__ == "__main__":
    app = App()
    app.mainloop()