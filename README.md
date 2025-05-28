# 🧠 HSN Code Validator Agent

This is a command-line HSN Code Validator built using **Google's Agent Developer Kit (ADK)**. The agent checks if the entered HSN code is in the correct format and exists in a local Excel dataset.

---

## 📁 Project Structure
```
hsn-code-validator-agent/
│
├── agent.py
├── hsn_lookup_tool.py
├── requirements.txt
├── README.md
├── agent.yaml
│
└── data/
└── HSN_SAC.xlsx
```
---

## ✅ What It Does

- Validates the format of HSN codes (numeric, 2–8 digits)
- Checks if the code exists in the dataset
- Returns description if valid, or error message if invalid

---

## 🚀 How to Run

```bash
python -m google.adk.cli run .
```
---

💾 Installation
Clone the repo:

bash
```
git clone https://github.com/sanghavai/hsn-code-validator-agent.git
cd hsn-code-validator-agent
```
---

🖼️ Screenshots
![image](https://github.com/user-attachments/assets/20b5368a-a95e-4d90-97bb-a8111e339890)
![image](https://github.com/user-attachments/assets/011feed4-ebd2-41f3-88f1-abd7bf218495)
![image](https://github.com/user-attachments/assets/b88df602-68f8-4e44-b5bd-7c1eb25ee2ef)
![image](https://github.com/user-attachments/assets/7894e952-cf51-4680-8b9d-5ac7e6abb472)
![image](https://github.com/user-attachments/assets/4a8141b4-2eea-4928-8320-57448dee806f)

🙌 Author
Sanghavai M L
