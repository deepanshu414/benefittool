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
    """
):
    st.markdown("""<style>body{text-align:center;}</style>""",True)
def login():
    st.markdown("<h1>Login</h1><br><br>", unsafe_allow_html=True)
    user_name = st.text_input("Enter user name")
    user_password = st.text_input("Enter password", type="password")
    submit = st.button("Submit")
    if submit:
        if user_name == "" or user_password == "":
            st.warning("Fill all fields")
        else:
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
                    with open("newuserdata.txt", 'w') as file:
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
    u=st.session_state.user_name
    v=st.session_state.user_password
    di={"deepanshu":"divyanshantil17","paras":"parasmutreja16","vivek":"vivekantil15","mukul":"mukulkaushik14","aanchal":"aanchaljha13"}
    za=0
    for key, value in di.items():
        if(u.lower()==key and  v.lower() == value):
            za+=1
            break
    if(za!=0):
        value=st.sidebar.radio("Navigation",["Home","Upload_other_things","Zip_file_uploader","Show_zip_file","Add_question","Show question","Add answer","Show answer","Code store","Code","Image","CJ_image","SMM_image","DCN_image","RDBMS_image","ML_image","PL_image","SE_image","Video","Mp3","Pdf","Excel_data","Text file","Csv","Message","Map","Remove_background","Image_Convertor_Pdf"],index=0 )
    else:
        value=st.sidebar.radio("Navigation",["Remove_background","Image_Convertor_Pdf"])
    if(value=="Home"):
        st.title("Upload Data")
        na=st.selectbox("Subject name",["Select name","CJ","SMM","DCN","RDBMS","ML","PL","SE"],index=0)
        uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])
        button = st.button("Submit")
        if(button == True):
            if na!="Select name" and uploaded_file is not None:
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
            else:
                st.warning("Fill all fields ...")
    elif(value=="Upload_other_things"):
        st.markdown("<h1 style='text-align:center;'>Upload</h1><br>", True)
        uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "pdf", "txt", "csv", "xlsx", "jpeg", "xls", "mp4", "wav", "mp3", "avi", "mov"])
        if uploaded_file is not None:
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
    elif(value=="Zip_file_uploader"):
        st.markdown("<h1 style='text-align:center;'>Store zip files</h1><br>", True)
        zip_file_upload = st.file_uploader("", type=["zip"])
        button = st.button("Submit")
        folder = "ant\zip_folder"
        if button:
            if zip_file_upload is not None:
                try:
                    zip_content=zip_file_upload.getvalue()
                    zip_path = os.path.join(folder, zip_file_upload.name)
                    with open(zip_path, "wb") as f:
                        f.write(zip_content)
                    st.success("Successfully uploaded ")
                except Exception as e:
                    st.error(e)
            else:
                st.warning("Fill all fields.")
    elif(value=="Show_zip_file"):
        st.markdown("<h1 style='text-align:center;'>Show all zip files</h1><br>", True)
        folder="ant\zip_folder"
        a=1
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                st.markdown(f"<h6 style='text-align:center;'>{a} files</h6><br>", True)
                if(filename!="ashdkiowersdnm,c23434df38rakl_q842wer3rkajew38rqw2338.txt"):
                    url = os.path.join(folder, filename)
                    with open(url, "rb") as f:
                        zip_content = f.read()
                    st.download_button(label="Download :- "+str(filename), data=zip_content, file_name=filename, mime="application/zip")
                    st.caption("File name: " + filename)
                    a += 1
    elif(value=="Add_question"):
        na=st.text_input("Name",placeholder="Enter your name")
        la=st.selectbox("Select Language",["C","C++","Python","SQL","Java","Php","Html","CSS","Javascript","Html + Css","Html + Css + Javascript","Html +Javascript","Ruby","Swift","Go","Rust","Typing script","Kotlin","Perl","R","Matlab","Assembly Languages","DSA","DA","Networking","RDBMS"])
        qu=st.text_area("Question",placeholder="Enter a question")
        bt=st.button("Submit")
        if(bt==True):
            if(na!="" and la!=""and qu!=""):
                folder="ant/question.txt"
                with open(folder,'r') as file:
                    te=file.read()
                    if(te!=""):
                        with open(folder,'a') as file:
                            file.write("\n"+na+" : "+la +" : " +qu)
                    else:
                        with open(folder,'w') as file:
                            file.write(na+" : "+la +" : " +qu)
                    st.success("Successfully submitted question")
            else:
                st.warning("Fill all fields")
    elif(value=="Show question"):
        st.markdown("<h1 style='text-align:center;'>Show all questions</h1><br>", True)
        folder="ant/question.txt"
        a=1
        with open(folder, "r") as file:
            text = file.read()
            lines = text.splitlines()
            if(text != ""):
                for line in lines:
                    st.markdown(f"<h3 style='text-align:center;'>{a} Question</h3><br>", True)
                    ana=line.split(":")[0].strip()
                    ala=line.split(":")[1].strip()
                    aqu=line.split(":")[2].strip()
                    st.markdown(f"<h2 style='text-align:center;color:blue;'>{ala}</h2>",True)
                    st.markdown(f"<h5 style='text-align:center;color:red;'>{aqu}</h5>",True)
                    a+=1
                    st.caption(ana)
    elif(value=="Add answer"):
        na=st.text_input("Name",placeholder="Enter your name")
        la=st.selectbox("Select Language",["C","C++","Python","SQL","Java","Php","Html","CSS","Javascript","Html + Css","Html + Css + Javascript","Html +Javascript","Ruby","Swift","Go","Rust","Typing script","Kotlin","Perl","R","Matlab","Assembly Languages","DSA","DA","Networking","RDBMS"])
        qu=st.text_area("Question",placeholder="Enter a question",key="que")
        ans=st.text_area("Answer",placeholder="Enter your answer",key="answ")
        bt=st.button("Submit")
        text_list = ans.split('\n')
        li='__.--.--.__'.join(text_list)
        if(bt==True):
            if(na!="" and la!=""and qu!="" and ans!=""):
                folder="ant/answer.txt"
                with open(folder,'r') as file:
                    te=file.read()
                    if(te!=""):
                        with open(folder,'a') as file:
                            file.write("\n"+na+" : "+la +" : " +qu + " : "+li)
                    else:
                        with open(folder,'w') as file:
                            file.write(na+" : "+la +" : " +qu + " : "+li)
                st.success("Successfully submitted answer")
            else:
                st.warning("Fill all fields")
    elif(value=="Show answer"):
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
                    ana=line.split(":")[0].strip()
                    ala=line.split(":")[1].strip()
                    aqu=line.split(":")[2].strip()
                    aans=line.split(":")[3].strip()
                    rlk=aans.split('__.--.--.__')
                    ex=st.expander("Language ("+ala+") Qustion  :- "+ aqu)
                    stri=""
                    for i in range(len(rlk)):
                        stri=stri+rlk[i]+"\n"
                    ex.code(stri)
                    a+=1
                    st.caption(ana)
    elif(value=="Code store"):
        st.markdown("<h1 style='text-align:center;'>Code</h1><br>", True)
        l_n=st.selectbox("Code name",["python","javascript","html","css","java","cpp","json","yaml","sql","markdown","hash","r","bash","php","ruby","swift","typescript","xml","rust","go","perl","scala","kotlin"])
        l_s=st.text_area("Code")
        btn=st.button("Submit")
        text_list = l_s.split('\n')
        li='__.--.--.__'.join(text_list)
        folder="ant/code.txt"
        if( btn ==True):
            if(l_n!="" and l_s!=""):
                with open(folder,'r') as file:
                    rea=file.read() 
                if(rea !=""):
                    with open(folder,'a') as file:
                        file.write("\n"+l_n+" : "+li)
                    st.success("Submitted successfully")
                else:
                    with open(folder,'w') as file:
                        file.write(l_n+" : "+li)
                    st.success("Submitted successfully")
            else:
                st.warning("Fill all fields")
    elif(value=="Code"):
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
                link_name=line.split(":")[0].strip()
                link=line.split(":")[1].strip()
                r_l=link.split('__.--.--.__')
                ex=st.expander(link_name)
                stk=""
                for i in range(len(r_l)):
                    stk=stk+r_l[i]+"\n"
                aq=ex.code(stk,language=link_name)
                a+=1
    elif(value=="CJ_image"):
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
    elif(value=="SMM_image"):
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
    elif(value=="DCN_image"):
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
    elif(value=="RDBMS_image"):
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
    elif(value=="ML_image"):
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
    elif(value=="PL_image"):
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
    elif(value=="SE_image"):
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
    elif(value=="Image"):
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
    elif(value == "Csv"):
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
    elif(value =="Excel_data"):
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
    elif(value =="Text file"):
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
    elif value == "Pdf":
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
    elif(value=="Mp3"):
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
    elif(value=="Video"):
        st.markdown("<h1 style='text-align:center;'>Mp3</h1><br>", True)
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
    elif(value=="Message"):
        st.markdown("<h1 style='text-align:center;'>Messages</h1><br>", True)
        folder="ant/message.txt"
        l=0
        with open(folder, "r") as file:
            text = file.read()
            lines = text.splitlines()
            if(text != ""):
                for line in lines:
                    l+=1
                    if(line.startswith(u.lower())):
                        az=line.split(":")[1].strip()
                        st.markdown(f"<h6 style='text-align:right;color:green;'>{az}</h6>",True)
                    else:
                        st.markdown(f"<h6 style='text-align:left;color:black;'>{line.capitalize()}</h6>",True)
        mg = st.chat_input("Enter Message ... ")
        if mg and mg.strip():  
            with open(folder, "a") as file:
                text = "\n" + u.lower() + " : " + mg
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
                        if(line.startswith(u.lower())):
                            az=last_line.split(":")[1].strip()
                            st.markdown(f"<h6 style='text-align:right;color:green;'>{az}</h6>",True)
                        else:
                            st.markdown(f"<h6 style='text-align:left;color:black;'>{line.capitalize()}</h6>",True)
                l+=1
            time.sleep(1)
    elif(value=="Map"):
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
    elif(value=="Remove_background"):
        st.title("Remove Background")
        input_file = st.file_uploader("",["jpg","png","jpg","bmp","jpeg","gif","svg","tga","tiff","WebP"])
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
    elif(value=="Image_Convertor_Pdf"):
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
        uploaded_files = st.file_uploader("", type=["jpg", "png"], accept_multiple_files=True)
        name=st.text_input("",placeholder="Enter pdf name ...")
        if st.button("Convert") :
            if(uploaded_files!="" and name!=""):
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
            else:
                st.warning("Fill all fields...")
            

def main():
    if not st.session_state.get("logged_in"):
        login()
    else:
        personal_data()

if __name__ == "__main__":
    main()
