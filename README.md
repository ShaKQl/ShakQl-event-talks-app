# 📊 BigQuery Release Notes Hub

A clean, modern web application that aggregates official Google Cloud BigQuery release notes and makes them easy to search, filter, and share to X (Twitter).

---

## 🗺️ How It Works

```text
+------------------------------+
| Google BigQuery Feed (Atom)   |
| (cloud.google.com/...xml)    |
+--------------+---------------+
               |
               | (HTTP GET)
               v
+--------------+---------------+
| Flask Web Server (app.py)    | <--- Serves UI & API Endpoint
+--------------+---------------+
               |
               | (JSON Payload)
               v
+--------------+---------------+
| Web Front-end (Browser)      |
|                              |
|  * Parsing & Tokenizing HTML |
|  * Filtering & Searching     |
|  * Interactive UI (Timeline) |
+-------+--------------+-------+
        |              |
        |              | (Select & Compose)
        v              v
+-------+------+ +-----+-------+
|  Copy Text   | | Share on X  |
|  Clipboard   | | (Web Intent)|
+--------------+ +-------------+
```

---

## 🎨 Interface Layout

```text
+-------------------------------------------------------------------------+
|  [DB] BigQuery Release Hub                     [ Refresh (Spinner) ]    |
+-------------------------------------------------------------------------+
|  SEARCH & FILTERS     |  TIMELINE UPDATES                               |
|                       |                                                 |
|  Search               |  June 23, 2026                                  |
|  [ Filter notes... ]  |  +-------------------------------------------+  |
|                       |  | FEATURE                                   |  |
|  Category Filter      |  | You can now configure BQ pipelines to...  |  |
|   - All Updates       |  |                                  [Copy] [X]  |
|   - Features          |  +-------------------------------------------+  |
|   - Changes           |                                                 |
|   - Deprecations      |  June 22, 2026                                  |
|   - Fixes             |  +-------------------------------------------+  |
|                       |  | CHANGED                                   |  |
|                       |  | BigQuery Data Transfer Service now...     |  |
|                       |  |                                  [Copy] [X]  |
|                       |  +-------------------------------------------+  |
+-------------------------------------------------------------------------+
|  TWEET COMPOSER DIALOG (MODAL)                                          |
|  +-------------------------------------------------------------------+  |
|  | Share on X / Twitter                                              |  |
|  | [ BigQuery Feature (June 23): You can now configure...          ] |  |
|  | [ https://docs.cloud.google.com/bigquery/docs/release-notes     ] |  |
|  | [ #BigQuery #GoogleCloud                                        ] |  |
|  |                                              145/280 chars        |  |
|  |                                      [ Copy Text ]  [ Post to X ] |  |
|  +-------------------------------------------------------------------+  |
+-------------------------------------------------------------------------+
```

---

## 🛠️ Stack & Technologies

* **Backend:** Python, Flask, Requests
* **Frontend:** Vanilla HTML5, Vanilla JavaScript, Vanilla CSS3 (Custom Dark Theme, CSS variables, Glassmorphism, Animations)
* **Fonts & Icons:** Outfit & Plus Jakarta Sans (Google Fonts), FontAwesome Icons

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have Python 3 installed.

### 2. Installation
Clone the repository and install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the App
Launch the local web server:
```bash
python app.py
```

Open your browser and navigate to **[http://127.0.0.1:5000](http://127.0.0.1:5000)**.

---

## 📦 Preparing for GitHub Publish

If you want to push this project to GitHub, follow these commands in your terminal:

```bash
# Initialize git repository
git init

# Add all files (respecting the .gitignore)
git add .

# Make the initial commit
git commit -m "Initial commit: BigQuery Release Notes Hub with Flask and Vanilla HTML/CSS/JS"

# Rename default branch to main
git branch -M main

# Add your remote repository origin
# git remote add origin https://github.com/YOUR_USERNAME/bq-releases-notes.git

# Push the code
# git push -u origin main
```
