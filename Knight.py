import customtkinter as ctk
import sys
import requests as r

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def on_closing():
    print("DEBUG: Knight shutting down safely...")
    app.destroy()
    sys.exit()

app = ctk.CTk() 
app.title("Knight V1")
app.geometry("800x600")
app.configure(fg_color="#000000")
app.protocol("WM_DELETE_WINDOW", on_closing)

print("DEBUG LOG BEGINS HERE")

def change_Text():
    my_label.configure(text = "Knight Activated", text_color ="red")
    user_input = url_entry.get()

    if not user_input.startswith("https"):
        user_input = "https://" + user_input

    result_box.delete("0.0","end")

    result_box.insert("end",f"Scanning: {user_input}\n")
    print(f"DEBUG: Engine is now analyzing the link: {user_input}")
    static_check(user_input)

    try:
        result_box.insert("end","\nChecking For Redirects....\n")
        headers = {"User-Agent": "Mozilla/5.0"}
        response = r.head(user_input, allow_redirects=True, timeout=8)

        if len(response.history) > 0:
            result_box.insert("end",f"{len(response.history)} Redirects \n")
            for hop in response.history:
                result_box.insert("end", f"->{hop.url}\n")

        result_box.insert("end",f"\nFinal Destination: {response.url}\n")

        if response.url != user_input:
            static_check(response.url)

    except Exception as e:
        result_box.insert("end",f"\nConnection Error: {e}\n")

def static_check(url_to_test):
    if len(url_to_test) > 100:
        result_box.insert("end", "⚠️ WARNING: Long URL\n")
    if "@" in url_to_test:
        result_box.insert("end", "⚠️ WARNING: URL Contains '@' (Phishing Risk)\n")
    if not user_to_test.startswith("https"):
        result_box.insert("end","WARNING: Connection is not secure (Missing HTTPS)\n")

my_label = ctk.CTkLabel(app, text="Hello User", font=("Arial", 20))
my_label.pack(pady=20)

url_entry = ctk.CTkEntry(app, placeholder_text="Enter URL", width=300)
url_entry.pack(pady=10)

my_button = ctk.CTkButton(app, text = "Scan URL", command = change_Text)
my_button.pack(pady=10)

result_box = ctk.CTkTextbox(app, width=700, height=300, font=("Courier New", 12), fg_color="#0a0a0a", border_color="#333333", border_width=2, text_color="#00FF00")
result_box.pack(pady=20)

app.mainloop()
