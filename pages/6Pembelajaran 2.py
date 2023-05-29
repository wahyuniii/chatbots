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

# Pilihan Ganda
st.title("PEMBELAJARAN 2")

tab1, tab2 = st.tabs(["MATERI CAMPURAN", "KUIS CAMPURAN"])

with tab1:
    st.header("Campuran Homogen dan Heterogen")
    st.write("---")
    st.image("https://cdn1-production-images-kly.akamaized.net/OUqqLu3BtXjfJac0EtxLVMETVws=/1200x1200/smart/filters:quality(75):strip_icc():format(webp)/kly-media-production/medias/3128504/original/083078300_1589462572-shutterstock_435468841.jpg")
    st.subheader("Pernahkah kalian membuat es teh manis seperti pada gambar diatas?")
    st.write("Ketika kamu membuat es teh manis, berarti kamu telah membuat suatu campuran. Campuran yang dibuat olehmu yaitu campuran antara gula pasir dan air teh sebagai pelarut. Begitu pula saat kamu membuatkan kopi untuk ayahmu, kamu akan mencampurkan kopi, gula, dan air.")
    st.write("Pada dasarnya, suatu campuran dapat berupa unsur dengan unsur ataupun unsur dengan senyawa. Komposisi unsur-unsur atau senyawa penyusun suatu campuran tidak tertentu. Sifat asli zat-zat pembentuk campuran masih tampak, sehingga komponen penyusun campuran tersebut dapat dikenali dan dapat dipisahkan lagi. Ada dua macam campuran, yaitu campuran homogen dan campuran heterogen.")
    st.write("Untuk lebih memahami mengenai campuran, simak video berikut")
    st.video("https://youtube.com/watch?v=D8YDyTVGzxE&feature=share")
    st.write("---")
    submit = st.button("Percobaan tentang Campuran   \u2193")
    if submit:
        st.write("Nah setelah kalian mengamati video pembelajaran tersebut, sekarang kamu telah memahami tentang campuran dan mengetahui contoh-contoh campuran. Cobalah untuk bereksperimen dengan membuat campuran seperti pada kegiatan berikut.")
        st.write("Lakukan percobaan untuk menentukan jenis campuran beberapa zat/benda.")
        st.image("https://64.media.tumblr.com/ed2995d24b9caa410394a9c868197949/f13083098715fa81-e6/s640x960/b0f44c6d6f221204792c4b5bf1c4684910891a47.pnj")
        st.write("---")
        st.write("Untuk memahami langkah-langkah percobaan, simak video berikut!")
        st.video("https://youtube.com/watch?v=JkkmcdYNBCg&feature=share")

with tab2:
    def generate_questions():
        questions = [
            {
                'type': 'text',
                'question': 'Campuran yang zat penyusunnya tidak tercampur sempurna.merupakan pengertian dari campuran ...',
                'options': ['A.Unsur', 'B.Senyawa', 'C.Campuran homogen', 'D.Campuran heterogen'],
                'answer': 'D.Campuran heterogen'
            },
            {
                'type': 'image',
                'question': 'Gambar berikut merupakan contoh dari ....',
                'image': 'https://www.bodrexin.com/product_images/bodrexin-flubatukpe-rev-2210.png',
                'options': ['A.Campuran homogen', 'B.Campuran heterogen', 'C.Unsur', 'D.Senyawa'],
                'answer': 'A.Campuran homogen'
            },
            {
                'type': 'text',
                'question': 'Campuran antara air dan minyak merupakan salah satu contoh dari ....',
                'options': ['A.Campuran homogen', 'B.Campuran heterogen', 'C.Unsur', 'D.Senyawa'],
                'answer': 'B.Campuran heterogen'
            },
            {
                'type': 'text',
                'question': 'Berikut yang merupakan contoh campuran adalah ....',
                'options': ['A.Air', 'B.Gula', 'C.Garam', 'D.Sirup'],
                'answer': 'D.Sirup'
            },
            {
                'type': 'text',
                'question': 'Materi yang memiliki zat penyusun terdiri dari air mineral dan garam adalah ....',
                'options': ['A.Air kopi', 'B.Air teh', 'C.Air minum', 'D.Air garam'],
                'answer': 'D.Air garam'
            },
            {
                'type': 'text',
                'question': 'Berikut ini yang termasuk campuran heterogen dalam kehidupan sehari-hari adalah ....',
                'options': ['A.Air garam', 'B.Air kopi', 'C.Air gula', 'D.Air susu'],
                'answer': 'B.Air kopi'
            },
            {
                'type': 'text',
                'question': 'Berikut ini yang termasuk campuran homogen adalah ....',
                'options': ['A.Larutan gula, air dengan minyak, dan air kopi', 'B.Air dengan minyak, air kopi, dan larutan oralit', 'C.Larutan oralit, larutan gula, dan sirop', 'D.Sirop, air dengan pasir, dan udara'],
                'answer': 'C.Larutan oralit, larutan gula, dan sirop'
            },
            {
                'type': 'image',
                'question': 'Gambar berikut merupakan contoh dari....',
                'image': 'https://statics.indozone.id/do_692x516/content/2020/08/12/gms7d3D/t_5f338f6d8ac25_700.jpg',
                'options': ['A.Zat Tunggal', 'B.Campuran heterogen', 'C.Senyawa', 'D.Unsur'],
                'answer': 'B.Campuran heterogen'
            },
            {
                'type': 'text',
                'question': 'Minuman teh yang dibuat dengan teh tubruk termasuk kedalam zat ....',
                'options': ['A.Campuran homogen', 'B.Campuran heterogen', 'C.Senyawa', 'D.Unsur'],
                'answer': 'B.Campuran heterogen'
            },
            {
                'type': 'text',
                'question': 'Tepung yang sudah tercampur dengan air apabila didiamkan beberapa saat, di dasar wadahnya akan terlihat air dan tepung itu memisah. Peristiwa tersebut merupakan contoh dari ....',
                'options': ['A.Zat tunggal', 'B.Campuran', 'C.Campuran homogen', 'D.Campuran heterogen'],
                'answer': 'D.Campuran heterogen'
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
        st.title('Kuiz Pembelajaran 2- Campuran Homogen dan Heterogen')
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
   want_to_pemb = st.button("Next   \u25B6   About")
if want_to_pemb:
   switch_page("About")
