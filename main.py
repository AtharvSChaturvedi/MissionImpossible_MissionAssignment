import tkinter as tk
from tkinter import messagebox
from missions import MISSIONS
import pyttsx3

class MissionImpossible:
    def __init__(self,root):
        self.root = root
        self.root.title("Mission Access")
        self.root.geometry("400x200")
        self.root.configure(bg="black")

        self.icon_img=tk.PhotoImage(file="classified_icon.png")
        self.root.iconphoto(False,self.icon_img)

        self.engine=pyttsx3.init()
        self.engine.setProperty('rate',130)

        self.label=tk.Label(root,text="Enter Password:",font=("Arial", 14),fg="red",bg="black")
        self.label.pack(pady=10)

        self.password_entry=tk.Entry(root,show="*",font=("Arial",14))
        self.password_entry.pack(pady=5)
        self.password_entry.focus()

        self.submit_btn = tk.Button(root,text="Unlock Mission",command=self.check_password)
        self.submit_btn.pack(pady=10)

        self.mission_label = tk.Label(root,text="",font=("Arial",12),fg="red",bg="black",wraplength=350)
        self.mission_label.pack(pady=10)

    def say_mission(self,text):
        self.engine.say(text)
        self.engine.runAndWait()

    def check_password(self):
        password=self.password_entry.get()
        found=False

        for agent, data in MISSIONS.items():
            if password==data["password"]:
                mission_text=f"Agent {agent}, your mission, should you choose to accept it: {data['mission']}"
                self.mission_label.config(text=mission_text)
                self.say_mission(mission_text)
                found=True
                break

        if not found:
            messagebox.showerror("Access Denied","Incorrect password! Access denied.")
            self.mission_label.config(text="")
            self.password_entry.delete(0,tk.END)
            self.password_entry.focus()


root=tk.Tk()
mi=MissionImpossible(root)
root.mainloop()
