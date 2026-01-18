# 🖥️ Ethical Keystroke Monitor & Analytical Dashboard

---

## 📝 Project Overview

**Ethical Keystroke Monitor & Analytical Dashboard** is a cybersecurity awareness tool developed during the **VOIS & Vodafone Idea Foundation Cybersecurity Internship**.
The project provides an educational demonstration of how keystroke logging operates within a **controlled, ethical environment**.

The application features a modern **Dark Mode GUI** that captures keyboard events, generates forensic-style logs, and provides real-time typing analytics. Its primary objective is to highlight the risks associated with **input-interception malware** while promoting strong defensive cybersecurity practices.

---

## 🛡️ Problem Statement

Keystroke logging is a stealthy **pre-encryption threat** that captures sensitive information—such as passwords and personally identifiable information (PII)—before it reaches secure applications.

### Key Challenges

* **Awareness Gap:** Users often rely solely on browser-level security indicators (HTTPS), unaware of local input-level vulnerabilities.
* **Educational Need:** Many learners lack hands-on visibility into how keystroke logging actually functions.

By visualizing the capture and analysis process, this project encourages defensive habits such as **Multi-Factor Authentication (MFA)** and the use of **virtual keyboards** to reduce the risks posed by stealthy input loggers.

---

## ✨ Key Features

* **Modern UI:** Built with CustomTkinter for a professional, responsive dark-mode experience
* **Live Feed:** Real-time visualization of keystrokes directly within the dashboard
* **Forensic Logging:** Structured JSON logs with human-readable timestamps and raw TXT logs
* **Session Analytics:** Automatic calculation of Words Per Minute (WPM), total keystrokes, and session duration
* **Transparent Control:** Operates only when a user explicitly starts a session, unlike malicious background spyware

---

## 💻 Tech Stack

| Component        | Technology           |
| ---------------- | -------------------- |
| Language         | Python 3.x           |
| GUI Framework    | CustomTkinter        |
| Input Handling   | Pynput               |
| Data Format      | JSON / Plain Text    |
| Forensics & Time | Datetime, OS Modules |

---

## 🚀 Getting Started

### Prerequisites

* Python 3.7 or higher
* A code editor such as VS Code

### Installation

**Clone the repository:**

```bash
git clone https://github.com/vaishaldsouza/Keystroke-Awareness-Dashboard.git
cd Keystroke-Awareness-Dashboard
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Run the application:**

```bash
python KeyloggerGUI.py
```

---

## 📂 Project Structure

```plaintext
├── Keylogger.py        # Backend logic and hardware-level hooks
├── KeyloggerGUI.py     # Frontend dashboard and analytics UI
├── requirements.txt   # Python dependencies
├── .gitignore         # Prevents tracking of logs and junk files
└── README.md          # Project documentation
```

---

## 👥 Targeted End Users

* **Cybersecurity Students:** Study input-based attack vectors and data serialization
* **IT Trainees:** Understand forensic timelines and event-driven programming
* **General Users:** Build awareness about spyware and endpoint security

---

## 📜 Disclaimer

This project is intended **strictly for educational and cybersecurity awareness purposes**.
It must be used only in a **controlled environment**.
Unauthorized use of keystroke logging tools on systems you do not own is **illegal and unethical**.

---

## 🤝 Acknowledgment

Developed as part of the **VOIS & Vodafone Idea Foundation CSR Program**
**4-Week Virtual Internship on Cybersecurity with Generative AI**,
conducted by **Edunet Foundation**.

---
