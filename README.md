# 🖥️ Tkinter & CustomTkinter Study Lab

🔁 **Last Update:** 16/05/2026  
🚀 **Execution:** Desktop App (Local)

---

## 📋 Summary
- [📖 About Project](#-about-project)
- [🛠️ Technologies Used](#%EF%B8%8F-technologies-used)
- [📋 Requirements](#-requirements)
- [🚀 How to Run](#-how-to-run)
- [👨‍💻 Author](#-author)

---

## 📖 About Project
This is a study repository dedicated to developing Desktop Graphical User Interfaces (GUIs) in Python. The project demonstrates practical learning steps, starting from the basic dialogue boxes of the standard **Tkinter** library to the construction of a modern, modular desktop application with native theme support (such as Dark Mode) using **CustomTkinter**.

The project structure is divided into three main implementation phases:

1. **`main.py`**: Initial exploration of basic user interactions using system dialogs, such as displaying alerts (`messagebox`), entering data in text fields (`simpledialog`), and selecting local files (`filedialog`).
2. **`sistema.py`**: Initial structure of a registration window built with native Tkinter, applying basic layout positioning (`pack`) and font customization.
3. **`sistema-completo.py`**: A robust, fully featured desktop application built using Object-Oriented Programming (OOP) with **CustomTkinter**. The interface features:
   - 📊 **Main Dashboard**: An interactive data processing simulator using a progress bar (`CTkProgressBar`).
   - 👥 **Profile Tab**: A user registration form containing text fields, radio buttons (`CTkRadioButton`), email notification checkboxes (`CTkCheckBox`), and dynamic updates to the sidebar window header.
   - ⚙️ **Preferences Tab**: A dropdown menu (`CTkOptionMenu`) for language selection and an interactive volume slider (`CTkSlider`) that dynamically updates the percentage label on screen in real time.
   - 🌓 **Dark / Light Mode**: A quick switch (`CTkSwitch`) on the sidebar to change the application's appearance theme instantly.

---

## 🛠️ Technologies Used
- **Python** (Version >= 3.12)
- **Tkinter** (Python's standard GUI library)
- **CustomTkinter** (Modern extension for custom widgets with dynamic theme support)
- **UV** (Extremely fast Python package installer and resolver)

---

## 📋 Requirements
To run this study lab in your local environment, you will need:
- **Python** (version 3.12 or higher recommended)
- **UV** (package manager) installed on your machine
- A code editor of your choice (such as **Visual Studio Code**)

---

## 🚀 How to Run

Follow the steps below to set up your environment and test the applications:

### 1. Clone the Repository
Clone this repository to your local machine and open the directory in your code editor:
```bash
git clone https://github.com/MatheusRodri/lab-tkinter.git
cd lab-tkinter
```

### 2. Install Dependencies
With **UV** installed, run the following command in your terminal to automatically synchronize and install all project dependencies (this handles the `.venv` virtual environment for you):
```bash
uv sync
```

### 3. Run the Study Scripts

You can run each of the learning phase scripts directly from your terminal:

#### 🔹 A. Test System Dialogs (`main.py`)
To see pop-ups and file selectors in action:
```bash
uv run main.py
```

#### 🔹 B. Test Initial Tkinter UI (`sistema.py`)
To display the simple registration window with custom typography:
```bash
uv run sistema.py
```

#### 🔹 C. Run the Complete Application (`sistema-completo.py`)
To launch the full app with its sidebar, tab managers, forms, and interactive progress bar:
```bash
uv run sistema-completo.py
```

---

## 👨‍💻 Author
**Matheus Rodrigues**
