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
st.title("PEMBELAJARAN 1")
st.write("---")

tab1, tab2 = st.tabs(["MATERI UNSUR DAN SENYAWA", "KUIS UNSUR DAN SENYAWA"])

with tab1:
    st.header("MATERI UNSUR DAN SENYAWA")
    st.subheader("Perhatikan gambar berikut!")
    st.image("https://i.ytimg.com/vi/EaRZnpabMEA/maxresdefault.jpg", width=320)
    st.subheader("Apa saja manfaat air dalam kehidupan?")
    st.write("Air sangat kita butuhkan dalam berbagai hal sehari-hari seperti mandi, mencuci alat-alat rumah tangga, dan mencuci baju. Air merupakan benda tunggal. Akan tetapi, sebenarnya air terbentuk atas hidrogen dan oksigen. Hidrogen dan oksigen dalam air tidak dapat dipisahkan, kecuali dengan reaksi kimia tertentu. Berbeda dengan tanah. Dalam tanah dapat kamu jumpai adanya kerikil, batu, dan pasir yang dapat kamu pisahkan dengan tangan.")
    submit = st.button("Apa itu zat tunggal dan campuran?  \u2193")
    if submit:
        st.write("Secara umum, benda-benda di lingkungan sekitar kita (materi) dapat dibedakan menjadi dua, yaitu zat tunggal dan campuran.")
        st.write("Untuk lebih memahami mengenai zat tunggal dan campuran, Mari amati video berikut ini")
        st.video("https://youtube.com/watch?v=vEa1I5CQGwQ&feature=share")
        st.write("---")
        st.write("Nah setelah kalian mengamati video pembelajaran tersebut, tentu sekarang kalian sudah paham tentang unsur dan campuran")
        st.write("Untuk mengukur pemahaman kalian, mari kerjakan kuis dengan menekan tombol KUIS pada bagian atas")
        

