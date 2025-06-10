import streamlit as st

st.set_page_config(page_title="Birthday Surprise Dee", layout="centered")

st.markdown("""
<style>
    body { background: #fefbe0; color: #333; }
    .card { background: #ffffff; border-radius: 12px; padding: 20px; margin: 20px auto; max-width: 400px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    .btn { background: #ff9a9e; color: white; padding: 10px 24px; border: none; border-radius: 8px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="card"><h2>🎉 HAPPY BIRTHDAY DEE!</h2></div>', unsafe_allow_html=True)

if "idx" not in st.session_state:
    st.session_state.idx = 0

messages = [
    "Awkward betul nk wish gini HAHAHAHA",
    "Saje buat gini biar nmpak effort tu ade HEHE",
    "First time ni aku buat bende gini, special sikit.",
    "Tiber betulla,",
    "Sbenanya nk bg gift, tp duit cukup utk keperluan je HAHAHA",
    "Tkpee, nnti tahun depan aku bagi la Gift. buat part timee abih exam nnti haha.",
    "Sekali lagi, Happy Birthday, semoga sentiata dalam lindungan nyaaaa.",
    "Tu je byee......."
]

if st.session_state.idx < len(messages):
    st.markdown(f'<div class="card"><p>{messages[st.session_state.idx]}</p></div>', unsafe_allow_html=True)
    if st.button("👉 Next", key="txt_btn"):
        st.session_state.idx += 1
else:
    st.success("✅ Semua dah! Tapi tunggu… ada satu soalan lagi!")

    if "q_idx" not in st.session_state:
        st.session_state.q_idx = 0
        st.session_state.no_count = 0
    
    if st.session_state.q_idx == 0:
        st.markdown('<div class="card"><p>Btw... mu rindu akuu takk? 😗</p></div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("YES"):
                st.session_state.q_idx = 1
        with col2:
            if st.button("NO"):
                st.session_state.no_count += 1

    else:
        st.success("💕 Alaa sweetnyaaa 😳 aku pun rindu mu jugak.")

    if st.session_state.no_count and st.session_state.q_idx == 0:
        no = st.session_state.no_count
        if no == 1:
            st.warning("Yeke? Tak percaya... cuba jujur sikit lagi 🤨")
        elif no == 2:
            st.warning("Hmm. Aku tunggu sampai mu tekan Yes...")
        else:
            st.warning("Weh... tekan YES laaa. Aku malu ni 🥺")
