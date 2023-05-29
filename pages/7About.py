import streamlit as st

# Menghilangkan tombol Menu
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Mengganti Background dengan gambar
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://lh3.googleusercontent.com/pw/AJFCJaVPqM4Ovxxk0i1fCqFSE4r8S1G9dc1EaCeyGJl9XGxk2OEVsbBeEjjU3lbTSlRGUUcRoQ0z35IHNejGALDXaMwlAAPkkwTJGFQlAxFMAk1fLS-dPTJe-kP0fM9RPqjFdw_InzVCylKF2NI_6BSsi4zOWvmTxDIkXyrrEjVwyDKdwvysmrmp0jNv81lw1Qr7QSwkWbadFEzGA4I0zkBSo7VF3KKc3ebPHMlncP4ywlsIvRKqVzG3AoN2VQ7M6MPpQ4Uoxnd4TuaWjqq7HLXzV7mq8GukRFY4hAuuc8VQxcKG8VrdvPV5XhLCYJ-sa44l8QH6znZrjg1YDwHXjSf6GZSfF3owuBFO1zLqqkK5Ej3PmAlkwMSu47_b0RlY5ebt9SVJ1ScsFmAQgtgGWMWt9F7gKvDC_SzmPNdMVy2_JqdfqPHfIAeEKTw6RGKOxsh-Rc1a1Opmt6sOlvqbbi_LxBxikcqbd_1-je3rgSz4XidygZLGo6fq-FI9JgLdhIRbYd0LVWbjarJJS_TSyJrlVhugYTqD5rt7GiW08neVe2mbbEyoPlaZkw2mpYBSdy4pP7WQaS99rNgtLEeFdrm_rJQrlIIU5VBKqhnihlb17_tmL0O9161SzocfBFrs79K1idPe1cFrE0bV1kGo08rDfDjnLWnvIYNN0E2eCwx9JOegkaWDvhNyh_gegboes5gDoT21fJCA0Cvb5rhdYea9byPhRcxJsxmeiXWP3E02okvzktBH3SI6cP5KZ7vEZEXxurfknl-jHmXLX30fa1jpv5VO0EC44XV3EYc6hLrowWPNVYloowiUd_9meQiQfULHhStxVlDtCh7yVCl09UkoOpX9pMkM5LZnHGELLq4Cy-4JPNHVhNp1RTx1EwccKMT8RaQogzkmBKrbnC1UFLebMg=w329-h600-s-no?authuser=0");
background-size: cover;
}

[data-testid="stHeader"] {
background-color: rgba{0, 0, 0, 0};
}

[data-testid="stToolbar"] {
right: 2rem;
}

