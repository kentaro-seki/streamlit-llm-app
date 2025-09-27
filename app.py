from dotenv import load_dotenv
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

def get_llm_response(user_input, expert_type):
    """
    LLMにプロンプトを送信し、回答を取得する関数
    
    Args:
        user_input (str): ユーザーからの入力テキスト
        expert_type (str): 専門家の種類（経営コンサルタント or ITエンジニア）
    
    Returns:
        str: LLMからの回答
    """
    try:
        # ChatOpenAIクライアントの初期化
        chat = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.7
        )
        
        # 専門家の種類に応じてシステムメッセージを設定
        if expert_type == "経営コンサルタント":
            system_message = SystemMessage(content="""
あなたは経験豊富な経営コンサルタントです。
経営戦略、マーケティング、組織運営、財務管理などの分野に深い知識を持っています。
ビジネスの課題に対して実践的で具体的なアドバイスを提供し、
クライアントの事業成長をサポートすることが専門です。
回答は専門的でありながらも分かりやすく、実行可能な提案を含めてください。
""")
        else:  # ITエンジニア
            system_message = SystemMessage(content="""
あなたは経験豊富なITエンジニアです。
プログラミング、システム設計、データベース、クラウド技術、セキュリティなどの
IT技術全般に深い知識を持っています。
技術的な問題の解決方法を提示し、最新の技術トレンドも考慮した
実践的なアドバイスを提供することが専門です。
回答は技術的に正確で、具体的な実装方法やベストプラクティスを含めてください。
""")
        
        # ユーザーメッセージの作成
        human_message = HumanMessage(content=user_input)
        
        # メッセージリストの作成
        messages = [system_message, human_message]
        
        # LLMに送信して回答を取得
        response = chat(messages)
        
        return response.content
        
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"

# Streamlitアプリケーションのメイン部分
st.title("🤖 LLM専門家コンサルティングアプリ")

# アプリの概要説明
st.markdown("""
## 📖 アプリの概要
このWebアプリは、LangChainを使用してLLM（大規模言語モデル）と連携し、
専門家の視点からあなたの質問にお答えします。

## 🔧 操作方法
1. **専門家の種類を選択**: ラジオボタンで相談したい専門家を選択してください
2. **質問を入力**: テキストフォームに相談内容や質問を入力してください  
3. **回答を取得**: 「回答を取得」ボタンをクリックすると、選択した専門家の視点からLLMが回答します

## 👥 選択可能な専門家
- **経営コンサルタント**: ビジネス戦略、マーケティング、組織運営に関するアドバイス
- **ITエンジニア**: プログラミング、システム設計、技術的な問題解決に関するアドバイス
""")

st.divider()

# 専門家選択のラジオボタン
expert_type = st.radio(
    "相談したい専門家を選択してください：",
    ["経営コンサルタント", "ITエンジニア"],
    help="選択した専門家の視点からLLMが回答します"
)

# 入力フォーム
user_input = st.text_area(
    "質問や相談内容を入力してください：",
    placeholder="例：新規事業の立ち上げについてアドバイスをください",
    height=120
)

# 回答取得ボタン
if st.button("💬 回答を取得", type="primary"):
    if user_input.strip():
        with st.spinner("回答を生成中..."):
            # LLMから回答を取得
            response = get_llm_response(user_input, expert_type)
            
            st.divider()
            
            # 選択した専門家の表示
            st.markdown(f"### 🎯 {expert_type}からの回答")
            
            # 回答の表示
            st.markdown(response)
            
    else:
        st.error("質問や相談内容を入力してから「回答を取得」ボタンを押してください。")
