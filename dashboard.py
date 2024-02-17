import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sea

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df


def peminjaman(df_day, df_hour):
    #AZHAR
    st.write(
        "10122088 - Azhar Fachrezi"
        )
    st.header(
        "Tren Penggunaan Sepeda Tiap Waktu"
    )
    st.write(
        "Untuk mengetahui banyaknya penggunaan sepeda setiap bulan dan pada bulan apa peminjaman terjadi kenaikan dan penurunan."
    )

    df_day["dteday"] = pd.to_datetime(df_day["dteday"])
    by_date = df_day.groupby("dteday")["cnt"].sum()

    fig, ax = plt.subplots(figsize=(12, 6))

    by_date.plot(kind="line", color="orange", ax=ax)
    ax.set_title("Tren Penggunaan Sepeda dari Waktu ke Waktu")
    ax.set_xlabel("Bulan-Tahun")
    ax.set_ylabel("Total Penggunaan Sepeda (Cnt)")
    ax.grid(True)

    st.pyplot(fig)

    with st.expander("Penjelasan Tren Penggunaan Sepeda"):
        st.write(
            "Dari awal Januari 2011 hingga Juli 2011, terjadi kenaikan yang signifikan hampir menyentuh 6000 peminjaman. Awal 2012 terjadi penurunan hingga Februari 2012. Kemudian mengalami kenaikan kembali pada bulan Maret hingga April mencapai 8000 peminjaman. Titik puncak peminjaman terjadi di antara bulan September dan Oktober. Peminjaman mengalami penurunan hingga Desember 2012 "
        )

    st.write("<hr>", unsafe_allow_html=True)
    
    #NABIL
    st.write('10122094 - Mochamad Nabil Ramdhani')
    st.header(
        'Pengaruh Weathersit Terhadap Rata-Rata Peminjaman Sepeda'
    )
    st.write(
        'Untuk mengetahui apakah weathersit berpengaruh pada jumlah peminjaman.'
    )
    
    rata_cnt_by_weathersit = df_day.groupby('weathersit')['cnt'].mean().reset_index()
    st.write(rata_cnt_by_weathersit)

    x_coords = np.arange(len(list(rata_cnt_by_weathersit['weathersit'])))
    
    fig, ax = plt.subplots()
    bars = ax.bar(x_coords, rata_cnt_by_weathersit['cnt'], tick_label=rata_cnt_by_weathersit['weathersit'], color=['#FF0000', '#0000FF', '#0000FF'])
    ax.set_title('Rata-Rata Peminjam Berdasarkan Weathersit')
    ax.set_xlabel('Weathersit')
    ax.set_ylabel('Rata-Rata Peminjaman Sepeda')
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height, '%d' % int(height), ha='center', va='bottom')

    st.pyplot(fig)
    
    with st.expander('Penjelasan Analisis Jumlah Peminjaman Pada Setiap Cuaca'):
        st.write('Pada grafik di atas, terdapat 3 cuaca yang berbeda. Cuaca 1 merupakan cerah, cuaca 2 merupakan berkabut, cuaca 3 merupakan bersalju. Cuaca 1 merupakan cuaca dengan rata-rata peminjaman sepanjang tahun 2011-2012. Sedangkan Cuaca 3 merupakan cuaca dengan rata-rata peminjaman paling sedikit.')
    
    st.write("<hr>", unsafe_allow_html=True)
    
    #SINGGIH
    st.write("10122095 - Muhamad Singgih Prasetyo")
    st.header(
        "Jumlah Peminjaman Sepeda Setiap Musim"
    )
    st.write(
        "Untuk mengetahui banyaknya peminjaman sepeda yang terjadi setiap musim."
    )

    total_cnt_by_season = df_day.groupby('season')['cnt'].sum().reset_index()
    st.write(total_cnt_by_season)    

    x_coords = np.arange(len(list(total_cnt_by_season['season'])))

    fig, ax = plt.subplots()
    bars = ax.bar(x_coords, total_cnt_by_season['cnt'], tick_label=total_cnt_by_season['season'], color=['#0000FF', '#0000FF', '#FF0000', '#0000FF'])
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Peminjaman')
    ax.set_title('Jumlah Peminjaman Berdasarkan Musim')
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height, '%d' % int(height), ha='center', va='bottom')

    st.pyplot(fig)  

    with st.expander('Penjelasan Analisis Jumlah Peminjaman Pada Setiap Musim'):
        st.write('Pada grafik yang ditampilkan di atas, terlihat adanya kenaikan dan penurunan peminjaman berdasrkan perbedaan musim. Pada analisis ini, kami mengasumsikan bahwa musim 1 merupakan musim dingin, karena terjadi jumlah peminjaman terendah dalam grafik tersebut, hanya 471,348 peminjaman. Kemudian, musim 2 merupakan musim semi, musim 3 merupakan musim panas karena terjadi peminjaman tertinggi sebanyak 1,061,129 peminjaman. Dan musim 4 merupakan musim gugur. Jadi, peminjaman tertinggi terjadi pada saat musim panas dan penurunan peminjaman paling signifikan terjadi pada musim dingin.')

    st.write("<hr>", unsafe_allow_html=True)
    
    #RAFFY
    st.write("10122099 - Muhammad Raffy Abdillah")
    st.header("Grafik Rata-Rata Peminjaman Sepeda Per Bulan")
    st.write("Untuk mengetahui jumlah rata-rata peminjam sepeda setiap bulan")

    df_day["year_month"] = pd.to_datetime(df_day["dteday"]).dt.to_period("M")

    df_result = (
        df_day.groupby("year_month")
        .agg({"casual": "mean", "registered": "mean", "cnt": "mean"})
        .reset_index()
    )

    df_result["year_month"] = df_result["year_month"].astype(str)

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df_result["year_month"], df_result["casual"], label="Casual (avg)")
    ax.plot(df_result["year_month"], df_result["registered"], label="Registered (avg)")
    ax.plot(df_result["year_month"], df_result["cnt"], label="Cnt (avg)")
    ax.set_xlabel("Tahun-Bulan")
    ax.set_ylabel("Rata-Rata Peminjam")
    ax.set_title("Rata-Rata Jumlah Peminjam Sepeda Per Bulan (2011-2012)")
    ax.set_xticklabels(df_result["year_month"], rotation=45)
    ax.legend()

    st.pyplot(fig)

    with st.expander("Penjelasan Peminjaman Tertinggi"):
        st.write(
            "Berdasarkan grafik di atas, peminjaman sepeda terbanyak terjadi pada bulan September 2012 baik peminjam yang terdaftar maupun yang tidak terdaftar sebanyak 7000 lebih."
        )

    st.write("<hr>", unsafe_allow_html=True)

    #HAYKAL
    st.write("10122116 - Haykal Fadhilah Suryana")
    st.header("Perbandingan Jumlah Peminjam Sepeda Antara Tahun 2011-2012")
    st.write(
        "Untuk mengetahui Perbandingan jumlah peminjam pada Weekday antara Tahun 2011 dan 2012"
    )
    
    data_2011 = df_day[(df_day["yr"] == 0) & (df_day["weekday"].isin([0, 1, 2, 3, 4]))]
    data_2012 = df_day[(df_day["yr"] == 1) & (df_day["weekday"].isin([0, 1, 2, 3, 4]))]

    count_2011 = data_2011.groupby("weekday")["cnt"].sum()
    count_2012 = data_2012.groupby("weekday")["cnt"].sum()

    labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    fig, ax = plt.subplots()

    ax.bar(labels, count_2011, width=0.4, label="2011", align="edge", color="blue")

    ax.bar(labels, count_2012, width=-0.4, label="2012", align="edge", color="orange")

    ax.set_xlabel("Hari dalam Seminggu")
    ax.set_ylabel("Jumlah Peminjam")
    ax.set_title("Perbandingan Jumlah Peminjam pada Weekday antara Tahun 2011 dan 2012")
    ax.legend()

    st.pyplot(fig)

    with st.expander("Penjelasan Perbandingan Peminjam Sepeda"):
        st.write(
            "Pada Grafik diatas, kita bisa mengetahui bahwa para peminjam sepeda sudah mengetahui dimana bisa meminjam sepeda. Oleh karena itu, data pada Weekday di tahun 2012 lebih tinggi daripada data Weekday pada tahun 2011."
        )