with tab2:
    def generate_questions():
        questions = [
            {
                'type': 'text',
                'question': 'Gabungan dari dua zat atau lebih yang sifat asalnya tidak hilang sama sekali disebut....',
                'options': ['A.Zat Tunggal', 'B.Unsur', 'C.Senyawa', 'D.Campuran'],
                'answer': 'D.Campuran'
            },
            {
                'type': 'image',
                'question': 'Gambar berikut merupakan contoh dari ....',
                'image': 'https://storage.googleapis.com/palma/mandau/-FaMfICji3uQwpTgGmKC.jpeg',
                'options': ['A.Campuran homogen', 'B.Campuran heterogen', 'C.Unsur', 'D.Senyawa'],
                'answer': 'C.Unsur'
            },
            {
                'type': 'text',
                'question': 'Ibu Ani kepasar membeli aluminium, gula pasir, garam dapur, perak, besi dan vitamin C. Dari Barang yang  dibeli Ibu Ani, yang termasuk kelompok senyawa adalah....?',
                'options': ['A.Gula pasir, garam dapur dan vitamin C', 'B.Aluminium, perak dan besi', 'C.Gula pasir, garam dapur dan besi', 'D.Aluminium, perak dan vitamin C'],
                'answer': 'A.Gula pasir, garam dapur dan vitamin C'
            },
            {
                'type': 'text',
                'question': 'Pernahkah kamu berwisata di laut dan melihat aliran ombak dilaut yang begitu indah. Air laut merupakan contoh dari ....',
                'options': ['A.Campuran', 'B.Senyawa', 'C.Unsur', 'D.Zat tunggal'],
                'answer': 'A.Campuran'
            },
            {
                'type': 'text',
                'question': 'Benda atau materi yang berada di lingkungan sekitar dapat memberikan manfaat bagi kehidupan. Sebagai contoh, garam adalah zat tunggal yang merupakan senyawa. Salah satu manfaat garam adalah ....',
                'options': ['A.Sebagai bahan makanan pokok', 'B.Untuk mencuci pakaian', 'C.Untuk memasak', 'D.Untuk mengusir ular'],
                'answer': 'C.Untuk memasak'
            },
            {
                'type': 'text',
                'question': 'Unsur dan senyawa termasuk kedalam ....',
                'options': ['A.Campuran homogen', 'B.Campuran homogen', 'C.Campuran', 'D.Zat tunggal'],
                'answer': 'D.Zat tunggal'
            },
            {
                'type': 'text',
                'question': 'Senyawa apa yang digunakan untuk mengawetkan makanan?',
                'options': ['A.Gula pasir', 'B.Asam cuka', 'C.Garam', 'D.Vitamin A'],
                'answer': 'C.Garam'
            },
            {
                'type': 'image',
                'question': 'Gambar berikut merupakan contoh dari....',
                'image': 'https://lh3.googleusercontent.com/pw/AJFCJaU7PQfE0l4phDZqACJmDg-TIwAVJjEtuuW3CQCl3rzZhwp2Tv1d97OLOcaWlNX_Vd7xb2T2mRvR69VZM_7iuaf4OSmv00Ss_xrUsHQTpxGVT3fv554O31-SnY-sSYLPFixVT-B5hzhU2T3tPgjrfOVHAvyRi0Ifho4DPtwNmc-pt-ug2fXa8u7JsP-6MmKRr-no5drNM3Ios6u-EiEmqGttak-nTJAQyhijz57H5_83RKz-9LHPWl7TpCX9CTaHzpFwmtLRoFCNKc2JaK5X4CXaF3eCzJdyaIhQE8ySFdPr-yQ9e9URGq5S_IDRXN7EqpgxBwj2mSPnwuxpjLMF4bEihlsN1PKxfjtfdUCFmlj6rNX8ITn7jIxpkPn_1UGZkVApmM2mplkoDMexMqMfYeEJBCBFP1lcY7dQ5iQ8X1Z8eVCx38-dzfHvwFXK2aSeviG62Qmzbhlr8XDlku6kbwDpV41hEUfvNpvBIugTA53IWf__O-R5gBl4VdUYLsW3rgZTrNyIUZ7Lp1JFjfRqVBH2djYaqm2hOW2NFZWgk26gkpznqvMGKX37aixys1ZmNNY7AyD6RgGXMgEb9Wv09zVnik7pRHTL_Ma0RuZ1C4hFTu0daclOVNSpmLG-vA4cSKUDpxrONO6y-_f_bmUXtLitoA043vC7d-3i6Wy5ClcyXVSFXYKmOMzuoqcNi111FmRMxNwxRgFXW3SSxiNgRiIjQISXWQzXd7efPCy60zX671gTXAUNV80ewNf1fJnR0jyrjnpCGA2FMIO_oixCYMz6RlmCqtG2tdAQU9kByhKR1kforvwo1arRnDSd-Tte2HAG4UxvPhRnjuHRRcAEXnjvVOg-_aZfb731ThIGTK6DwPj0ZV-omxNvcVfzd-cLfs8wWaOuboYkKVnMwhmCjw=w600-h600-s-no?authuser=0',
                'options': ['A.Zat Tunggal', 'B.Campuran heterogen', 'C.Senyawa', 'D.Unsur'],
                'answer': 'Campuran Homogen'
            },
            {
                'type': 'text',
                'question': 'Gula pasir, garam dapur, dan asam cuka termasuk contoh dari ....',
                'options': ['A.Campuran homogen', 'B.Campuran heterogen', 'C.Senyawa', 'D.Unsur'],
                'answer': 'C.Senyawa'
            },
            {
                'type': 'text',
                'question': 'Zat tunggal terdiri dari unsur dan senyawa. Berikut ini merupakan contoh dari unsur adalah ....',
                'options': ['A.Soda kue', 'B.Besi', 'C.Vitamin A', 'D.Garam'],
                'answer': 'B.Besi'
            },
        ]
        return questions

    def display_question(question):
        if question['type'] == 'text':
            st.write('**Pertanyaan:**', question['question'])
            selected_option = st.radio('Pilih jawaban Anda:', question['options'])
        elif question['type'] == 'image':
            st.write('**Pertanyaan:**', question['question'])
            st.image(question['image'], use_column_width=True)
            selected_option = st.radio('Pilih jawaban Anda:', question['options'])
        else:
            pass
        return selected_option

    def main():
        st.title('Kuiz Pembelajaran 1- Unsur dan Senyawa')
        st.write('Jawablah pertanyaan-pertanyaan berikut.')
        questions = generate_questions()
        num_questions = len(questions)
        current_question = 0
        score = 0

        if 'current_question' in st.session_state:
            current_question = st.session_state.current_question
        if 'score' in st.session_state:
            score = st.session_state.score

        if current_question < num_questions:
            selected_option = display_question(questions[current_question])
            st.write('---')
            if st.button('Next', key='next_button', help='Jawaban Anda akan dikunci saat tombol Next ditekan'):
                if selected_option == questions[current_question]['answer']:
                    score += 1
                current_question += 1
        else:
            st.write('Anda telah menjawab semua pertanyaan.')
            st.write('Skor akhir Anda:', score, '/', num_questions)

        st.session_state.current_question = current_question
        st.session_state.score = score

    if __name__ == '__main__':
        main()


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
st.write("---")
st.write("---")
st.write("---")
st.write("---")

from streamlit_extras.switch_page_button import switch_page

col1, col2= st.columns(2)
with col1:
   want_to_menu = st.button("\u25C0   Menu")
if want_to_menu:
   switch_page("Menu")
 
with col2:
   want_to_pemb = st.button("Next   \u25B6   Pembelajaran 2")
if want_to_pemb:
   switch_page("Pembelajaran 2")
