import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Function to perform Caesar Cipher encryption or decryption
def perform_caesar_cipher(text, shift_value, operation_mode):
    result_text = ""
    for character in text:
        if character.isalpha():
            ascii_offset = 65 if character.isupper() else 97
            if operation_mode == "encrypt":
                result_text += chr((ord(character) - ascii_offset + shift_value) % 26 + ascii_offset)
            elif operation_mode == "decrypt":
                result_text += chr((ord(character) - ascii_offset - shift_value + 26) % 26 + ascii_offset)
        else:
            result_text += character  # Non-alphabetical characters remain unchanged
    return result_text

# Function to handle the process button click event
def handle_process_button():
    input_text = input_text_area.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Warning", "Please enter text to process.")
        return

    try:
        shift_value = int(shift_selection.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid shift value. Please select a number.")
        return

    operation_mode = operation_mode_selection.get()
    processed_text = perform_caesar_cipher(input_text, shift_value, operation_mode)
    output_text_area.config(state="normal")
    output_text_area.delete("1.0", tk.END)
    output_text_area.insert(tk.END, processed_text)
    output_text_area.config(state="disabled")

# Function to save processed text to a file
def save_result_to_file():
    processed_text = output_text_area.get("1.0", tk.END).strip()
    if not processed_text:
        messagebox.showwarning("Warning", "No processed text to save.")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if save_path:
        try:
            with open(save_path, "w") as file:
                file.write(processed_text)
            messagebox.showinfo("Success", f"File saved successfully at {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save the file: {e}")

# Function to clear all fields
def clear_all_fields():
    input_text_area.delete("1.0", tk.END)
    output_text_area.config(state="normal")
    output_text_area.delete("1.0", tk.END)
    output_text_area.config(state="disabled")
    shift_selection.set("3")
    operation_mode_selection.set("encrypt")

# Function to load text from a file into the input area
def load_text_from_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                file_content = file.read()
                input_text_area.delete("1.0", tk.END)
                input_text_area.insert(tk.END, file_content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open the file: {e}")

# Setting up the main application window
app_window = tk.Tk()
app_window.title("Caesar Cipher Encryption/Decryption Tool")
app_window.geometry("750x600")
app_window.configure(bg="#87CEEB")  # Sky blue background

# Center the application window
app_window.eval('tk::PlaceWindow . center')

# Create a frame to center all widgets
center_frame = tk.Frame(app_window, bg="#87CEEB")
center_frame.pack(expand=True)

# Input text label and text area with scrollbar
tk.Label(center_frame, text="Input Text:", bg="#87CEEB", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="e")
input_text_frame = tk.Frame(center_frame)
input_text_frame.grid(row=0, column=1, padx=10, pady=10)
input_text_scrollbar = tk.Scrollbar(input_text_frame)
input_text_scrollbar.pack(side="right", fill="y")
input_text_area = tk.Text(input_text_frame, height=8, width=60, font=("times new roman", 12), relief="solid", borderwidth=2, yscrollcommand=input_text_scrollbar.set)
input_text_area.pack(side="left", fill="both", expand=True)
input_text_scrollbar.config(command=input_text_area.yview)

# Shift value label and dropdown
shift_selection = tk.StringVar(value="3")
tk.Label(center_frame, text="Shift Value:", bg="#87CEEB", font=("times new roman", 12, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="e")
shift_dropdown = ttk.Combobox(center_frame, textvariable=shift_selection, values=list(range(1, 26)), width=10, state="readonly")
shift_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Operation mode label and dropdown
operation_mode_selection = tk.StringVar(value="encrypt")
tk.Label(center_frame, text="Mode:", bg="#87CEEB", font=("times new roman", 12, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="e")
mode_dropdown = ttk.Combobox(center_frame, textvariable=operation_mode_selection, values=["encrypt", "decrypt"], width=10, state="readonly")
mode_dropdown.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Buttons for processing, clearing, saving, and loading files
tk.Button(center_frame, text="Process", command=handle_process_button, font=("times new roman", 10, "bold"), bg="#4682B4", fg="white", relief="raised").grid(row=3, column=0, padx=10, pady=10, sticky="e")
tk.Button(center_frame, text="Clear All", command=clear_all_fields, font=("times new roman", 10, "bold"), bg="#4682B4", fg="white", relief="raised").grid(row=3, column=1, padx=10, pady=10, sticky="w")
tk.Button(center_frame, text="Load File", command=load_text_from_file, font=("times new roman", 10, "bold"), bg="#4682B4", fg="white", relief="raised").grid(row=4, column=0, padx=10, pady=10, sticky="e")
tk.Button(center_frame, text="Save File", command=save_result_to_file, font=("times new roman", 10, "bold"), bg="#4682B4", fg="white", relief="raised").grid(row=4, column=1, padx=10, pady=10, sticky="w")

# Output text label and text area with scrollbar
tk.Label(center_frame, text="Output Text:", bg="#87CEEB", font=("times new roman", 12, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="e")
output_text_frame = tk.Frame(center_frame)
output_text_frame.grid(row=5, column=1, padx=10, pady=10)
output_text_scrollbar = tk.Scrollbar(output_text_frame)
output_text_scrollbar.pack(side="right", fill="y")
output_text_area = tk.Text(output_text_frame, height=8, width=60, font=("times new roman", 12), relief="solid", borderwidth=2, state="disabled", yscrollcommand=output_text_scrollbar.set)
output_text_area.pack(side="left", fill="both", expand=True)
output_text_scrollbar.config(command=output_text_area.yview)

# Run the application
app_window.mainloop()
