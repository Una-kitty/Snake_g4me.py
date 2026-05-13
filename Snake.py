import streamlit as st
import time, random

st.title("Snake")

if 's' not in st.session_state:
    st.session_state.update(s=[(7,7)], d=(1,0), f=(12,12), sc=0, o=False)

gs=15
def draw():
    h = f'<div style="display:grid;grid-template-columns:repeat({gs},30px);gap:3px;background:#111;padding:12px;border:4px solid #0f0">'
    for y in range(gs):
        for x in range(gs):
            c = "#1f1f1f"
            if (x,y) in st.session_state.s:
                c = "#00ff00" if st.session_state.s[0]==(x,y) else "#00cc00"
            elif (x,y) == st.session_state.f:
                c = "#ff0000"
            h += f'<div style="width:30px;height:30px;background:{c};border-radius:3px"></div>'
    return h+'</div>'

st.metric("Score", st.session_state.sc)
st.markdown(draw(), unsafe_allow_html=True)

c = st.columns(3)
if c[0].button("Left"): st.session_state.d = (-1,0) if st.session_state.d != (1,0) else st.session_state.d
if c[1].button("Up"): st.session_state.d = (0,-1) if st.session_state.d != (0,1) else st.session_state.d
if c[1].button("Down"): st.session_state.d = (0,1) if st.session_state.d != (0,-1) else st.session_state.d
if c[2].button("Right"): st.session_state.d = (1,0) if st.session_state.d != (-1,0) else st.session_state.d

if st.button("Restart"): st.session_state.clear(); st.rerun()

if not st.session_state.o:
    h = st.session_state.s[0]
    nh = (h[0]+st.session_state.d[0], h[1]+st.session_state.d[1])
    if nh[0]<0 or nh[0]>=gs or nh[1]<0 or nh[1]>=gs or nh in st.session_state.s:
        st.session_state.o = True
        st.error(f"GAME OVER! Score: {st.session_state.sc}")
    else:
        st.session_state.s.insert(0, nh)
        if nh == st.session_state.f: 
            st.session_state.sc += 10
            st.session_state.f = (random.randint(0,gs-1),random.randint(0,gs-1))
        else: 
            st.session_state.s.pop()
        time.sleep(0.15)
        st.rerun()
