import streamlit as st

st.title("This is title")
st.text("Lorem ipsum di Almet.")
st.header("This is header")

nama = st.text_input(label="Nama", value="Masukan nama anda disini", key="input1")
nim = st.text_input("NIM", key="input2")
# alamat = st.map() 

if nama :
    st.text("Nama: "+ nama)
    if len(nim) == 10 :
        st.text("NIM: "+nim)
box = st.selectbox("Pilih jurusan: ", ["RPL", "IF", "DS"])
st.write(box)

Umur = st.slider("Umur", 1, 70, 10)
st.write(Umur)

Gender = st.radio('Gender', ['Pria', 'Wanita'])
if Gender=='Pria' :
    st.write(f"Welcome Mr.{nama}")
else :
    st.write(f"Welcome Mrs.{nama}")

list_hobi = st.text_area("Hobi", "Main bola, Main game")
list_hobi = [x.strip() for x in list_hobi.split(',')]

st.write(list_hobi)

st.divider()
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/640px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg", caption="picture of Mona Lisa", width=250)

st.markdown('[ini link ke bing](https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=undexpand)')

import pandas as pd

data = {'Pekerjaan': ['Programmer', 'Dokter', 'Pengacara'], 
        'Tier': ["E", "SS", "A"]}
df = pd.DataFrame(data)
st.dataframe(data=df, use_container_width=True)

st.title("Buka Data")
file = st.file_uploader('Pilih file jpg', type=['jpg', 'csv'])

if file is not None:
    st.write(file.type)
    
    try :
        if file.type == "image/jpeg" :
            st.image(file)
        else :
            data = pd.read_csv(file)
            st.dataframe(data)
    except :
        st.warning("Type File Error")

num1 = st.number_input("Masukkan angka 1 ", value=0)
num2 = st.number_input("Masukkan angka 2 ", value=0)

operasi = st.radio('Pilih Operasi', ["Penjumlahan (+)", "Pengurangan (-)", "Pembagian (/)", "Perkalian (*)", "Eksponensial (**)", "Modulo (%)"])
if st.button('hitung'):
    if operasi == "Penjumlahan (+)":
        hasil = num1+num2
    elif operasi == "Pengurangan (-)":
        hasil = num1-num2
    elif operasi == "Pembagian (/)":
        hasil = num1/num2
    elif operasi == "Perkalian (*)":
        hasil = num1 * num2
    elif operasi == "Modulo (%)":
        hasil = num1 % num2
    else :
        hasil = num1**num2
    
    st.success(f'Hasil {operasi} : {hasil}')

st.sidebar.title('Menu')
st.sidebar.header('Profile')
if st.sidebar.checkbox('Biodata'):
    st.sidebar.write(f"Nama: {nama}\nNIM: {nim}")