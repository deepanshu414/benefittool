import streamlit as st
from PIL import Image
from rembg import remove as rm 
from streamlit_extras.stylable_container import stylable_container
import pandas as pd
import os
import time
from PyPDF2 import PdfReader
st.set_page_config(page_title="Personal" ,page_icon="https://static.vecteezy.com/system/resources/previews/016/774/644/non_2x/3d-user-icon-on-transparent-background-free-png.png")
hide="""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}
</style>
"""
st.markdown(hide,unsafe_allow_html=True)
with stylable_container(
    key="ab",
    css_styles="""
    div[data-testid="stImage"] > img{
        border-radius:100px;
        display: inline-block;
        position: sticky;
        margin:0;
        padding:0;
    }
    [data-testid="stStyledFullScreenFrame"]{
        margin:0px;
        padding:0px;
    }
    [data-testid="StyledFullScreenButton"]{
        display: none;
        pointer-events: none;
    }
    [class="st-emotion-cache-eczf16 e1nzilvr3"]{
        display: none;
        color:none;
        pointer-events: none;
    }
    [data-testid="baseButton-secondary"]{
        background-color:white;
        outline-style:solid;
        color:blue;
        transition:0.5s ease-in-out;
    }
    .block-container.st-emotion-cache-1y4p8pa.ea3mdgi2 {
        margin: 0px;
        padding: 0px;
    }
    .st-emotion-cache-1li7dat.e1y5xkzn1 {
        display: none;
    }
    svg.st-c3.st-c4.st-c5.st-c6.st-c7 {
        fill: crimson;
    }
    textarea.st-ae.st-bc.st-bd.st-be.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-ah.st-bm.st-bn.st-bo.st-bp.st-eg.st-eh.st-ei.st-ej.st-ax.st-ay.st-az.st-bu.st-b1.st-b2.st-bb.st-bv.st-ek.st-el.st-e0.st-en {
        font-family: sans-serif;
    }
    span.st-emotion-cache-10trblm.e1nzilvr1 {
        font-family: math;
    }
    span.st-emotion-cache-10trblm.e1nzilvr1 {
        text-shadow: 1px 10px 20px gray;
    }
    textarea.st-ae.st-bc.st-bd.st-be.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-ah.st-bm.st-bn.st-bo.st-bp.st-eg.st-eh.st-ei.st-ej.st-ax.st-ay.st-az.st-bu.st-b1.st-b2.st-bb.st-bv.st-ek.st-el.st-e0.st-en {
        margin-left: 20px;
    }
    label.st-ci.st-af.st-cj.st-cf.st-ck.st-cl.st-cm.st-cn.st-co.st-cp.st-cq.st-cr.st-cs.st-ct:hover {
        transform: scale(1.2);
    }
    p {
    font-weight: unset;
    }
    p {
        font-family: system-ui;
        text-shadow: 1px 1px 1px white;
    }
    label.st-ci.st-af.st-cj.st-cf.st-ck.st-cl.st-cm.st-cn.st-co.st-cp.st-cq.st-cr.st-cs.st-ct {
        margin-bottom: 10px;
    }
    .st-emotion-cache-16idsys.e1nzilvr5 {
        box-shadow: 2px 1px 2px black;
        margin: 0 0px 10px 0px;
        padding: 10px;
        font-weight: bold;
    }
    span.st-emotion-cache-10trblm.e1nzilvr1 {
        font-family: inherit;
        text-transform: capitalize;
    }
    section.st-emotion-cache-1gulkj5.e1b2p2ww15 {
        box-shadow: 2px 1px 2px;
    }
    button.st-emotion-cache-7ym5gk.ef3psqc12 {
        text-shadow: 2px 3px 10px gray;
    }
    .st-emotion-cache-16idsys.e1nzilvr5 {
        border-radius: 10px;
    }
    span.st-emotion-cache-9ycgxx.e1b2p2ww12 {
        font-family: cursive;
        font-weight: bold;
        text-shadow: 2px 2px 20px gray;
    }
    small.st-emotion-cache-1aehpvj.e1bju1570 {
        font-family: monospace;
        font-weight: bold;
        text-shadow: 2px 5px 15px gray;
    }
    span.st-emotion-cache-10trblm.e1nzilvr1 {
        text-shadow: 2px 7px 5px darkgoldenrod;
    }
    button.st-emotion-cache-7ym5gk.ef3psqc12 {
        margin-bottom: 10px;
    }
    .st-emotion-cache-16idsys.e1nzilvr5 {
        color: cadetblue;
    }
    section.main.st-emotion-cache-uf99v8.ea3mdgi3 {
        margin-bottom: 120px;
    }
    input.st-ae.st-bc.st-bd.st-be.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-ah.st-bm.st-bn.st-bo.st-bp.st-bq.st-br.st-bs.st-bt.st-ax.st-ay.st-az.st-bu.st-b1.st-b2.st-bb.st-bv.st-bw.st-bx {
        color: steelblue;
        font-family: cursive;
        margin-left:15px;
    }
    .st-af.st-ah.st-ba.st-ar.st-as.st-ax.st-ay.st-az.st-b0.st-b1.st-b2.st-bb.st-b7 {
        background: ghostwhite;
    }
    .st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-al.st-am.st-an.st-ao.st-ap.st-aq.st-ar.st-as.st-at.st-au.st-av.st-aw.st-ax.st-ay.st-az.st-b0.st-b1.st-b2.st-b3.st-b4.st-b5.st-b6.st-b7.st-b8.st-by {
        background: ghostwhite;
        box-shadow: 0 1px 2px black;
    }
    .st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-al.st-am.st-an.st-ao.st-ap.st-aq.st-ar.st-as.st-at.st-au.st-av.st-aw.st-ax.st-ay.st-az.st-b0.st-b1.st-b2.st-b3.st-b4.st-b5.st-b6.st-b7.st-b8.st-b9 {
        box-shadow: 0 1px 2px black;
    }
    .st-ax.st-ay.st-az.st-bu.st-b1.st-b2.st-ae.st-dj.st-ah {
        font-family: cursive;
        box-shadow: 0px 1px 2px black;
        background: ghostwhite;
    }
    .st-ae.st-af.st-ag.st-ah.st-ef.st-eg.st-eh.st-ei.st-am.st-an.st-ao.st-ap.st-aq.st-ar.st-as.st-at.st-au.st-av.st-aw.st-b3.st-b4.st-b5.st-b6.st-b7.st-b8.st-b9 {
        box-shadow: 0px 1px 2px black;
    }
    textarea.st-ae.st-bc.st-bd.st-be.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-ah.st-bm.st-bn.st-bo.st-bp.st-ej.st-ek.st-el.st-em.st-ax.st-ay.st-az.st-bu.st-b1.st-b2.st-bb.st-bv.st-bw.st-bx.st-en.st-eo.st-ep {
        font-family: cursive;
    }
    .st-emotion-cache-16idsys.e1nzilvr5 {
        box-shadow: 0px 1px 2px black;
    }
    span.st-emotion-cache-10trblm.e1nzilvr1 {
        text-shadow: 0px 1px 5px cadetblue;
        color: cadetblue;
    }
    span.st-emotion-cache-nwtri.e1b2p2ww13 {
        filter: drop-shadow(0px 1px 0px black);
    }
    button.st-emotion-cache-7ym5gk.ef3psqc12 {
        text-shadow: 0px 1px 1px cadetblue;
        color: cadetblue;
    }
    button.st-emotion-cache-7ym5gk.ef3psqc12:hover{
        color:black;
        outline:none;
        border:2px solid black;
        background-image: white;
    }
    button.st-emotion-cache-7ym5gk.ef3psqc12:active{
        color:black;
        outline:none;
        border:2px solid black;
        text-shadow: 0px 1px 1px black;
        animation:s 2s ;
        background-image: linear-gradient(180deg, lightgreen, skyblue);
    }
    button.st-af.st-bz.st-bj.st-bk.st-bh.st-bi.st-c0.st-c1.st-c2.st-bl.st-bb {
        border: none;
        outline: none;
    }
    .stCodeBlock.st-emotion-cache-12r09dv.e1ycw9pz1 {
        box-shadow: 0px 0px 2px black;
    }
    .st-emotion-cache-0.eqpbllx5 {
        box-shadow: 0px 0px 1px black;
    }
    label.st-emotion-cache-ue6h4q.e1y5xkzn3 {
        margin-left: 10px;
    }
    section.st-emotion-cache-1gulkj5.e1b2p2ww15 {
        margin-left: 10px;
        margin-right: 10px;
    }
    .st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-al.st-am.st-an.st-ao.st-ap.st-aq.st-ar.st-as.st-at.st-au.st-av.st-aw.st-ax.st-ay.st-az.st-b0.st-b1.st-b2.st-b3.st-b4.st-b5.st-b6.st-b7.st-b8.st-b9 {
        margin-left: 10px;
        margin-right: 10px;
        width: 98%;
    }
    .st-emotion-cache-1om1ktf.ezh4s2r0 {
        margin-left: 10px;
        margin-right: 10px;
    }
    .st-emotion-cache-0.eqpbllx5 {
        margin-left: 10px;
        margin-right: 10px;
    }
    .st-ax.st-ay.st-az.st-bu.st-b1.st-b2.st-ae.st-dj.st-ah {
        margin-left: 10px;
        margin-right: 10px;
        width: 98%;
    }
    .st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-al.st-am.st-an.st-ao.st-ap.st-aq.st-ar.st-as.st-at.st-au.st-av.st-aw.st-ax.st-ay.st-az.st-b0.st-b1.st-b2.st-b3.st-b4.st-b5.st-b6.st-b7.st-b8.st-by {
        margin-left: 10px;
        margin-right: 10px;
        width: 98%;
    }
    .st-emotion-cache-11lmpti.e1f1d6gn2 {
        overflow: auto;
    }
    .uploadedFileName.st-emotion-cache-1uixxvy.e1b2p2ww6 {
        text-shadow: 0px 0px 1px black;
    }
    section.main.st-emotion-cache-uf99v8.ea3mdgi3 {
        overflow: auto;
    }
    """
):
    st.markdown("""<style>body{text-align:center;}</style>""",True)
