# Proyek Analisis Data [Air Quality Dataset]

- **Nama:** [Rizky Syah Gumelar]
- **Email:** [m007d4ky2576@bangkit.academy]
- **ID Dicoding:** [rizkysyahgumelar]

## Daftar Isi

1. [Instalasi](#instalasi)
2. [Struktur Proyek](#struktur-proyek)
3. [Penggunaan](#penggunaan)
4. [Demo Aplikasi](#demo-aplikasi)

## Instalasi

### 1. Setup Lingkungan Virtual

```bash
# Buat virtual env dengan nama .venv
python -m venv .venv

#Aktifkan env
.venv\Scripts\Activate.ps1
```
### 2. Instal Streamlit

```bash
pip install streamlit
```

## Struktur Proyek

```
final_submission_analisis_data
├───dashboard
| ├───main_data.csv		# Dataset yang digunakan
| ├───main_data_clean_downsampled.csv
| └───dashboard.py 		# File utama aplikasi Streamlit
├───data 					# Folder kumpulan dataset
| ├───data_1.csv
| └───data_2.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
```

## Penggunaan

1. Pastikan lingkungan virtual telah diaktifkan.

2. Buka folder **final_submission_analisis_data**

3. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run dashboard/dashboard.py
   ```

4. Buka browser dan akses URL yang ditampilkan oleh Streamlit (biasanya `http://localhost:8501`).

## Demo Aplikasi

![Screenshot 2024-03-04 022323](https://github.com/rizky-gumelar/final_submission_analisis_data/assets/91964713/c0c9ab73-26b4-470e-8f52-f55332ec3d36)
![Screenshot 2024-03-04 022357](https://github.com/rizky-gumelar/final_submission_analisis_data/assets/91964713/dca961e7-2523-430c-9093-b3f157fea165)
![Screenshot 2024-03-04 022411](https://github.com/rizky-gumelar/final_submission_analisis_data/assets/91964713/665654ab-394c-4f1e-a0bc-c1cf95c6b17b)
![Screenshot 2024-03-04 022423](https://github.com/rizky-gumelar/final_submission_analisis_data/assets/91964713/471530a3-c9a8-4d35-b2dd-ef44d1b8a992)
![Screenshot 2024-03-04 022902](https://github.com/rizky-gumelar/final_submission_analisis_data/assets/91964713/72ec326e-99a5-441a-a10e-be99986a85be)
