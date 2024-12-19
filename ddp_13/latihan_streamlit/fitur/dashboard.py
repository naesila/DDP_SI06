import streamlit as st

st.title("Halaman dashboard")
st.image("images.jpg", caption="Bank Tokyo")

# fungsi menghitung dan menghitung total
def total():
    total_nabung = sum(v['Jumlah']
    for v in st.session_state['total_semua']
    if v ['Tipe'] == 'Menabung')
    return total_nabung

total_semua = st.session_state['total_semua']
total_nabung = total()

st.metric("Total Menabung", f"Rp {total_nabung}")
                    
    
    
