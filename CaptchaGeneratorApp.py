import tkinter as tk
from tkinter import messagebox
import random
import string

class CaptchaGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Captcha Generator")
        self.root.geometry("350x200")
        self.root.configure(bg="#826afb")

        self.captcha_text = tk.StringVar()
        self.captcha_input = tk.StringVar()

        self.create_widgets()
        self.generate_captcha()

    def create_widgets(self):
        header = tk.Label(self.root, text="Captcha Generator", bg="#826afb", fg="#333", font=("Poppins", 18, "bold"))
        header.pack(pady=10)

        captcha_frame = tk.Frame(self.root, bg="#fff", bd=2, relief="solid")
        captcha_frame.pack(pady=10)

        self.captcha_label = tk.Entry(captcha_frame, textvariable=self.captcha_text, font=("Poppins", 16), state="readonly", readonlybackground="#fff", fg="#6b6b6b")
        self.captcha_label.grid(row=0, column=0, padx=5, pady=5)

        refresh_button = tk.Button(captcha_frame, text="↻", command=self.generate_captcha, bg="#826afb", fg="#fff", font=("Poppins", 16), bd=0)
        refresh_button.grid(row=0, column=1, padx=5, pady=5)

        input_label = tk.Entry(self.root, textvariable=self.captcha_input, font=("Poppins", 16))
        input_label.pack(pady=5)

        submit_button = tk.Button(self.root, text="Submit Captcha", command=self.validate_captcha, bg="#826afb", fg="#fff", font=("Poppins", 16))
        submit_button.pack(pady=5)

        self.message_label = tk.Label(self.root, text="", font=("Poppins", 14), bg="#826afb")
        self.message_label.pack(pady=5)

    def generate_captcha(self):
        captcha = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        self.captcha_text.set('   '.join(captcha))

    def validate_captcha(self):
        entered_text = self.captcha_input.get().replace(" ", "")
        generated_text = self.captcha_text.get().replace(" ", "")

        if entered_text == generated_text:
            self.message_label.config(text="Entered captcha is correct", fg="#826afb")
        else:
            self.message_label.config(text="Entered captcha is not correct", fg="#FF2525")
        self.captcha_input.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = CaptchaGeneratorApp(root)
    root.mainloop()