def login():
    st.markdown("<h1>Login</h1><br><br>", unsafe_allow_html=True)
    user_name = st.text_input("Enter user name")
    user_password = st.text_input("Enter password", type="password")
    if user_name != "" and user_password != "":
        submit = st.button("Submit")
        if submit:
            pairs = {user_name:user_password}
            record_exists = False
            with open("userdata.txt", 'r') as file:
                for line in file:
                    key, value = line.strip().split(':')
                    if user_name.lower()==key and user_password.lower()==value:
                        record_exists = True
                        break
            if not record_exists:
                record_check = False
                with open("newuserdata.txt", 'r') as file:
                    for line in file:
                        key, value = line.strip().split(':')
                        if user_name.lower()==key and user_password.lower()==value:
                            record_check = True
                            break
                if not record_check:
                    with open("newuserdata.txt", 'a') as file:
                        for key, value in pairs.items():
                            file.write(f"{key}:{value}\n")
            st.session_state.logged_in = True
            st.session_state.user_name = user_name
            st.session_state.user_password = user_password
            st.experimental_rerun()
def display_zip_files(directory):
    zip_files = [f for f in os.listdir(directory) if f.endswith('.zip')]
    return zip_files
def personal_data():
    def home():
        st.title("Upload Data")
        na=st.selectbox("Subject name",["Select name","CJ","SMM","DCN","RDBMS","ML","PL","SE"],index=0)
        uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])
        if na!="Select name" and uploaded_file is not None:
            button = st.button("Submit")
            if (button == True):
                if uploaded_file is not None:
                    file_extension = uploaded_file.name.split(".")[-1].lower()
                    if file_extension in ["jpg", "jpeg", "png", "gif"]:
                        if(na == "CJ"):
                            folder="ant/CJ_image"
                            with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                                    f.write(uploaded_file.getbuffer())
                        elif(na=="SMM"):
                            folder="ant/SMM_image"
                            with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                                    f.write(uploaded_file.getbuffer())
                        elif(na=="DCN"):
                            folder="ant/DNC_image"
                            with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                                    f.write(uploaded_file.getbuffer())
                        elif(na=="RDBMS"):
                            folder="ant/RDBMS_image"
                            with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                                    f.write(uploaded_file.getbuffer())
                        elif(na=="ML"):
                            folder="ant/ML_image"
                            with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                                    f.write(uploaded_file.getbuffer())
                        elif(na=="PL"):
                            folder="ant/PL_image"
                            with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                                    f.write(uploaded_file.getbuffer())
                        elif(na=="SE"):
                            folder="ant/SE_image"
                            with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                                    f.write(uploaded_file.getbuffer())
                    elif file_extension == "pdf":
                        folder="ant/pdf"
                        with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                                f.write(uploaded_file.getbuffer())
                    elif file_extension == "txt":
                        folder="ant/text"
                        with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                                f.write(uploaded_file.getbuffer())
                    elif file_extension in ["xlsx", "xls"]:
                        folder="ant/excel"
                        with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                                f.write(uploaded_file.getbuffer())
                    elif file_extension == "csv":
                        folder="ant/csv"
                        with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                                f.write(uploaded_file.getbuffer())
                    elif file_extension in ["mp4","avi","mov"]:
                        folder="ant/mp4f"
                        with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                                f.write(uploaded_file.getbuffer())
                    elif file_extension in ["mp3","wav"]:
                        folder="ant/mp3f"
                        with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                                f.write(uploaded_file.getbuffer())
                    st.success("Successfully uploaded")
                else:
                    st.error("File not be considered uploaded")
    def upload():
        st.markdown("<h1 style='text-align:center;'>Upload</h1><br>", True)
        uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "pdf", "txt", "csv", "xlsx", "jpeg", "xls", "mp4", "wav", "mp3", "avi", "mov"])
        if uploaded_file is not None:
            button = st.button("Submit")
            if button:
                file_extension = uploaded_file.name.split(".")[-1].lower()
                if file_extension in ["jpg", "jpeg", "png", "gif"]:
                    folder="ant/image"
                    with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                            f.write(uploaded_file.getbuffer())
                elif file_extension == "pdf":
                    folder="ant/pdf"
                    with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                            f.write(uploaded_file.getbuffer())
                elif file_extension == "txt":
                    folder="ant/text"
                    with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                            f.write(uploaded_file.getbuffer())
                elif file_extension in ["xlsx", "xls"]:
                    folder="ant/excel"
                    name_excel=uploaded_file.name.strip().split('.')[0]
                    text_file = str(name_excel)+".txt"
                    with open(os.path.join(folder, text_file), "wb") as f:
                            df = pd.read_excel(uploaded_file)
                            df.to_csv(f, index=False)
                elif file_extension == "csv":
                    folder="ant/csv"
                    name_excel=uploaded_file.name.strip().split('.')[0]
                    text_file = str(name_excel)+".txt"
                    with open(os.path.join(folder, text_file), "wb") as f:
                            df = pd.read_excel(uploaded_file)
                            df.to_csv(f, index=False)
                elif file_extension in ["mp4","avi","mov"]:
                    folder="ant/mp4f"
                    with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                            f.write(uploaded_file.getbuffer())
                elif file_extension in ["mp3","wav"]:
                    folder="ant/mp3f"
                    with open(os.path.join(folder, uploaded_file.name), "wb") as f:
                            f.write(uploaded_file.getbuffer())
                st.success("Successfully uploaded")
    def zip_upload():
        st.markdown("<h1 style='text-align:center;'>Store zip files</h1><br>", True)
        zip_file_upload = st.file_uploader("Zip files", type=["zip"])
        folder = "ant\zip_folder"
        if zip_file_upload is not None:
            button = st.button("Submit")
            if button:
                try:
                    zip_content=zip_file_upload.getvalue()
                    zip_path = os.path.join(folder, zip_file_upload.name)
                    with open(zip_path, "wb") as f:
                        f.write(zip_content)
                    st.success("Successfully uploaded ")
                except Exception as e:
                    st.error(e)
    def show_zip():
        st.markdown("<h1 style='text-align:center;'>Show all zip files</h1><br>", True)
        folder="ant\zip_folder"
        a=1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                    url = os.path.join(folder, filename)
                    with open(url, "rb") as f:
                        zip_content = f.read()
                    st.download_button(label="Download :- "+str(filename), data=zip_content, file_name=filename, mime="application/zip")
                    st.caption("File name: " + filename)
                    a += 1
    def add_question():
        st.markdown("<h1 style='text-align:center;'>Add Questions</h1><br>", True)
        na=st.text_input("Name",placeholder="Enter your name")
        la=st.selectbox("Select Language",["Python","Javascript","Html","Css","Java","Cpp","Json","Yaml","Sql","Markdown","Hash","R","Bash","Php","Ruby","Swift","Typescript","Xml","Rust","Go","Perl","Scala","Kotlin"])
        qu=st.text_area("Question",placeholder="Enter a question")
        text_list = qu.split('\n')
        li='__.--.--.__'.join(text_list)
        if (na!="" and la!=""and qu!=""):
            bt=st.button("Submit")
            if (bt==True):
                folder="ant/question.txt"
                with open(folder,'r') as file:
                    te=file.read()
                    if(te!=""):
                        with open(folder,'a') as file:
                            file.write("\n"+na+" :-:-:-: "+la +" :-:-:-: " +li)
                    else:
                        with open(folder,'w') as file:
                            file.write(na+" :-:-:-: "+la +" :-:-:-: " +li)
                    st.success("Successfully submitted question")
    def show_question():
        st.markdown("<h1 style='text-align:center;'>Show all questions</h1><br>", True)
        folder="ant/question.txt"
        a=1
        with open(folder, "r") as file:
            text = file.read()
            lines = text.splitlines()
            if(text != ""):
                for line in lines:
                    st.markdown(f"<h3 style='text-align:center;'>{a} Question</h3><br>", True)
                    ana=line.split(":-:-:-:")[0].strip()
                    ala=line.split(":-:-:-:")[1].strip()
                    aqu=line.split(":-:-:-:")[2].strip()
                    rlk=aqu.split('__.--.--.__')
                    ex=st.expander("Language ("+ala+")")
                    stri=""
                    for i in range(len(rlk)):
                        stri=stri+rlk[i]+"\n"
                    ex.code("Question: - \n" +stri,language="C")
                    a+=1
                    st.caption(ana)
    def add_answer():
        st.markdown("<h1 style='text-align:center;'>Add Answers</h1><br>", True)
        na=st.text_input("Name",placeholder="Enter your name")
        la=st.selectbox("Select Language",["Python","Javascript","Html","Css","Java","Cpp","Json","Yaml","Sql","Markdown","Hash","R","Bash","Php","Ruby","Swift","Typescript","Xml","Rust","Go","Perl","Scala","Kotlin"])
        folder="ant/question.txt"
        m=[]
        with open(folder, "r") as file:
            text = file.read()
            lines = text.splitlines()
            if(text != ""):
                for line in lines:
                    ana=line.split(":-:-:-:")[0].strip()
                    ala=line.split(":-:-:-:")[1].strip()
                    aqu=line.split(":-:-:-:")[2].strip()
                    rlk=aqu.split('__.--.--.__')
                    if(la==ala):
                        stri=""
                        for i in range(len(rlk)):
                            stri=stri+rlk[i]
                        m.append(stri)
                    else:
                        pass
                m.append("Other")
            else:
                m.append("Other")
        qu=st.selectbox("Question",m,index=None)
        if(qu=="Other"):
            qu=st.text_area("Other Question",placeholder="Enter a question",key="que")
        ans=st.text_area("Answer",placeholder="Enter your answer",key="answ")
        text_list = ans.split('\n')
        li='__.--.--.__'.join(text_list)
        if(na!="" and la!=""and qu!="" and ans!=""):
            bt=st.button("Submit")
            if (bt==True):
                folder="ant/answer.txt"
                with open(folder,'r') as file:
                    te=file.read()
                    if(te!=""):
                        with open(folder,'a') as file:
                            file.write("\n"+na+" :-:-:-: "+la.lower() +" :-:-:-: " +qu + " :-:-:-: "+li)
                    else:
                        with open(folder,'w') as file:
                            file.write(na+" :-:-:-: "+la.lower() +" :-:-:-: " +qu + " :-:-:-: "+li)
                st.success("Successfully submitted answer")
    def show_answer():
        with stylable_container(
            key="ab",
            css_styles="""
                [data-testid="stExpanderDetails"]{
                    body{
                        text-align: left;
                        }
                }
                [data-testid="stExpanderDetails" ]{
                    text-align:left;
                }
        
        """
        ):
            st.markdown("<h1 style='text-align:center;'>Show all answers</h1><br>", True)
        folder="ant/answer.txt"
        a=1
        with open(folder, "r") as file:
            text = file.read()
            lines = text.splitlines()
            if(text != ""):
                for line in lines:
                    st.markdown(f"<h3 style='text-align:center;'>{a} Question</h3><br>", True)
                    ana=line.split(":-:-:-:")[0].strip()
                    ala=line.split(":-:-:-:")[1].strip()
                    aqu=line.split(":-:-:-:")[2].strip()
                    aans=line.split(":-:-:-:")[3].strip()
                    rlk=aans.split('__.--.--.__')
                    ex=st.expander("Language ("+ala+") Qustion  :- "+ aqu)
                    stri=""
                    for i in range(len(rlk)):
                        stri=stri+rlk[i]+"\n"
                    ex.code(stri,language=ala)
                    a+=1
                    st.caption(ana)
    def code_store():
        st.markdown("<h1 style='text-align:center;'>Code</h1><br>", True)
        l_n=st.selectbox("Code name",["Python","Javascript","Html","Css","Java","Cpp","Json","Yaml","Sql","Markdown","Hash","R","Bash","Php","Ruby","Swift","Typescript","Xml","Rust","Go","Perl","Scala","Kotlin"])
        l_s=st.text_area("Code")
        text_list = l_s.split('\n')
        li='__.--.--.__'.join(text_list)
        folder="ant/code.txt"
        if(l_n!="" and l_s!=""):
            btn=st.button("Submit")
            if ( btn ==True):
                with open(folder,'r') as file:
                    rea=file.read() 
                if(rea !=""):
                    with open(folder,'a') as file:
                        file.write("\n"+l_n.lower()+" :-:-:-: "+li)
                    st.success("Submitted successfully")
                else:
                    with open(folder,'w') as file:
                        file.write(l_n+" :-:-:-: "+li)
                    st.success("Submitted successfully")
    def show_code():
        with stylable_container(
            key="ab",
            css_styles="""
                [data-testid="stExpanderDetails"]{
                    body{
                        text-align: left;
                        }
                }
                [data-testid="stExpanderDetails" ]{
                    text-align:left;
                }
        
        """
        ):
            st.markdown("<h1 style='text-align:center;'>Show all Code</h1><br>", True)
        folder="ant/code.txt"
        a=1
        with open(folder, "r") as file:
            text = file.read()
            lines = text.splitlines()
            for line in lines:
                st.markdown(f"<h6 style='text-align:center;'>{a} code</h6><br>", True)
                link_name=line.split(":-:-:-:")[0].strip()
                link=line.split(":-:-:-:")[1].strip()
                r_l=link.split('__.--.--.__')
                ex=st.expander(link_name)
                stk=""
                for i in range(len(r_l)):
                    stk=stk+r_l[i]+"\n"
                aq=ex.code(stk,language=link_name)
                a+=1
    def cj_image():
        st.markdown("<h1 style='text-align:center;'>CJ Images</h1><br>", True)
        folder="ant/CJ_image"
        a=1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                    pat=os.path.join(folder, filename)
                    st.image(pat,caption="File name : " + filename, use_column_width=True)
                    a=a+1
    def smm_image():
        st.markdown("<h1 style='text-align:center;'>SMM Images</h1><br>", True)
        folder="ant/SMM_image"
        a=1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                    pat=os.path.join(folder, filename)
                    st.image(pat,caption="File name : " + filename, use_column_width=True)
                    a=a+1
    def dcn_image():
        st.markdown("<h1 style='text-align:center;'>DCN Images</h1><br>", True)
        folder="ant/DNC_image"
        a=1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                    pat=os.path.join(folder, filename)
                    st.image(pat,caption="File name : " + filename, use_column_width=True)
                    a=a+1
    def rdbms_image():
        st.markdown("<h1 style='text-align:center;'>RDBMS Images</h1><br>", True)
        folder="ant/RDBMS_image"
        a=1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                    pat=os.path.join(folder, filename)
                    st.image(pat,"File name : " + filename, use_column_width=True)
                    a=a+1
    def ml_image():
        st.markdown("<h1 style='text-align:center;'>ML Images</h1><br>", True)
        folder="ant/ML_image"
        a=1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                    pat=os.path.join(folder, filename)
                    st.image(pat,caption="File name : " + filename, use_column_width=True)
                    a=a+1
    def pl_image():
        st.markdown("<h1 style='text-align:center;'>PL Images</h1><br>", True)
        folder="ant/PL_image"
        a=1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                    pat=os.path.join(folder, filename)
                    st.image(pat,caption="File name : " + filename, use_column_width=True)
                    a=a+1
    def se_image():
        st.markdown("<h1 style='text-align:center;'>SE Images</h1><br>", True)
        folder="ant/SE_image"
        a=1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                    pat=os.path.join(folder, filename)
                    st.image(pat,caption="File name : " + filename, use_column_width=True)
                    a=a+1
    def simple_image():
        st.markdown("<h1 style='text-align:center;'>Images</h1><br>", True)
        folder="ant/image"
        a=1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                    pat=os.path.join(folder, filename)
                    st.image(pat,caption="File name : " + filename, use_column_width=True)
                    a=a+1
    def show_csv():
        st.markdown("<h1 style='text-align:center;'>Csv files</h1><br>", True)
        folder="ant/csv"
        a=1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                    df = pd.read_csv(os.path.join(folder, filename))
                    st.write(df) 
                    a=a+1
                    st.caption("File name : " + filename)
    def show_excel():
        st.markdown("<h1 style='text-align:center;'>Excel files</h1><br>", True)
        folder="ant/excel"
        a=1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                    df = pd.read_csv(os.path.join(folder, filename))
                    st.write(df) 
                    a=a+1
                    st.caption("File name : " + filename)
    def show_text_file():
        st.markdown("<h1 style='text-align:center;'>Text files</h1><br>", True)
        folder="ant/text"
        a=1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                    with open(os.path.join(folder, filename), "r") as file:
                        text = file.read()
                        st.write(text)
                    a=a+1
                    st.caption("File name : " + filename)
    def show_pdf():
        st.markdown("<h1 style='text-align:center;'>Pdf files</h1><br>", True)
        folder = "ant/pdf"
        a = 1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                    pdf_file = os.path.join(folder, filename)
                    try:
                        with open(pdf_file, "rb") as f:
                            pdf_reader = PdfReader(f)
                            if pdf_reader.is_encrypted:
                                pdf_reader.decrypt("")
                            num_pages = len(pdf_reader.pages)
                            st.write(f"Total Pages in PDF: {num_pages}")
                            for page_num in range(min(num_pages, 3)):
                                page = pdf_reader.pages[page_num]  
                                text = page.extract_text()
                                for line in text.splitlines():
                                    st.write(line)
                    except Exception as e:
                        st.error(f"Error reading PDF file: {e}")
                    a += 1
                    st.caption("File name : " + filename)
    def show_mp3():
        st.markdown("<h1 style='text-align:center;'>Mp3</h1><br>", True)
        folder="ant/mp3f"
        a=1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                    audio_file=os.path.join(folder, filename)
                    st.audio(audio_file, format='audio/mp3', start_time=0)
                    st.caption("File name : " + filename)
                    a=a+1 
    def show_mp4():
        st.markdown("<h1 style='text-align:center;'>Mp4</h1><br>", True)
        folder="ant/mp4f"
        a=1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                    video_file=os.path.join(folder, filename)
                    st.video(video_file, format='video/mp4')
                    st.caption("File name : " + filename)
                    a=a+1 
    def show_and_store_message():
        u=st.session_state.user_name
        v=st.session_state.user_password
        st.markdown("<h1 style='text-align:center;'>Messages</h1><br>", True)
        folder="ant/message.txt"
        l=0
        with open(folder, "r") as file:
            text = file.read()
            lines = text.splitlines()
            if(text != ""):
                for line in lines:
                    l+=1
                    az=line.split(":-:-:-:")[1].strip()
                    za=line.split(":-:-:-:")[0].strip()
                    if(line.startswith(u.lower())):
                        st.markdown(f"<h6 style='text-align:right;color:green;font-family: revert;margin-right:20px;'>{az}</h6>",True)
                    else:
                        st.markdown(f"<h6 style='text-align:left;'><span style='color:red;font-weight:bold;font-family: system-ui;margin-left:10px;'>{za.capitalize()}</span> : <span style='color:blue;font-family: cursive;'> {az}</span> </h6>",True)
        mg = st.chat_input("Enter Message ... ")
        if mg and mg.strip():  
            with open(folder,'r') as fil:
                t=fil.read()
            if(t!=""):
                with open(folder, "a") as file:
                    text = "\n" + u.lower() + " :-:-:-: " + mg
                    file.write(text)
            else:
                with open(folder, "a") as file:
                    text = u.lower() + " :-:-:-: " + mg
                    file.write(text)
        while True:
            k=0
            with open(folder, "r") as file:
                text = file.read()
                lines = text.splitlines()
                for line in lines:
                    k+=1
            if(l<k and l!=k):
                with open(folder, "r") as file:
                    text = file.read()
                    lines = text.splitlines()
                    if lines: 
                        last_line = lines[-1]
                        az=last_line.split(":-:-:-:")[1].strip()
                        za=line.split(":-:-:-:")[0].strip()
                        if(line.startswith(u.lower())):
                            st.markdown(f"<h6 style='text-align:right;color:green;font-family: revert;margin-right:20px;'>{az}</h6>",True)
                        else:
                            st.markdown(f"<h6 style='text-align:left;'><span style='color:red;font-weight:bold;font-family: system-ui;margin-left:10px;'>{za.capitalize()}</span> : <span style='color:blue;font-family: cursive;'> {az}</span> </h6>",True)
                l+=1
            time.sleep(1)
    def show_map():
        a=st.number_input("Latitude",placeholder="for ex:- 32.1323")
        b=st.number_input("Longitude",placeholder="for ex:- 112.345")
        def plot_location_on_map(a,b):
            data = pd.DataFrame({
                'latitude': [a],  
                'longitude': [b]  
            })
            st.map(data,zoom=5)
        if(a!="" and b!=""):
            plot_location_on_map(a,b)
    def remove_background_from_image():
        st.title("Remove Background")
        input_file = st.file_uploader("Select Image",["jpg","png","jpg","bmp","jpeg","gif","svg","tga","tiff","WebP"])
        if input_file is not None:
            with open("temp_file", "wb") as f:
                f.write(input_file.read())
            input_path = "temp_file"
            if st.button("Remove"):
                directory, filename = os.path.split(input_path)
                output_path=input_path.replace(directory,"results")
                with open (input_path,"rb") as i:
                    with open (output_path,"wb") as o:
                        original_image=i.read()
                        output=rm(original_image)
                        o.write(output) 
                        file_name = input_file.name
                        print(file_name)
                        st.image(output_path, caption=file_name, use_column_width=True)
                        file_extension =input_file.name.split(".")[-1].lower()
                        mime_type = f"image/{file_extension}"
                        st.download_button(label="Download",data=output,file_name=file_name,mime=mime_type)
    def image_convertor_pdf():
        def images_to_pdf(images, output_path):
            images[0].save(output_path, save_all=True, append_images=images[1:])
        def delete_files(folder_path):
            files = os.listdir(folder_path)
            if files:  
                for file in files:
                    file_path = os.path.join(folder_path, file)
                    os.remove(file_path)
                print("All files deleted successfully.")
            else:
                print("No files found in the folder.")
        st.title("Image to PDF Converter")
        uploaded_files = st.file_uploader("Select Image", type=["jpg", "png"], accept_multiple_files=True)
        name=st.text_input("PDF Name",placeholder="Enter pdf name ...")
        if (uploaded_files is not None and name!="") :
            if st.button("Convert"):
                images = []
                for uploaded_file in uploaded_files:
                    image = Image.open(uploaded_file)
                    image = image.convert('RGB')
                    image = image.resize((400, 400))
                    images.append(image)
                if images:
                    with open("temp_file", "wb") as f:
                        for uploaded_file in uploaded_files:
                            f.write(uploaded_file.read()) 
                    input_path = "temp"
                    os.makedirs(input_path, exist_ok=True) 
                    delete_files(input_path)
                    an=str(name)+".pdf"
                    jo=os.path.join(input_path ,an)
                    print(jo)
                    output_path = jo
                    images_to_pdf(images, output_path)
                    st.success("PDF file created successfull...")
                    with open(output_path, "rb") as f:
                        pdf_data = f.read()
                    st.download_button(label="Download PDF", data=pdf_data, file_name=an, mime="application/pdf")
    def check_nav():
        xza=0
        u=st.session_state.user_name
        v=st.session_state.user_password
        with open("userdata.txt","r") as file:
            file1=file.read()
            lines = file1.splitlines()
            store_username_and_password=u.lower().strip()+":"+v.lower().strip()
            for x in lines:
                if(x==store_username_and_password):
                    xza+=1
                    break
        return xza 
    za=check_nav()
    if(za!=0):
        value=st.sidebar.radio("Navigation",["Home","Upload_other_things","Zip_file_uploader","Show_zip_file","Add_question","Show question","Add answer","Show answer","Code store","Code","Image","CJ_image","SMM_image","DCN_image","RDBMS_image","ML_image","PL_image","SE_image","Video","Mp3","Pdf","Excel_data","Text file","Csv","Message","Map","RemoveBackground","ImageConvertorPdf"],index=0 )
    else:
        value=st.sidebar.radio("Navigation",["RemoveBackground","ImageConvertorPdf"])
    if(value=="Home"):
        home()
    elif(value=="Upload_other_things"):
        upload()
    elif(value=="Zip_file_uploader"):
        zip_upload()
    elif(value=="Show_zip_file"):
        show_zip()
    elif(value=="Add_question"):
        add_question()
    elif(value=="Show question"):
        show_question()
    elif(value=="Add answer"):
        add_answer()
    elif(value=="Show answer"):
        show_answer()
    elif(value=="Code store"):
        code_store()
    elif(value=="Code"):
        show_code()
    elif(value=="CJ_image"):
        cj_image()
    elif(value=="SMM_image"):
        smm_image()
    elif(value=="DCN_image"):
        dcn_image()
    elif(value=="RDBMS_image"):
        rdbms_image()
    elif(value=="ML_image"):
        ml_image()
    elif(value=="PL_image"):
        pl_image()
    elif(value=="SE_image"):
        se_image()
    elif(value=="Image"):
        simple_image()
    elif(value == "Csv"):
        show_csv()
    elif(value =="Excel_data"):
        show_excel()
    elif(value =="Text file"):
        show_text_file()
    elif value == "Pdf":
        show_pdf()
    elif(value=="Mp3"):
        show_mp3()
    elif(value=="Video"):
        show_mp4()
    elif(value=="Message"):
        show_and_store_message()
    elif(value=="Map"):
        show_map()
    elif(value=="RemoveBackground"):
        remove_background_from_image()
    elif(value=="ImageConvertorPdf"):
        image_convertor_pdf()
def main():
    if not st.session_state.get("logged_in"):
        login()
    else:
        personal_data()
if __name__ == "__main__":
    main()
