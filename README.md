# Kafe ID - Sistem Manajemen Pesanan Kafe

## Pendahuluan
aplikasi ini dibuat oleh
As'adurrofiq  23.01.5049 sebagai bagian backend
Rasendriya Ajeng P.  23.01.5051 sebagai bagian frontend

## Tentang Aplikasi

Kafe ID adalah aplikasi manajemen pesanan berbasis web untuk kafe dan restoran. Dibangun dengan Django dan Tailwind CSS, aplikasi ini menyediakan antarmuka yang intuitif untuk pelanggan memesan menu dan bagi staf kafe untuk mengelola pesanan.

## Fitur Utama

- **Pemesanan Menu**: Pelanggan dapat memesan makanan dan minuman dari meja mereka
- **Dashboard Admin**: Panel admin untuk melihat dan mengelola semua pesanan
- **Manajemen Status Pesanan**: Melacak status pesanan (antri, diproses, selesai)
- **Antarmuka Responsif**: Desain modern yang bekerja di berbagai ukuran perangkat
- **Konfirmasi Pesanan**: Halaman konfirmasi pesanan dengan redirect otomatis

## Teknologi

- **Backend**: Django 5.2.4, Python 3.12
- **Database**: SQLite (untuk pengembangan)
- **Frontend**: HTML, CSS, JavaScript, Tailwind CSS
- **Deployment**: Compatible dengan platform hosting berbasis Python

## Instalasi

1. Clone repositori ini:
   ```
   git clone https://github.com/Rofiq02bae/kafe_id.git
   cd kafe_id
   ```

2. Buat dan aktifkan lingkungan virtual:
   ```
   python -m venv env
   source env/bin/activate  # Untuk Linux/Mac
   # atau
   env\Scripts\activate  # Untuk Windows
   ```

3. Pasang dependensi:
   ```
   pip install -r requirements.txt
   ```

4. Migrasi database:
   ```
   python manage.py migrate
   ```

5. Jalankan server pengembangan:
   ```
   python manage.py runserver
   ```

6. Akses aplikasi di browser: http://localhost:8000/

## Penggunaan

### Untuk Pelanggan:
1. Buka halaman menu dari meja Anda: `/meja/{id}/`
2. Pilih menu dan jumlah pesanan
3. Klik "Pesan Sekarang"
4. Dapatkan konfirmasi pesanan

### Untuk Admin/Staff:
1. Buka dashboard admin: `/dashboard/`
2. Lihat semua pesanan dengan status mereka
3. Ubah status pesanan saat diproses dan selesai

## Struktur Proyek

```
kafe_id/
│
├── app/                  # Konfigurasi Django utama
│   ├── settings.py       # Pengaturan aplikasi
│   ├── urls.py           # URL mapping utama
│   └── ...
│
├── kafe_id/              # Aplikasi utama
│   ├── models.py         # Model database (User, Menu, Pesanan, dll)
│   ├── views.py          # Views dan fungsi logika
│   ├── urls.py           # URL mapping aplikasi
│   ├── templates/        # Template HTML
│   │   ├── base.html     # Template dasar
│   │   └── kafe/         # Template halaman spesifik
│   │       ├── dashboard.html
│   │       ├── menu_list.html
│   │       └── pesanan_sukses.html
│   │
│   └── static/           # Aset statis (CSS, JS, gambar)
│       ├── css/
│       └── ...
│
└── static/               # Aset statis global
    └── media/            # File media (gambar menu, dll)
```

## Kontribusi

Kontribusi selalu diterima! Silakan fork repositori ini, buat perubahan, dan kirimkan pull request.

## Lisensi

[MIT License](LICENSE)

## Kontak

Untuk pertanyaan dan saran, hubungi: cse.arrofiq@gmail.com