def angin(df_day):
    st.write("10122093 - Muhammad Fahreza Thias Akhzan")
    st.header(
        "Rata-Rata Windspeed Tiap Bulan Dari 2011 Hingga 2012"
    )
    st.write(
        "Untuk mengetahui rata-rata kecepatan angin yang terjadi setiap bulan dari 2011 hingga 2012."
    )
    
    df_day['dteday'] = pd.to_datetime(df_day['dteday'])

    df_day['year'] = df_day['dteday'].dt.year
    df_day['month'] = df_day['dteday'].dt.month

    data_day_filtered = df_day[(df_day['year'] >= 2011) & (df_day['year'] <= 2012)]

    avg_windspeed_per_month = data_day_filtered.groupby(['year', 'month'])['windspeed'].mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(avg_windspeed_per_month['windspeed'], marker='o')
    ax.set_title('Rata-rata Windspeed tiap Bulan (2011-2012)')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Rata-rata Windspeed')
    ax.set_xticks(range(0, 24))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
                        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax.grid(True)
    st.pyplot(fig)

    with st.expander('Penjelasan rata-rata kecepatan angin dari yang tertinggi dan terendah'):
        st.write('Dari grafik di atas, kita dapat mengetahui kecepatan angin yang tertinggi terjadi pada bulan April 2011. Sedangkan, kecepatan angin terendah terjadi pada bulan September 2011.')

def lembab(df_hour):
    st.write("10122099 - Muhammad Raffy Abdillah")
    st.header("Grafik Perubahan Kelembaban Setiap Jam pada 06-03-2012")
    st.write("Untuk mengetahui perubahan kelembaban setiap jam.")
    
    filtered_data = df_hour[df_hour['dteday'] == '2012-03-06']
    hrs = filtered_data['hr']
    humidity_percent = filtered_data['hum'] * 100
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(hrs, humidity_percent, marker='o', color='blue')
    ax.set_title('Kelembaban Terhadap Jam pada Tanggal 06-03-2012')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Kelembaban (%)')
    ax.set_xticks(range(24)) 
    ax.grid(True)
    
    st.write(fig)
    
    with st.expander('Penjelasan Perubahan Kelembaban'):
        st.write('Pada grafik di atas, pada jam 0 kelembaban menginjak di 37%. Kemudian naik secara cepat hingga 59% pada jam 8. Turun drastis hingga di bawah 35% pada jam 16. Hingga akhirnya naik secara signifikan hingga 61% pada jam 23.')


df_day = load_data(
    "https://raw.githubusercontent.com/rapilap/UjianAkhirSemester/main/day.csv"
)
df_hour = load_data(
    "https://raw.githubusercontent.com/rapilap/UjianAkhirSemester/main/hour.csv"
)

st.header(f"Dashboard Analisis Peminjaman Sepeda")
tab1, tab2, tab3 = st.tabs(["Analisis Peminjaman", "Analisis Kecepatan Angin", "Analisis Kelembaban"])

with tab1:
    peminjaman(df_day, df_hour)
with tab2:
    angin(df_day)
with tab3:
    lembab(df_hour)