[data-testid="stSidebar"] {
background-image: url("https://lh3.googleusercontent.com/pw/AJFCJaWhQxmAjv6xcNJiAaUZdHVEIINj4-r2bcsEgpMcnT3xf0mVfmKaJgSq2DF4SKLbhcmi2519LFX03zc47WKxXbRDew0jk7nBWjuiLgYbW2H4eMsq8gVmZb4K0zKwsscRNqQgu22Tw6VmzvfJDHnvawnTfNa6BhpioXW9qE5tHvJXe4GZKbnJwIjbevW89DKoRcJbsbZr0Poi-mohOcb0GDvGS0k4-G0fmu75Or-y1zYmPTjnL-PMVDFBzT7xecuewLd01CEs3Rz4Oulb4o0NEl53Hz3TCNWQ4yotcqvXyR754AtUKzXmNS4sd_ERIxQ4S4JMseCuQ-JPER3I3vLoC7Y3PCz9KGPrQZt0xWJOD0wMJsHviA4qc1HUaYIAMSWhIvVthNjNJyNhCbQxt2KgMgSThDRokZLDdk-AUoeVCTC4EsgmE0iGsJYK2UROqitHuXZVFRdUiJ4wu0PD7ABQ5eBE0EGwN3b1Q1NymO8BrsQWgHXsUN4C57tn2DhEP8S1VRUZWTFIZADDNmwuD7j-MDwp01NjFHZiUd5Y2Yia9BM1o_g4mI9Y1QwNSyvyyRl8TsVRCqNkvi56mKz_z9v9C9a9D8vAxzsQppkO0Jr2vC93o5xUJ0qwknBwlRsNSKAcRdCJQbRnT13MCpeVsbHRMOwtbcvo0K1kqzHg9hsaGI45fl_vXfGlrTRgwuRRQAK5S5lzk1I-GE4Fv2Tg63X7mHYA3Uaqd1fJ6x8LivCjO5nDXpWv_Q4JD9e-hFuE8MNri7GLAPVV2M4aWXeobnRpPt5lI9lMSeHpB8jGsVTwbpwc8s_lsB1ebCW3kbdADKoH36rUoymWRXlW8GSyBxGDa-FaIzfEvEHNnI1kygm6qnpQgqIARWGzGZtJPgOkN2jZvtvTVnH8qj22JLAoARMR-Q=w288-h600-s-no?authuser=0");
background-size: cover;
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Mulai Title
st.title("Pengembang Zatacbot")
st.write("---")
st.image("https://lh3.googleusercontent.com/pw/AJFCJaUV4G8Z0eXozTh6U49Oecvd_bMCne2fgGer_VZmJyTAlsXtbJZ_36_YtNvBLfUt1ohlqTu1LZ4sXRfWi4cb50ZOVyky4kiro6ElZk2OnJiYRZCeZcGZn1Iv03CaIHw5Wjn52jV-rLGmnqWgs6MBO2d4biDlrMMDy_1hzvB4qjxePn4M1x1ML3-syR0xU7oT4dnl8pdq4UfT1ci93cvknzn6CpjwfX_nwCmwfK1gETlfZh093DevlMPAqN1ud9QRoXbcWSk8vA70chfi1uHJGzJ7CtM9vtQalpBVvas0O5dxs5R5Qj3QqJXRV1iEnsgCmFShqT5LbDlHCYJRRr7_8izXxJFh2Rrj7-O2et_zeGi4pzzsZE9SKQvghJYAUiTYGVYLFu8fBTYzsgPcyuRm871aDVXRAEgUFEfTXsWVzh1G_hurxEmha-u7sIxhReXB3Gl0RPx3fMTpZ9qWTmdGB-_lWx1wvRtHntYtRcDE4q0KbOhwpkDG91FAmX_IzG1EldA-JtWx1RkTBfn9ruKj6XJKK0oUZMkckKYVHG1lDYTzAmVU5rZFyQo72LdjjOSoNLZwFJEVJ4uG43fBW0OrZyWI9vLGOhfybeRBrnhYTh6Cqd6tiHWn_jAstU43tdOiNki-v35KA2GxAPKexsq8sxNQpJ3lBebUqc4yRAtF9uWNYlq3tBej4qHXq7mW-LuqOLvrAYRvus8xmSoep8y1CRDewxY2tmgPFYaHalKv8o9F-KQ_f1k_k5v1v__NC_hhq2rHh_0rONoKUBzk7HEoj_2j9_qPW34npSm6WzUHpjflwNZyQWZmOpo7rhz808xBIq0nAAkERUw2GO5ev8VCgpfI68qim8-0_Cb-IANY1o3Hl1DBSbDJW1W0KsW-RbfOSYwUIp9olbP-RspK9ljnGA=w450-h600-s-no?authuser=0", width=200)

st.write("---")
st.write("Nama: Wahyuni")
st.write("Alamat: Cilacap, Indonesia")
st.write("Instansi: Universitas Negeri Semarang")
st.write("Fakultas: Ilmu Pendidikan")
st.write("Jurusan: Pendidikan Guru Sekolah Dasar")
st.write("---")
st.write("Untuk saran dan masukan hub: 085758447988")


#Ganti Page Berdampingan
st.markdown(
    """
    <style>
    .stButton button {
        font-size: 18px;
        background-color: #ff8c00; /* Ubah dengan kode warna coklat pastel yang diinginkan */
        color: white;
        width:100%
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("---")

from streamlit_extras.switch_page_button import switch_page

want_to_menu = st.button("\u25C0   Menu")
if want_to_menu:
   switch_page("Menu")



