import tkinter as tk
import customtkinter as ctk
import pyperclip

# Initialize CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Caesar Cipher Encrypt
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Caesar Cipher Decrypt
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Encrypt text
def encrypt_text():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        output_entry.delete("1.0", tk.END)
        output_entry.insert("1.0", "Please enter some text!")
        return
    try:
        shift = int(shift_entry.get())
    except ValueError:
        output_entry.delete("1.0", tk.END)
        output_entry.insert("1.0", "Invalid shift! Please enter a number.")
        return
    encrypted_text = caesar_encrypt(text, shift)
    output_entry.delete("1.0", tk.END)
    output_entry.insert("1.0", encrypted_text)

# Decrypt text
def decrypt_text():
    text = output_entry.get("1.0", tk.END).strip()
    if not text:
        output_entry.delete("1.0", tk.END)
        output_entry.insert("1.0", "Please encrypt text first!")
        return
    try:
        shift = int(shift_entry.get())
    except ValueError:
        output_entry.delete("1.0", tk.END)
        output_entry.insert("1.0", "Invalid shift! Please enter a number.")
        return
    decrypted_text = caesar_decrypt(text, shift)
    output_entry.delete("1.0", tk.END)
    output_entry.insert("1.0", decrypted_text)

# Copy output to clipboard
def copy_to_clipboard():
    pyperclip.copy(output_entry.get("1.0", tk.END).strip())

# Reset fields
def reset_fields():
    text_entry.delete("1.0", tk.END)
    output_entry.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)

# Initialize the main window
app = ctk.CTk()
app.title("Caesar Cipher")
app.geometry("450x550")

# Title and Shift Section
title_label = ctk.CTkLabel(app, text="---Caesar Cipher---", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

shift_frame = ctk.CTkFrame(app, fg_color="transparent")
shift_frame.pack(pady=10)

shift_label = ctk.CTkLabel(shift_frame, text="Input Key:", font=("Arial", 16))
shift_label.pack(side=tk.LEFT, padx=5)

shift_entry = ctk.CTkEntry(shift_frame, width=120, font=("Arial", 14))
shift_entry.pack(side=tk.LEFT, padx=10)

# Text Entry Section
text_label = ctk.CTkLabel(app, text="Enter Your Text", font=("Arial", 16))
text_label.pack(pady=10)

text_entry = ctk.CTkTextbox(app, width=400, height=100, font=("Arial", 12))
text_entry.pack(pady=10)

# Buttons for Encrypt/Decrypt
button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.pack(pady=10)

encrypt_button = ctk.CTkButton(button_frame, text="Encrypt", command=encrypt_text, font=("Arial", 14), width=100)
encrypt_button.grid(row=0, column=0, padx=10, pady=5)

decrypt_button = ctk.CTkButton(button_frame, text="Decrypt", command=decrypt_text, font=("Arial", 14), width=100)
decrypt_button.grid(row=0, column=1, padx=10, pady=5)

# Output Section
output_label = ctk.CTkLabel(app, text="Output Text", font=("Arial", 16))
output_label.pack(pady=10)

output_entry = ctk.CTkTextbox(app, width=400, height=100, font=("Arial", 12))
output_entry.pack(pady=10)

# Copy and Reset Buttons
copy_button = ctk.CTkButton(app, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 14), width=180)
copy_button.pack(pady=10)

reset_button = ctk.CTkButton(app, text="Reset", command=reset_fields, font=("Arial", 14), width=180)
reset_button.pack(pady=10)

app.mainloop()
