import streamlit as st

# Judul aplikasi
st.title("🏦 ATM Virtual 🏦")

# Menyimpan saldo awal di session state jika belum ada
if "uang_saya" not in st.session_state:
    st.session_state.uang_saya = 0

# Menyimpan riwayat transaksi di session state jika belum ada
if "riwayat_transaksi" not in st.session_state:
    st.session_state.riwayat_transaksi = []

# Fitur Keamanan (PIN)
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "username" not in st.session_state:
    st.session_state.username = ""

def login():
    # Meminta pengguna untuk memasukkan nama pengguna
    username = st.text_input("Masukkan Nama Pengguna")
    pin = st.text_input("Masukkan PIN Anda", type="password")
    
    if st.button("Login"):
        # Validasi jika nama pengguna dan PIN benar
        if username and pin == "1234":
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success(f"Login berhasil! Selamat datang, {username}.")
        else:
            st.error("Nama pengguna atau PIN salah. Coba lagi!")

# Menu utama hanya tampil jika user berhasil login
if not st.session_state.authenticated:
    login()
else:
    # Menampilkan nama pengguna yang berhasil login
    st.sidebar.write(f"👋 Selamat datang, {st.session_state.username}!")
    
    # Menu utama
    st.sidebar.title("💰 Menu 💰")
    option = st.sidebar.radio("Pilih opsi transaksi:", ["Cek Uang Saya", "Ambil Uang Saya", "Tabung Uang Saya", "Riwayat Transaksi", "Logout"])

    # Fungsi untuk cek saldo
    def cek_uang():
        st.subheader("💸 Cek Uang Saya 💸")
        st.write(f"💵 Saldo Anda saat ini: Rp {st.session_state.uang_saya} 💵")

    # Fungsi untuk ambil uang
    def ambil_uang():
        st.subheader("Ambil Uang Saya")
        st.write(f"Saldo Anda saat ini: Rp {st.session_state.uang_saya}")
        jumlah_ambil = st.number_input("Masukkan jumlah uang yang ingin diambil:", min_value=0, step=1)
        
        if st.button("Ambil Uang"):
            if st.session_state.uang_saya - jumlah_ambil < 0:
                st.error("Saldo tidak mencukupi!")
            else:
                st.session_state.uang_saya -= jumlah_ambil
                st.session_state.riwayat_transaksi.append(f"Ambil Uang: Rp {jumlah_ambil}")
                st.success(f"Berhasil mengambil uang sebesar Rp {jumlah_ambil}")
                st.write(f"Saldo Anda sekarang: Rp {st.session_state.uang_saya}")

    # Fungsi untuk tabung uang
    def tabung_uang():
        st.subheader("Tabung Uang Saya")
        st.write(f"Saldo Anda saat ini: Rp {st.session_state.uang_saya}")
        jumlah_tabung = st.number_input("Masukkan jumlah uang yang ingin ditabung:", min_value=0, step=1)
        
        if st.button("Tabung Uang"):
            st.session_state.uang_saya += jumlah_tabung
            st.session_state.riwayat_transaksi.append(f"Tabung Uang: Rp {jumlah_tabung}")
            st.success(f"Berhasil menabung uang sebesar Rp {jumlah_tabung}")
            st.write(f"Saldo Anda sekarang: Rp {st.session_state.uang_saya}")

    # Fungsi untuk menampilkan riwayat transaksi
    def riwayat_transaksi_fn():
        st.subheader("Riwayat Transaksi")
        if st.session_state.riwayat_transaksi:
            for transaksi in st.session_state.riwayat_transaksi:
                st.write(transaksi)
        else:
            st.write("Tidak ada riwayat transaksi.")

    # Fungsi untuk logout
    def logout():
        st.session_state.authenticated = False
        st.session_state.username = ""
        st.success("Anda telah logout.")

    # Menjalankan fungsi sesuai opsi yang dipilih
    if option == "Cek Uang Saya":
        cek_uang()
    elif option == "Ambil Uang Saya":
        ambil_uang()
    elif option == "Tabung Uang Saya":
        tabung_uang()
    elif option == "Riwayat Transaksi":
        riwayat_transaksi_fn()
    elif option == "Logout":
        logout()

    # Footer
    st.sidebar.write("---")
    st.sidebar.write("Terima kasih telah menggunakan ATM Virtual!")



# CSS to Streamlit 
st.markdown(
    """
    <style>
    /* Warna latar belakang aplikasi */
    .stApp {
    
        background-color: ; /* Ganti dengan warna latar belakang yang sesuai */
        background-size: 3830 x 2160px; /* Mengatur ukuran gambar latar belakang */
        background-image: url('https://img.freepik.com/premium-vector/us-dollar-value-rising-due-interest-rate-hike-exchange-rate-financial-report-economy-investment-concept-businessman-investor-look-dollar-sign-rocket-flying-high-exchange-chart_212586-1872.jpg?w=1020')
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #2F4F4F; 
        color: ;
        padding: 0px;
        border-radius: 0px;
    }
       
    /* Teks pada sidebar */
    [data-testid="stSidebar"] * {
        color: white !important; 
        font-size: 20px;
        margin-bottom: 10px;
        margin-top: 3px;
    }

    /* Judul aplikasi */
    h1 {
        color:rgb(39, 148, 15); 
        text-align: center; 
        font-family: 'Arial', sans-serif; 
        font-size: 77px;
        margin-bottom: 20px; 

        
    }

    /* Tombol */

    .stButton > button {
        background-color:rgb(42, 98, 41); 
        color: white; 
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer 
    }

    .stButton > button:hover {
        background-color:rgb(224, 9, 9); 
    }

    /* Subheader */
    h2 {
        color: #FFFFFF; 
        font-family: 'Arial', sans-serif;
        margin-top: 20px; 
    }

    /* Footer */
    .stSidebar > div:last-child {
        margin-top: 10px;
        font-size: 7px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)