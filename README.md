# HOW2USE G2E!

download ⬆️⬆️ (G2E.py)

---

## 📦 Prerequisites

Before using `G2E.py`, make sure the following are installed:

### 1. Node.js

* Download: [https://nodejs.org](https://nodejs.org)
* Install the latest LTS or Current version (v20+ recommended)

Check installation:

```bash
node -v
npm -v
```

---

### 2. Python 3.10 or higher

* Download: [https://python.org/downloads](https://python.org/downloads)
* ✅ Make sure to check **"Add Python to PATH"** during installation!

Check version:

```bash
python --version
```

---

### 3. Python Dependencies

Install with:

```bash
pip install rich
```

---

## 🤖 How to Ask ChatGPT for Compatible Output

To get output that's compatible with `G2E.py`, use this prompt:

```
Create an Electron app with the following structure:

- A folder name at the top
- Full content of these files:
  [package.json]
  (Include basic Electron config with "start": "electron .")

  [index.html]
  (Simple HTML with a button and <script src="renderer.js">)

  [main.js]
  (Create a BrowserWindow and load index.html)

  [renderer.js]
  (Attach event to the button, e.g., alert)

Format it like this:

FolderName  
[package.json]  
...  
[index.html]  
...  
[main.js]  
...  
[renderer.js]  
...

The goal is to copy and paste the whole thing into a Python script that creates files automatically.
```

This format allows `G2E.py` to:

* Detect the folder name
* Extract each file block
* Create the Electron project automatically
* Run `npm install` and prepare to launch

---
