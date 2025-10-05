# Product data

import streamlit as st
# Initialize session state for selected product
if 'selected' not in st.session_state:
    st.session_state['selected'] = None

products = [
    {
        "name": "Chocolate Delight Hamper",
        "price": 799,
        "image": "https://i.imgur.com/x3Jw0lV.jpg",
        "description": "Assorted chocolates in a decorative box."
    },
    {
        "name": "Greeting Card & Treats",
        "price": 599,
        "image": "https://i.imgur.com/lHvhvCd.jpg",
        "description": "Handpicked greeting card plus small treats."
    },
    {
        "name": "Festival Combo Hamper",
        "price": 999,
        "image": "https://i.imgur.com/H3Xq6hx.jpg",
        "description": "Sweets, snacks, and decorative greeting card."
    }
]


st.title("🎁 Gift Hampers Store")
st.write("Choose your perfect gift hamper:")

for product in products:
    st.image(product["image"], width=200)
    st.subheader(product["name"])
    st.write(product["description"])
    st.write(f"Price: ₹{product['price']}")
    if st.button(f"View {product['name']}"):
        st.session_state['selected'] = product
        st.experimental_rerun()
        
if st.session_state['selected']:
    product = st.session_state['selected']
    st.header(product["name"])
    st.image(product["image"], width=300)
    st.write(product["description"])
    st.write(f"Price: ₹{product['price']}")

    st.write("### Place Your Order")
    st.write("Click below to contact via WhatsApp or Instagram:")

    whatsapp_link = "https://wa.me/91XXXXXXXXXX?text=Hi! I want to order this hamper."
    insta_link = "https://www.instagram.com/yourfriend_insta/"

    st.markdown(f"[💬 WhatsApp]({whatsapp_link})", unsafe_allow_html=True)
    st.markdown(f"[📸 Instagram]({insta_link})", unsafe_allow_html=True)

    if st.button("Back to Shop"):
        st.session_state['selected'] = None
        st.experimental_rerun()

