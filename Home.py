import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_extras.stateful_button import button


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
st.title("HAI DENGAN ZATACBOT DISINI :wave:")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://assets2.lottiefiles.com/packages/lf20_3vbOcw.json"
lottie_html = f'<div class="lottie" style="background-color: #FF000;"><lottie-player src="{lottie_url_hello}" background="transparent" speed="1" loop autoplay></lottie-player></div>'
st.markdown(lottie_html, unsafe_allow_html=True)
lottie_hello = load_lottieurl(lottie_url_hello)

st_lottie(lottie_hello, key="hello")

# Menambahkan CSS untuk mengatur teks menjadi rata tengah, besar, dan latar belakang teks
import streamlit as st


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

st.markdown(
    """
    <style>
    .my-text {
        font-size: 16px;
    }
    .stTextInput input {
        background-color: #B0E0E6;
    }
    .stTextInput label {
        font-size: 20px;
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="my-text">Untuk mulai belajar, tuliskan Namamu pada kolom dibawah ini kemudian tekan Submit  \u2193  \u2193  \u2193</p>', unsafe_allow_html=True)

my_input = st.text_input(st.session_state["my_input"])

submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.markdown(f"Selamat datang **{my_input}**, Zatacbot siap menemani belajarmu")
    st.write("Sebelum memulai belajar, bacalah petunjuk penggunaan Zatacbot terlebih dahulu ya")
    st.image("https://64.media.tumblr.com/77c5c4c51d2ea3df5b71138a19ad63f6/e708fdafee49a5db-7c/s400x600/821765f7145c3ba7b58249eeaf3e2528df374a1d.pnj", width=340)

# Tulis