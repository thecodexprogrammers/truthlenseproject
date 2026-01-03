import streamlit as st
import openai
import os
from newspaper import Article

from dotenv import load_dotenv
load_dotenv()
api_key= os.getenv("MY_KEY")
if api_key:
    client = openai.OpenAI(api_key=api_key)
else:
    print("error: API KEY NOT FOUND")

st.set_page_config(page_title="TruthLens AI", page_icon="⚖️")
st.title("⚖️ TruthLens: Fake News & Bias Detector")
st.write("Paste a news article URL below to analyze its credibility.")

url = st.text_input("Paste YOUR NEWS URL HERE :) :")

if url:
    try:
        with st.spinner("Fetching article content..."):
            # 3. Scrape the Article
            article = Article(url)
            article.download()
            article.parse()
            
            text_to_analyze = article.text[:4000] # Analyze first 4000 characters
            st.info(f"**Analyzing:** {article.title}")

        if st.button("Analyze Credibility"):
            with st.spinner("AI is checking for bias and facts..."):
                # 4. The Prompt
                prompt = f"""
                Analyze the following news text for:
                1. **Bias Score**: (Scale 1-10, where 1 is neutral and 10 is extreme bias).
                2. **Political Leaning**: (Left, Right, or Center).
                3. **Red Flags**: List any sensationalist language or logical fallacies.
                4. **Verdict**: Is this likely Fact or Opinion?

                Article Text:
                {text_to_analyze}
                """

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}]
                )
                
                result = response.choices[0].message.content

                # 5. Display the Analysis
                st.markdown("---")
                st.subheader("Analysis Results")
                st.write(result)

    except Exception as e:

        st.error(f"Could not process the URL. Error: {e}")






