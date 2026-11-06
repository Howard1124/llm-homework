import os
from google import genai

def generate_news_summary():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("錯誤：找不到 GEMINI_API_KEY！")
        return

    client = genai.Client(api_key=api_key)

    news_text = """
    科技巨頭今日發表最新一代人工智慧模型，該模型在語言理解與程式碼生成能力上皆有顯著提升。
    研發團隊指出，新模型不僅訓練效率提升，更引入了強大多模態處理能力。
    產業分析師預估，這項技術突破將進一步推動企業端 AI 應用的普及。
    """

    print("=== 新聞摘要產生器 ===")
    prompt = f"請針對以下新聞內容進行重點摘要，列出 3 個核心要點：\n\n{news_text}"

    response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt
    )

    for chunk in response:
        print(chunk.text, end="", flush=True)

if __name__ == "__main__":
    generate_news_summary()
