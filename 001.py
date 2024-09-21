import streamlit as st
import pandas as pd
col1, col2, col3 = st.columns(3)
with col1:
    st.image("001.png")
with col2:
    st.write("Welcome to Result Portal of St.Joseph Global School (CBSE) - Polivakkam")
with col3:
    st.write("")
d = 0
c = ""
a = st.selectbox( "Select the class?", ("GRADE - 6", "GRADE - 7", "GRADE - 8", "GRADE - 9"),)
b = st.selectbox( "Select the Section?", ("SECTION - A", "SECTION - B" , "NO SECTION"),)
if (a == "GRADE - 6" and b == "SECTION - A"):
    c = "6A"
elif (a == "GRADE - 6" and b == "SECTION - B"):
    c = "6B"
elif (a == "GRADE - 7" and b == "SECTION - A"):
    c = "7A"
elif (a == "GRADE - 7" and b == "SECTION - B"):
    c = "7B"
elif (a == "GRADE - 8" and b == "SECTION - A"):
    c = "8A"
elif (a == "GRADE - 8" and b == "SECTION - B"):
    c = "8B"
elif (a == "GRADE - 9" and b == "NO SECTION"):
    c = "9"
else:
    d = 1
f = ".xlsx"
e = "Here is the Result of " + c
if st.button("Submit"):

    if d == 1:
        st.warning("Please Select a Valid Class")
    else:
        dataframe1 = pd.read_excel(c + f)
        st.write(e)
        st.write(dataframe1)
        with open(c+f, "rb") as template_file:
            template_byte = template_file.read()
            st.download_button(label="Click to Download File as Excel",
                        data=template_byte,
                         file_name=c+f,
                         mime='application/octet-stream')
            st.download_button(label="Click to Download File as PDF",
                           data=template_byte,
                           file_name=c+".pdf",
                           mime='application/octet-stream')
