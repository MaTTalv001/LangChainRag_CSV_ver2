import os
import streamlit as st
from langchain_community.document_loaders import CSVLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

# OpenAI APIキーの設定
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Chromaデータベースの設定
CHROMA_PERSIST_DIR = "/app/persistent_storage"

def load_and_embed_data():
    loader = CSVLoader(file_path="/app/data/data.csv")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(texts, embeddings, persist_directory=CHROMA_PERSIST_DIR)
    vectorstore.persist()
    st.success("データがエンベッディングされ、ベクトルデータベースが更新されました。")

def query_data(query):
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(persist_directory=CHROMA_PERSIST_DIR, embedding_function=embeddings)
    
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    
    response = qa_chain.run(query)
    return response

st.title("LangChain ver.2 RAG APP with CSV")

st.markdown("""
## このアプリケーションの使い方

1. **データの準備**: 
   - CSVファイルを `data` フォルダに `data.csv` という名前で配置します。
   - このCSVファイルには、質問応答の対象となるデータが含まれている必要があります。

2. **エンベッディングの実行**:
   - 下の「エンベッディングを実行」ボタンをクリックします。
   - これにより、CSVファイルのデータがベクトルデータベースに登録されます。
   - エンベッディングは、新しいデータを追加したときや、データを更新したときに実行する必要があります。

3. **質問の入力**:
   - エンベッディングが完了したら、下の入力欄に質問を入力します。
   - 質問は、CSVファイルに含まれるデータに関連するものにしてください。
   - 「質問を実行」ボタンをクリックすると、AIが回答を生成します。

注意: エンベッディングの実行には時間がかかる場合があります。大きなCSVファイルの場合は、しばらくお待ちください。
""")

if st.button("エンベッディングを実行"):
    load_and_embed_data()

query = st.text_input("質問を入力してください：")
if st.button("質問を実行"):
    if query:
        response = query_data(query)
        st.write("回答:", response)
    else:
        st.warning("質問を入力してください。")
