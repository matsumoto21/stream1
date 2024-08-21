import streamlit as st 
import numpy as np
import pandas as pd
import time  
from PIL import Image 


st.title("streamlit 超入門")
st.write("プログレスバーの表示")
"start!!"
latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text("Iteration"+str(i+1))
    bar.progress(i+1)
    time.sleep(0.1)


left_column,right_column=st.columns(2)
button=left_column.button("ここは右カラム")
if button:
    right_column.write("ここは右カラム")

expander1=st.expander("問い合わせ")
expander1.write("問い合わせ１の回答")
expander2=st.expander("問い合わせ")
expander2.write("問い合わせ１の回答")
expander3=st.expander("問い合わせ")
expander3.write("問い合わせ１の回答")
# text=st.sidebar.text_input("あなたの趣味を教えてください")
# "あなたの趣味は：",text
if st.checkbox("show image"):
    img=Image.open("戦車.jpg")
    st.image(img,caption="戦車",use_column_width=True)

##st.dataframe(df,width=100,height=200)

option=st.selectbox(
    "あなたが好きな数字を選んでください",
    list(range(1,11))
)
"あなたが好きな数字は",option,"です"

conditon=st.sidebar.slider("あなたの調子は",0,50,100)
"コンディション",conditon