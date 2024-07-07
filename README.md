# RAG (Retrieval Augmented Generation) アプリケーション

## 概要

このアプリケーションは、CSVファイルのデータを基にした練習用の質問応答システムです。Langchain、OpenAI、Chroma、Streamlitを使用して構築されており、以下の機能を提供します：

- CSVデータのエンベディングと保存
- 保存されたデータに基づく質問応答

## How to Use

1. リポジトリのクローン：
```
git clone 
cd rag-application
```

2. `secrets.toml`ファイルの設定：
`.streamlit/secrets.toml`ファイルを作成し、OpenAI APIキーを追加します。
```toml
# touch .streamlit/secrets.toml
OPENAI_API_KEY = "your_openai_api_key_here"
```
3. CSVファイルの準備：
質問応答の対象となるデータを含むCSVファイルをdata/data.csvとして配置します。

4. Dockerイメージのビルドと起動：
```
docker-compose up --build
```
5. アプリケーションへのアクセス：
   ブラウザで`http://localhost:8501`を開きます。

6. アプリケーションの使用：
   - 「エンベッディングを実行」ボタンをクリックして、CSVデータをベクトルデータベースに登録します。
   - 質問を入力し、「質問を実行」ボタンをクリックして回答を得ます。

## 注意事項

- 初回実行時や、CSVファイルを更新した場合は、必ず「エンベッディングを実行」ボタンをクリックしてください。
- 大きなCSVファイルの場合、エンベッディングに時間がかかる場合があります。
- APIキーは安全に管理し、公開リポジトリにコミットしないよう注意してください。

## トラブルシューティング

- エラーが発生した場合は、コンソールログを確認してください。
- CSVファイルが正しく配置されているか確認してください。
- OpenAI APIキーが正しく設定されているか確認してください。
