import streamlit as st
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials, storage
import io
st.set_page_config(layout="wide")
with open("cred.txt","r") as file:
        userid = file.readline()
ref = db.reference("/posts")
ref1 = db.reference("/users")
st.markdown(
    f"""
    <div style="display: flex; align-items: center; padding: 20px; background: linear-gradient(to right, #87CEFA, #ffffff); 
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); border-radius: 8px;">
        <div style="text-align: left;">
            <p style="font-size: 50px; color: black;">{ref1.child(userid).child("name").get().upper()}</p>
            <p style="font-size: 20px; color: black;">{"@" + ref1.child(userid).child("user_name").get().upper()}</p>
            <p style="font-size: 12px; color: black;">{"#" + userid.upper()}</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("<br>",unsafe_allow_html=True)
st.subheader("Contributions: ")
st.markdown("<hr>",unsafe_allow_html=True)


datas = ref.get().keys()
datasl = list(datas)

for i in datasl:
    post_user_id = ref.child(i).child("userid").get()
    if(post_user_id==userid):
        #user's contribution
        with st.chat_message("human"):
            st.subheader(ref.child(i).child("title").get())
            st.write(ref.child(i).child("content").get()[0:300]+"...")
            st.caption("Uploaded On: " + ref.child(i).child("time").get())
            st.write("Total Likes: " + str(ref.child(i).child("likes").get()))


with open("cred.txt","r") as file:
    uid = file.readline()
