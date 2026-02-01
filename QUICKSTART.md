# Quick Start Guide - CinOpSys Dashboard

## Langkah Cepat (5 Menit)

### 1. Persiapan File

Pastikan Anda memiliki file-file ini di satu folder:
```
cinopsys-dashboard/
├── app.py                    # Dashboard utama
├── requirements.txt          # Dependencies
├── README.md                 # Dokumentasi lengkap
├── .streamlit/
│   └── config.toml          # Konfigurasi Streamlit
├── movie_embeddings.npy      # File dari notebook (WAJIB!)
└── movies_clean.csv          # File dari notebook (WAJIB!)
```

**PENTING**: File `movie_embeddings.npy` dan `movies_clean.csv` dihasilkan dari notebook `cinopsys_improved.ipynb`. Jalankan notebook terlebih dahulu untuk generate file-file ini.

### 2. Install Dependencies

```bash
# Buka terminal/command prompt
cd path/to/cinopsys-dashboard

# Install dependencies
pip install -r requirements.txt
```

### 3. Jalankan Dashboard

```bash
streamlit run app.py
```

Dashboard akan otomatis terbuka di browser pada `http://localhost:8501`

### 4. Cara Pakai

1. **Cari film**: Ketik judul di search box (contoh: "Matrix")
2. **Pilih film**: Klik dropdown untuk memilih
3. **Lihat rekomendasi**: Film serupa akan muncul otomatis
4. **Atur settings**: Gunakan sidebar untuk customize
5. **Download hasil**: Tombol download di bawah untuk export

## Troubleshooting Cepat

### Error: "File not found"
```bash
# Pastikan Anda sudah jalankan notebook dulu
# File movie_embeddings.npy dan movies_clean.csv HARUS ada
```

### Error: "Module not found"
```bash
# Install ulang dependencies
pip install -r requirements.txt --upgrade
```

### Dashboard tidak muncul
```bash
# Coba port lain
streamlit run app.py --server.port 8502
```

### Performance lambat
```bash
# Edit app.py, line ~62, ubah:
CACHE_TTL = 3600  # Jadi lebih kecil jika RAM terbatas
```

## Testing

Coba search film-film ini untuk test:
- "The Matrix" - Sci-fi
- "Toy Story" - Animation
- "The Shining" - Horror
- "Inception" - Mind-bending
- "Forrest Gump" - Drama

## Next Steps

- Baca `README.md` untuk dokumentasi lengkap
- Customize colors di `.streamlit/config.toml`
- Modify UI di `app.py` (search "Custom CSS")
- Add features sesuai kebutuhan

## Bantuan Lebih Lanjut

Jika masih ada masalah:
1. Check console untuk error messages
2. Pastikan Python version >= 3.10
3. Pastikan semua file ada di folder yang sama
4. Restart Streamlit jika ada perubahan code

---

**Selamat mencoba!** 🎬
