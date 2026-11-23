# Kun.uz Clone (Django)

**Kun.uz Clone** — bu Django framework yordamida yaratilgan yangiliklar sayti.
Loyiha O‘zbekistondagi mashhur yangiliklar portali Kun.uz dizayni va funksiyalaridan ilhomlanib ishlab chiqilgan.

---

## 🚀 Features

* 📰 Yangiliklar ro‘yxati (News list)
* 📄 Yangiliklar batafsil sahifasi
* 🖼️ Rasm bilan yangilik qo‘shish
* 🗂️ Kategoriyalar bo‘yicha yangiliklar
* 🔥 Trending / Popular news
* 🎞️ Asosiy yangiliklar slideri
* 🛠️ Django Admin orqali yangiliklarni boshqarish
* 📱 Responsive dizayn (telefon va kompyuter uchun)

---

## 🛠️ Technologies

Loyihada quyidagi texnologiyalar ishlatilgan:

* 🐍 Python
* 🌐 Django
* 🎨 HTML5
* 🎨 CSS3
* ⚡ Bootstrap
* 🗄️ SQLite
* 🖼️ Pillow (rasm bilan ishlash uchun)

---

## 📂 Project Structure

```
kunuzclone/
│
├── news/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
│
├── static/
│
├── media/
│
├── manage.py
│
└── db.sqlite3
```

---

## ⚙️ Installation

### 1️⃣ Repository ni clone qiling

```bash
git clone https://github.com/umidjon3455/KunUZClone_max.git
```

### 2️⃣ Papkaga kiring

```bash
cd KunUZClone_max
```

### 3️⃣ Virtual environment yarating

```bash
python -m venv venv
```

### 4️⃣ Virtual environment ni yoqing

Windows:

```bash
venv\Scripts\activate
```

Mac / Linux:

```bash
source venv/bin/activate
```

### 5️⃣ Kerakli kutubxonalarni o‘rnating

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6️⃣ Migratsiya qiling

```bash
python manage.py migrate
```

### 7️⃣ Serverni ishga tushiring

```bash
python manage.py runserver
```

Brauzerda oching:

```
http://127.0.0.1:8000
```

---

## 🔐 Admin Panel

Admin panelga kirish uchun:

```
http://127.0.0.1:8000/admin
```

Admin user yaratish:

```bash
python manage.py createsuperuser
```

---

## 📸 Screenshots

Bu yerga loyiha rasmlarini qo‘shishingiz mumkin.

Misol:

```
![Homepage](screenshot/home.png)
```

---

## 📌 Future Improvements

* 🔍 Yangilik qidirish (Search system)
* 💬 Kommentariya tizimi
* 👤 Foydalanuvchi registratsiyasi
* 🌙 Dark mode
* 📊 Ko‘rish statistikasi

---

## 👨‍💻 Author

**Umidjon Abdullayev**

GitHub:
https://github.com/umidjon3455
..


## Environment configuration

Copy `.env.example` to `.env` and replace `DJANGO_SECRET_KEY` with a newly generated random key before starting the project. Keep `.env` private and never commit it. `DJANGO_DEBUG=True` is for local development only; use `False` and configure `DJANGO_ALLOWED_HOSTS` for production.

Generate a new key with:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
