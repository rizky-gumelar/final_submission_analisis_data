import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
from func import load_plot

# Judul halaman
st.set_page_config(page_title="Air Quality Analysis - Rizky Syah Gumelar")
st.title('Proyek Analisis Data [Air Quality Dataset]')

# Informasi pribadi
st.write('**Nama:** Rizky Syah Gumelar')
st.write('**Email:** m007d4ky2576@bangkit.academy')
st.write('**ID Dicoding:** rizkysyahgumelar')
st.divider()

# Load Dataset
# data yang saya gunakan sudah di downsampled untuk mengurangi waktu running, jika ingin menggunakan dataset asli silakan ubah comment dibawah
all_df = pd.read_csv('dashboard/main_data_clean_downsampled.csv')
all_df['date'] = pd.to_datetime(all_df[['year', 'month', 'day', 'hour']])
#df = pd.read_csv('dashboard/main_data.csv')
min_date = all_df["date"].min()
max_date = all_df["date"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")

    selected = option_menu(
        menu_title = "Main Menu",
        options = ["Home", "Dataset", "Explanatory Data Analysis (EDA)"]
    )
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
df = all_df[(all_df["date"] >= str(start_date)) & (all_df["date"] <= str(end_date))]

if selected =="Home":
    st.header("Sebaran kadar senyawa pada masing-masing stasiun")
    senyawas = ["CO", "PM2.5", "PM10", "SO2", "NO2", "O3"]
    # Mengatur grid subplot
    fig, axes = plt.subplots(3, 2, figsize=(20, 15), sharex=True)
    plt.subplots_adjust(hspace=4, wspace=0.3)

    # Iterasi melalui senyawas dan membuat subplot
    for senyawa in senyawas:
        dmean = df.groupby('station')[senyawa].mean().reset_index()
        dmean = dmean.sort_values(by=senyawa, ascending=False)

        # Membuat plot
        plt.figure(figsize=(8, 4))
        sns.barplot(x='station', y=f'{senyawa}', data=dmean, palette='inferno')
        plt.xlabel('Tempat Station')
        plt.xticks(rotation=45, ha='right')
        plt.ylabel(f'Rata-rata kadar {senyawa}')
        plt.title(f'Perbandingan rata-rata kadar {senyawa} antar Stasiun')
        plt.show()
        plt_sebaran = plt
        load_plot(plt_sebaran)
    st.subheader('Kesimpulan 1:')
    st.write('Dari visualisasi yang telah dibuat dapat diketahui bahwa intensitas senyawa terbanyak pada masing-masing stasiun berbeda. Berikut adalah kesimpulan dari grafik tersebut:')
    kesimpulan = """
    - Station dengan kadar kandungan CO tertinggi adalah Wanshouxigong.
    - Station dengan kadar kandungan PM2.5 tertinggi adalah Dongsi.
    - Station dengan kadar kandungan PM10 tertinggi adalah Gucheng.
    - Station dengan kadar kandungan SO2 tertinggi adalah Nongzhanguan.
    - Station dengan kadar kandungan NO2 tertinggi adalah Wanliu.
    - Station dengan kadar kandungan O3 tertinggi adalah Dingling.
    """
    st.write(kesimpulan)

    st.divider()

    st.header("Tren dari Senyawa Karbon Monooksida (CO) setiap bulannya")
    data_time_series_monthly = df[['date', 'CO']].set_index('date').resample('M').mean()
    # Plot Bulanan
    plt.figure(figsize=(12, 6))
    plt.plot(data_time_series_monthly.index, data_time_series_monthly['CO'], marker='o', color='blue', linestyle='-')
    plt.title('Konsentrasi Rata-rata Bulanan CO')
    plt.xlabel('Tanggal')
    plt.ylabel('Konsentrasi')
    plt.grid(True)
    plt.show()
    load_plot(plt)
    # Menghitung nilai atas (maksimum) dan nilai bawah (minimum) dari plot
    co_max_value = data_time_series_monthly['CO'].max()
    co_min_value = data_time_series_monthly['CO'].min()
    # Mencetak nilai atas (maksimum) dan nilai bawah (minimum)
    st.write(f"Nilai maksimum CO: {co_max_value} (ug/m^3)")
    st.write(f"Nilai minimum CO: {co_min_value} (ug/m^3)")
    st.subheader('Kesimpulan 2:')
    kesimpulan = """
    Dari visualisasi yang telah dibuat dapat diketahui bahwa tren kadar senyawa Karbon Monooksida (CO) cukup fluktuatif yaitu dengan rata-rata maks 2789 ug/m^3 pada Januari 2016 dan 679 ug/m^3 pada Juli 2016. dari visualisasi datas juga dapat diketahui bahwa kadar CO selalu meningkat dan berada dipuncaknya tiap bulan januari.
    """
    st.write(kesimpulan)
    

    st.divider()

    st.header("Senyawa dan fitur yang saling berkorelasi kuat")
    data_time_series = df[['date', 'PM10', 'PM2.5']].set_index('date').resample('M').mean()

    plt.figure(figsize=(15, 6))
    plt.plot(data_time_series.index, data_time_series['PM10'], label='PM10', color='blue')
    plt.plot(data_time_series.index, data_time_series['PM2.5'], label='PM2.5', color='red')
    plt.title('Konsentrasi Rata-rata Bulanan PM10 dan PM2.5')
    plt.xlabel('Tanggal')
    plt.ylabel('Konsentrasi')
    plt.legend()
    plt.show()
    load_plot(plt)

    data_time_series = df[['date', 'TEMP', 'DEWP']].set_index('date').resample('M').mean()
    plt.figure(figsize=(15, 6))
    plt.plot(data_time_series.index, data_time_series['TEMP'], label='TEMP', color='blue')
    plt.plot(data_time_series.index, data_time_series['DEWP'], label='DEWP', color='red')
    plt.title('Konsentrasi Rata-rata Bulanan Temperature dan Dew Point')
    plt.xlabel('Tanggal')
    plt.ylabel('Konsentrasi')
    plt.legend()
    plt.show()
    load_plot(plt)

    data_time_series = df[['date', 'TEMP', 'DEWP', 'PRES']].set_index('date').resample('M').mean()
    plt.figure(figsize=(15, 6))
    plt.plot(data_time_series.index, data_time_series['TEMP'], label='TEMP', color='blue')
    plt.plot(data_time_series.index, data_time_series['DEWP'], label='DEWP', color='red')
    plt.plot(data_time_series.index, data_time_series['PRES'], label='PRES', color='green')
    plt.title('Konsentrasi Rata-rata Bulanan Temperature, Dew Point dan Pressure')
    plt.xlabel('Tanggal')
    plt.ylabel('Konsentrasi')
    plt.legend()
    plt.show()
    load_plot(plt)
    st.subheader('Kesimpulan 3:')
    kesimpulan = """
    Pada hasil Matriks korelasi dan visualisasi diatas dapat diketahui bahwa nilai korelasi positif antara PM2.5 dengan PM10 sangatlah tinggi yang menandakan hubungan antar fitur yang kuat. 
    Selain itu juga terdapat korelasi positif yang tinggi antara Temperature (TEMP)dengan Dew Point (DEWP), tetapi berkorelasi negatif dengan Pressure (PRES). 
    Dari visualisasi diatas juga dapat diketahui bahwa tren Temperature, Dew Point dan Pressure membentuk sebuah pola yang sangat jelas, yaitu Temperature dan Dew Point yang turun dibulan januari dan naik pada bulan Juli, tetapi berlaku sebaliknya pada Presure karena berkorelasi negatif.
    """
    st.write(kesimpulan)
    

if selected =="Dataset":
    st.write(df)
if selected == "Explanatory Data Analysis (EDA)":
    df_corr = df.select_dtypes(include='number')
    st.header("Analisis korelasi antar kolom")
    matriksCorr = df_corr.corr()
    plt.figure(figsize=(15, 10))
    sns.heatmap(matriksCorr, cmap='Greens', annot=True, annot_kws={'fontsize': 12})
    plt.show()
    plt_corr = plt
    load_plot(plt_corr)
    kesimpulan = """Pada hasil korelasi diatas dapat diketahui bahwa nilai korelasi positif antara PM2.5 dengan PM10 sangatlah tinggi yang menandakan hubungan antar fitur yang kuat. Selain itu juga terdapat korelasi positif yang tinggi antara Temperature dengan Dew Point, tetapi berkorelasi negatif dengan Pressure."""
    st.write(kesimpulan)

    st.divider()
    st.header("Analisis konsentrasi senyawa tahunan")
    senyawas = ["CO", "PM2.5", "PM10", "SO2", "NO2", "O3"]
    for senyawa in senyawas:
        data_time_series_yearly = df[['date', senyawa]].set_index('date').resample('Y').mean()

        # Plot bar chart per tahun
        plt.figure(figsize=(6, 3))
        plt.bar(data_time_series_yearly.index.year, data_time_series_yearly[senyawa], color='blue')
        plt.title(f'Konsentrasi Rata-rata Tahunan {senyawa}')
        plt.xlabel('Tahun')
        plt.ylabel(f'Konsentrasi {senyawa}')
        plt.show()
        plt_tahunan = plt
        load_plot(plt_tahunan)
    
