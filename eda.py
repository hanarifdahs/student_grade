import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    # Membuat Title
    st.title('Aplikasi Prediksi Nilai Akhir Siswa')

    # Membuat Sub Header
    st.subheader('Page ini berisi Exploratory Data Analysis dari dataset Student Performance')

    # Menambah gambar
    gambar = Image.open('./src/gambar_siswa.jpg')
    st.image(gambar, caption='Siswa kesulitan belajar')

    # Menambah Teks
    st.write('Page ini dibuat oleh *Angelica Zalisca*')
    st.write('### Data Frame')

    # Menampilkan Dataframe
    data = pd.read_csv('student_data.csv')
    st.dataframe(df)

    # Distribution of G3
    st.write('### Distribusi Nilai Akhir (G3)')
    plt.figure(figsize=(10, 6))
    sns.histplot(data['G3'], bins=20, kde=True)
    plt.title('Distribution of Final Grades (G3)')
    plt.xlabel('Final Grade (G3)')
    plt.ylabel('Frequency')
    st.pyplot(plt)

    # Distribution Age
    st.write('### Distribusi Umur Siswa')
    plt.figure(figsize=(10, 6))
    sns.histplot(data['age'], bins=8, kde=True)
    plt.title('Distribution of Age')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    st.pyplot(plt)

    # Study time vs Final Grade
    st.write('### Waktu Belajar vs Nilai Akhir')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='studytime', y='G3', data=data)
    plt.title('Study Time vs Final Grade')
    plt.xlabel('Study Time')
    plt.ylabel('Final Grade (G3)')
    st.puplot(plt)

    # Family relationship vs Final Grade
    st.write('### Hubungan Keluarga vs Nilai Akhir')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='famrel', y='G3', data=data)
    plt.title('Family Relationship vs Final Grade')
    plt.xlabel('Family Relationship Quality')
    plt.ylabel('Final Grade (G3)')
    st.pyplot(plt)

    # Free time vs Final Grade
    st.write('### Waktu Luang vs Nilai Akhir')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='freetime', y='G3', data=data)
    plt.title('Free Time vs Final Grade')
    plt.xlabel('Free Time')
    plt.ylabel('Final Grade (G3)')
    st.pyplot(plt)

    # Alcohol consumption vs Final Grade
    st.write('### Konsumsi Alkohol vs Nilai Akhir')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Dalc', y='G3', data=data)
    plt.title('Workday Alcohol Consumption vs Final Grade')
    plt.xlabel('Workday Alcohol Consumption')
    plt.ylabel('Final Grade (G3)')
    st.pyplot(plt)

if __name__ == '__main__':
    run()