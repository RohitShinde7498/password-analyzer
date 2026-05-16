# 🔐 Password Strength Analyzer

![License](https://img.shields.io/github/license/RohitShinde7498/password-analyzer)
![Language](https://img.shields.io/badge/language-Python-blue)
![Platform](https://img.shields.io/badge/platform-Kali%20Linux-red)
![Security](https://img.shields.io/badge/topic-cybersecurity-green)

A Python-based password strength analyzer that evaluates your password
security and suggests stronger alternatives using cryptography concepts.

---

## ✨ Features
- 🔍 Checks password length, complexity and uniqueness
- 🔠 Validates uppercase, lowercase, numbers and symbols
- 🚫 Detects common and weak passwords
- 🔄 Detects repeated and sequential patterns
- 💡 Gives detailed improvement suggestions
- 🔑 Generates strong random password alternatives
- 📊 Scores password on a scale of 0-6
- ⚡ Lightweight — no external libraries needed

---

## 🛠️ Installation

### Requirements
- Python 3.x
- Git
- Kali Linux / Any Linux distro

### Clone the repo
git clone https://github.com/RohitShinde7498/password-analyzer.git
cd password-analyzer

### Run directly - no installation needed!
python3 password_analyzer.py

---

## 🚀 Usage

Run the program:
python3 password_analyzer.py

You will see a menu:
========================================
   PASSWORD STRENGTH ANALYZER
========================================

1. Check password strength
2. Generate strong password
3. Exit

### Option 1 - Check password strength
- Enter any password
- Get instant strength score
- See exactly what is missing
- Get improvement suggestions

### Option 2 - Generate strong password
- Generates a random 16 character password
- Contains uppercase, lowercase, numbers and symbols
- Ready to use immediately

---

## 📊 Strength Scoring System

| Score | Strength     | Meaning                        |
|-------|-------------|--------------------------------|
| 0-1   | Very Weak 🔴 | Extremely easy to crack        |
| 2-3   | Weak 🟠      | Can be cracked easily          |
| 4     | Fair 🟡      | Moderate security              |
| 5     | Strong 🟢    | Good security                  |
| 6     | Very Strong 💪| Excellent security             |

---

## 🔍 What Gets Checked

| Check              | Requirement                    |
|--------------------|-------------------------------|
| Length             | Minimum 8 characters          |
| Better Length      | 12+ characters recommended    |
| Uppercase          | At least one A-Z              |
| Lowercase          | At least one a-z              |
| Numbers            | At least one 0-9              |
| Symbols            | At least one !@#$%^&*         |
| Common passwords   | Not in known weak list        |
| Repeated chars     | No aaa or 111 patterns        |
| Sequential chars   | No abc or 123 patterns        |

---

## 📁 Project Structure
password-analyzer/
├── password_analyzer.py    # Main program
└── README.md               # Documentation

---

## 🔧 Tech Stack
- Python 3
- re module (regex)
- random module
- string module
- No external dependencies!

---

## 💡 What I Learned
- Password security concepts
- Regular expressions in Python
- Basic cryptography concepts
- How attackers crack weak passwords
- Importance of entropy in passwords

---

## 🔮 Future Improvements
- [ ] Add GUI interface
- [ ] Check against larger common password database
- [ ] Calculate crack time estimate
- [ ] Add password history to prevent reuse
- [ ] Export results to PDF report
- [ ] Add color output in terminal

---

## ⚠️ Disclaimer
This tool is for educational purposes only.
Use it to improve your own password security.

---

## 👤 Author
Rohit Shinde
- GitHub: @RohitShinde7498

---

## 📄 License
MIT License - feel free to use and modify
