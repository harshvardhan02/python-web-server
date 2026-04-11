# 🐍 Python Virtual Environment Setup

Follow the steps below to create and activate a virtual environment inside your project folder.

---

## 📁 Step 1 — Create Project Folder

```bash
mkdir project_folder
```

## 📂 Step 2 — Go Inside Project Folder
```bash
cd project_folder
```

## 🧪 Step 3 — Create Virtual Environment
Run the following command to create a virtual environment named `venv`:
```bash
python3 -m venv venv
```

## ▶️ Step 4 — Activate Virtual Environment (Mac/Linux)
```bash
source venv/bin/activate
```

### 🪟 Step 5 — Activate Virtual Environment (Windows)
```bash
venv\Scripts\activate
```

## 🧩 Step 6 — Install Required Python Libraries
```bash
pip install jupyter ipykernel numpy pandas
```

## 🧠 Step 7 — Add Virtual Environment to Jupyter Kernel
Run the following command to register your virtual environment as a Jupyter kernel:
```bash
python -m ipykernel install --user --name=venv --display-name "Python (venv)"
```

---

## Save Dependencies:-
Run this command

```bash
pip freeze > requirements.txt
```
This allows:

✅ GitHub upload
✅ Recreate the environment later

---

### Go to VS Code and select Kernel - Python (venv)

## Create:
```bash
.gitignore
```
### Add:
```bash
venv/
__pycache__/
.ipynb_checkpoints/
outputs/
```

Run the app server

```bash
  flask --app server run
```

Run the app server with debug mode

```bash
  flask --app server --debug run
```
    
