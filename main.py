import streamlit as st
from PIL import Image
from langchain import PromptTemplate
from langchain.llms import OpenAI
from streamlit_extras.buy_me_a_coffee import button

API_KEY = st.secrets["OPENAI_API_KEY"]

template = """
    Below is a scientific abstract that has many inaccessible scientific terms.
    Your ultimate goal is to:
   
    Create a lay summary of this scientific research abstract by explaining:

    1) the introductory context of the abstract (usually towards the beginning of the abstract)

    2) the overall takeaway of the abstract (usually in the start of the results sentences)
    
    3) the implications for the future (usually towards the end of the abstract)

    Below is the scientific abstract, length of summary, and target audience (21 year old adult with normal education or five year old):
    LENGTH: {length}
    AUDIENCE: {audience}
    ABSTRACT: {abstract}
    
    YOUR {length} SUMMARY:
"""

prompt = PromptTemplate(
    input_variables=["length","audience","abstract"],
    template=template
)

def load_LLM():
    """logic for loading the chain you want here"""
    llm = OpenAI(temperature=.5, openai_api_key=API_KEY)
    return llm

llm = load_LLM()

st.set_page_config(page_title="Desciencify", page_icon=":robot:")

col1, col2 = st.columns(2)

with col1:
    # Streamlit app title
    st.markdown("<h1 style='text-align: center; color: black; font-size:35x;'>Understand science easily!</h1>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: black; font-size:28px;'>Desciencify is a fast, super accessible scientific translator. It lets you remove jargon, get to the point, and share the latest scientific findings with anyone.</h2>", unsafe_allow_html=True)

with col2:
    image = Image.open('desceinceify.jpg')

    st.image(image) 

st.write("##")

st.markdown("## Enter your abstract to convert:")

col3, col4 = st.columns(2)

with col3:
    option_summary_type = st.selectbox("Would you like a concise summary or extended summary?", ("Extended", "Concise"))

with col4:
    option_five_year_old = st.selectbox("Explain it like I'm 5?", ("Adult", "Five year old"))

def get_text():
    # Text input for the scientific abstract
    abstract = st.text_area(label="", placeholder="Your abstract...", key="abstract_input")
    return abstract

abstract_input = get_text()

st.markdown("### Your summarised, understandable abstract:")

if abstract_input:
    

    prompt_with_abstract = prompt.format(length=option_summary_type,audience=option_five_year_old,abstract=abstract_input)

    formatted_abstract = llm(prompt_with_abstract)

    st.write(formatted_abstract)

st.write("###")

st.write("###")

st.write("###")

st.write("###")

st.write("###")

st.write("###")

st.write("###")

st.write("###")

button(username="bensf", floating=True, width=221)

st.write("###")

st.write("###")

st.write("###")

st.write("###")

st.write("###")

st.write("###")

st.write("###")

st.write("###")

st.markdown("Powered by Langchain (www.langchain.com) and OpenAI (www.openai.com)")

