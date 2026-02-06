# Password Generator using Python & Streamlit

A modern, secure, and customizable **Password Generator Web App** built using **Python and Streamlit**.  
This project allows users to generate strong passwords with configurable options and real-time strength evaluation.

## Features

- Adjustable password length (6–32 characters)
- Include/exclude:
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Numbers (0–9)
  - Symbols (!@#$%^&*)
- Option to exclude similar-looking characters (O, 0, l, 1)
- Password strength indicator (Weak / Medium / Strong)
- Entropy calculation to measure password randomness
- Easy copy-to-clipboard
- Fully client-side (no passwords are stored or logged)


----

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- Standard Python libraries (`random`, `string`, `math`)

## 🗂️ Project Structure

```
Regression_Project/
│
├── app.py
├── requirements.txt
└── README.md
```
--- 


## ▶️ How to Run the Project Locally



### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/PasswordGenerator.git
cd PasswordGenerato
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
streamlit run app.py
```

---- 

### 🧠 Password Strength Logic

Password strength is evaluated based on:

- Length of the password

- Presence of uppercase characters

- Presence of numbers

- Presence of special symbols

Additionally, entropy (in bits) is calculated to estimate password randomness and security level.


--- 

### 🔐 Security Considerations

- Passwords are generated locally

- No passwords are saved, stored, or transmitted

- Safe for learning and demonstration purposes


-----


### 📌 Future Enhancements

- Dark / Light theme toggle

- Password history (session-based)

- One-click regenerate button

- Deployment on Streamlit Cloud

------

### 👩‍💻 Author

__Laiba Khan__

----

### ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!

