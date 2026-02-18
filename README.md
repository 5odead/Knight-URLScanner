## 🛡️ Knight V1 — Malicious URL Detection Tool

Knight is a Python-based lightweight URL scanner designed for detecting phishing links and malicious websites for cybersecurity education purposes.

### ✨ Features

- 🔍 **Real-Time URL Scanning**  
Analyzes URLs for suspicious patterns and security threats.

- 🔄 **Redirect Chain Detection**  
Tracks complete redirect paths to reveal hidden destinations.

- 📏 **Length Analysis**  
Flags abnormally long URLs that may indicate obfuscation.

- 🎣 **Phishing Pattern Detection**  
Identifies suspicious characters like '@' used in credential theft.

- 🔒 **HTTPS Validation**  
Checks for secure connections to protect against attacks.

- 🌙 **Dark Mode UI**  
Professional interface built with CustomTkinter.

### 🚀 Example Usage:

#### **Clone the Repository:**
```bash
git clone https://github.com/yourusername/Knight.git
cd Knight
```

#### **Install Dependencies:**
```bash
pip install customtkinter requests
```

> 💡 **Note:**  
>
> 1. Ensure Python 3.8+ is installed before running.
>
> 2. Internet connection required for redirect checking.
>
> 3. Known bug: Line 42 has variable name typo (`user_to_test` should be `url_to_test`).

#### **Run Knight:**
```bash
python knight.py
```

---

> ⚠️ **Disclaimer:**  
This tool is still in development. Expect Bugs.
