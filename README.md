<p align="center">
  <b>Saya</b> is a high-performance, modular Telegram userbot architecture built with <b>Telethon</b> + <b>MongoDB</b>. Designed for developers who prioritize security, speed, and clean code.
</p>


---

</div>

## 🛡️ Why Saya is Safe?

**Zero String Session Reliance**

Unlike traditional userbots that require risky "String Sessions" generated via third-party  bots, Ether utilizes a **native authentication flow**.

* **Self-Hosted Sovereignty:** Deploy on your own VPS. Your credentials never leave your environment.
* **Direct-to-Telegram Login:** Use the `/login` command to trigger an official Telegram OTP/2FA flow directly to your device.
* **Encrypted Local Storage:** Session data is stored securely on *your* server, not in a cloud database or a developer's logs.
* **No Middleware Risks:** No Replit, no Heroku logs, and no external session string generators.

---

## ⭐ Features

* **🛡️ Secure Auth:** Native login system (No String Session required)
* **⚡ Hybrid Engine:** Leverages Telethon (Userbot) and Bot API simultaneously
* **🔐 Privacy First:** Full 2FA support and local session management
* **📦 Plugin Architecture:** Easily drop new `.py` scripts into the `plugins/` folder
* **👉 There are many more features — visit the plugins folder or deploy to explore all.**

---

### 1️⃣ Collect Required Details

| Variable | Description |
|---|---|
| API_ID | Telegram API ID |
| API_HASH | Telegram API Hash |
| BOT_TOKEN | BotFather Bot Token |
| OWNER_ID | Your Telegram Numeric ID |
| MONGO_URI | MongoDB Connection URI |

### Required Links

- https://my.telegram.org
- https://t.me/BotFather
- https://mongodb.com

---

### 2️⃣ Fork Repository

- ⭐ Star the repository
- 🍴 Fork Ether to your GitHub account

---

### 3️⃣ Deploy to Render

Click the **Deploy to Render** button.

Then:

- Login to Render
- Connect GitHub
- Select your forked Ether repository

---

### 4️⃣ Configure Render

#### Recommended Plan

- Free Plan

---

### Fill in Start Command

```bash
python render.py
```

---

## Add Environment Variables

| Key | Value |
|---|---|
| API_ID | Your Telegram API ID |
| API_HASH | Your Telegram API Hash |
| BOT_TOKEN | Your Bot Token |
| OWNER_ID | Your Telegram User ID |
| MONGO_URI | MongoDB URI |

---

After adding all variables:

✅ Click **Create Web Service**

⏳ Deployment usually takes around **1–2 minutes**

---

### 5️⃣ Final Telegram Setup

Open **@BotFather**

- Send `/mybots`
- Select your bot
- Open **Bot Settings**
- Enable **Inline Mode**

---

Then open your deployed bot and run:

```bash
/login
```

Complete the login process:

- Phone Number Verification
- OTP Verification
- 2FA Password (if enabled)

---

## ✅ Deployment Complete

Use:

```bash
.help
```

to see all available commands.



</details>

---


`🚀 JustRunMyApp Deployment Guide`

</summary>

---

# 1️⃣ Collect Required Details

| Variable | Description |
|---|---|
| API_ID | Telegram API ID |
| API_HASH | Telegram API Hash |
| BOT_TOKEN | BotFather Bot Token |
| OWNER_ID | Your Telegram Numeric ID |
| MONGO_URI | MongoDB Connection URI |

---

# 2️⃣ Fork & Download Repository

- ⭐ Star Ether
- 🍴 Fork the repository
- 📦 Download repository ZIP

---

# 3️⃣ Upload ZIP File

- Login to JustRunMyApp
- Upload the ZIP file
- Wait for processing
- Fill all required environment variables

⏳ Deployment usually takes around **1–2 minutes**

---

# 4️⃣ Final Telegram Setup

Open **@BotFather**

- Send `/mybots`
- Select your bot
- Open **Bot Settings**
- Enable **Inline Mode**

---

Then open your deployed bot and run:

```bash
/login
```

Complete:

- Phone Number Verification
- OTP Verification
- 2FA Password (if enabled)

---

# ✅ Deployment Complete

Use:

```bash
.help
```

to see all available commands.

---

</details>

---

# ☁️ Deploy on VPS

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install python3 python3-pip python3-venv git screen -y

# Clone repository
git clone https://github.com/Username.git

# Open project folder
cd Ether

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Create environment file
nano .env

# Start screen session
screen -S ether

# Start Ether
python main.py

# Detach screen session:
# CTRL + A then D
```

---

