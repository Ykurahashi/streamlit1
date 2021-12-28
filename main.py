import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit入門")

st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range (100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.2)

'Done!!'

option = st.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1,11))
)
'あなたの好きな数字は', option,'です'

left_column, right_column = st.beta_columns(2)
button = left_column.button("右カラムに文字を入れる")
if button:
    right_column.write("ここが右カラム")

expander = st.beta_expander("問い合わせ")
expander.write("問い合わせ")

st.sidebar.write("Interactive Weights")
text = st.sidebar.text_input("あなたの趣味を教えてください")
"あなたの趣味：", text

condition = st.sidebar.slider("あなたの調子を教えてください", 0, 100, 50)
"あなたの調子：", condition

st.write("Display image")
if st.checkbox("Show image"):
    img = Image.open("sample.png")
    st.image(img, caption ="ZTMY", use_column_width=True)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50,50] + [35.69,139.70],
    columns = ["lat", "lon"]
)

#st.table(df.style.highlight_max(axis=0))
#st.map(df)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""