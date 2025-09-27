# 🤖 streamlit-llm-app

LangChainを使用したLLM専門家コンサルティングWebアプリケーション

## 📖 概要

このWebアプリは、LangChainを使用してLLM（大規模言語モデル）と連携し、選択した専門家の視点から質問に答えるコンサルティングアプリケーションです。

## 🎯 機能

- **専門家選択機能**: ラジオボタンで相談したい専門家を選択
- **LLM連携**: OpenAIのGPT-3.5-turboを使用
- **専門的回答**: 選択した専門家の視点からの回答を生成

## 👥 選択可能な専門家

- **経営コンサルタント**: ビジネス戦略、マーケティング、組織運営に関するアドバイス
- **ITエンジニア**: プログラミング、システム設計、技術的な問題解決に関するアドバイス

## 🚀 使用方法

1. 専門家の種類をラジオボタンで選択
2. 質問や相談内容をテキストエリアに入力
3. 「回答を取得」ボタンをクリック
4. 選択した専門家の視点からLLMが回答を生成

## 🛠️ 技術スタック

- **Frontend**: Streamlit
- **LLM Framework**: LangChain
- **LLM Model**: OpenAI GPT-3.5-turbo
- **Environment Management**: python-dotenv

## 📦 インストール

```bash
# リポジトリをクローン
git clone https://github.com/kentaro-seki/streamlit-llm-app.git
cd streamlit-llm-app

# 仮想環境を作成・アクティベート
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# 依存関係をインストール
pip install -r requirements.txt

# 環境変数を設定
cp .env.example .env
# .envファイルにOpenAI APIキーを設定
```

## ⚙️ 環境設定

`.env`ファイルに以下の環境変数を設定してください：

```
OPENAI_API_KEY=your_openai_api_key_here
```

## 🏃‍♂️ 実行

```bash
streamlit run app.py
```

アプリケーションは `http://localhost:8501` で実行されます。

## 🔐 セキュリティ

- OpenAI APIキーは`.env`ファイルに保存
- `.gitignore`で機密情報を保護
- APIキーがGitリポジトリにコミットされないよう設定済み