import streamlit as st
import qrcode
st.set_page_confiq("QR GEN",page_icon="QR GEN.png")
st.title("QR CODE GENERATOR")

qr_data = st.text_input("Enter the link to generate qrcode:")

if st.button("Generate QR CODE")
     if qr_data:
         img = qrcode.make(qr_data)
         img.save("random.png")
         st.image(image="random png")

      else:
          st.warning("please enter data to generate the QR code.")
st.write("All copy right reserved @ 2024 Shahim mughal")