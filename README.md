# 📦 Backend Engineer Test Project

Proyek ini merupakan aplikasi backend sederhana yang dibuat menggunakan **FastAPI**, **SQLAlchemy**, dan **PostgreSQL**. Proyek ini dilengkapi autentikasi JWT, pengelolaan konten, manajemen pengguna, serta pengujian otomatis menggunakan **pytest**.

---

## 🚀 Fitur Utama

- Autentikasi menggunakan JWT (Login & Register)
- CRUD Konten (dengan proteksi token)
- CRUD Pengguna (hanya untuk admin)
- Validasi input (password, username unik, dll)
- Struktur modular dan bersih
- Test otomatis dengan Pytest
- Migrasi database menggunakan Alembic

---

## 🛠️ Langkah Instalasi

### 1. Clone Proyek

```bash
git clone https://github.com/Sinise5/backend-engineer-test.git
cd backend-engineer-test
```

### 2. Buat Virtual Environment

```bash
python3 -m venv env
source env/bin/activate  # Untuk macOS/Linux
# env\Scripts\activate  # Untuk Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Setup Database (PostgreSQL)

1. Pastikan PostgreSQL sudah terinstall dan berjalan.
2. Buat database dengan nama `db_contents`:

```sql
CREATE DATABASE db_contents;
```

3. Jalankan migrasi Alembic:

```bash
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
```

---

## ▶️ Menjalankan Server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8003
```

Akses API di: [http://localhost:8003](http://localhost:8003)

---

## ✅ Menjalankan Pengujian

```bash
pytest tests/
```

Test akan mencakup seluruh endpoint (auth, users, content).

---

## 📬 Koleksi Postman

Kamu bisa gunakan koleksi Postman untuk mencoba seluruh endpoint:

```
backend-engineer-test/backend-engineer-test.postman_collections.json
```

Import ke Postman untuk mulai uji coba API secara interaktif.

---

## 📁 Struktur Direktori

```
app/
├── auth/            # Logika autentikasi & hash password
├── core/            # Konfigurasi global (env, settings)
├── database/        # Koneksi DB dan engine
├── models/          # SQLAlchemy models
├── routers/         # Endpoint (auth, user, content)
├── schemas/         # Validasi & struktur data Pydantic
├── main.py          # Entry point FastAPI
tests/
├── test_auth.py     # Tes untuk login & register
├── test_users.py    # Tes untuk manajemen user
├── test_contents.py # Tes untuk konten
```

---

## ❓ FAQ

### Q: Kenapa error `Username already registered`?
A: Username sudah ada di database. Gunakan username lain saat register.

### Q: Gagal saat login?
A: Pastikan username dan password sesuai dengan yang sudah diregister. Password minimal 8 karakter. dan `SECRET_KEY` di `.env` sesuai 

### Q: Tidak bisa konek ke database?
A: Pastikan PostgreSQL aktif dan `DB_URL` di `.env` sesuai.

---

## 🙌 Kontribusi

Pull request dan feedback sangat dipersilakan. Silakan fork dan buka PR!

---

## 🧑‍💻 Dibuat oleh

Backend Engineer - [Nama Kamu]

---
