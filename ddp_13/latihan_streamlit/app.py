import streamlit as st

#st.title("Hello world")
#st.markdown("Selamat datang di Tokyo")
#st.image("images.jpg", caption="ini gambar")

dashboard = st.Page("./fitur/dashboard.py", title="dashboard")
nabung = st.Page("./fitur/nabung.py", title="Menabung")

pg = st.navigation(
    {
     "Menu utama" : [dashboard],
     "Transaksi" : [nabung],
    }
)

if 'total_semua' not in st.session_state:
    st.session_state['total_semua'] = []

pg.run()