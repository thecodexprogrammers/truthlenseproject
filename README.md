IF IT SHOWS WEB CANT BE FOUND THEN 
RUN THIS ON CODESPACE named FANTASTIC WAFFLE - BY USING COMMAND IN TERMINAL - python -m streamlit run app.py

OR

HERE IS THE DEPLOYMENT LINK FOR DIRECT RESULT - https://fantastic-waffle-wrppg497749p29jwr-8501.app.github.dev/ (WHEN ITS ACTIVE)

⚖️ TruthLens: AI Fake News & Bias Detector
TruthLens is an AI-powered web application designed to help users navigate the complex landscape of modern media. By pasting a news URL, the app analyzes the content for political bias, sensationalism, and factual credibility using advanced Natural Language Processing.

if you want to run this just copy the code to vs code or anyother python prog..software and past it over there and to run read discription below (Installation and setup)

🚀 Features
Web Scraping: Automatically extracts clean text from any news article URL.

Bias Analysis: Identifies whether an article leans Left, Right, or Center.

Sensationalism Detection: Highlights "red flags" and emotional language used to manipulate readers.

Credibility Score: Provides a verdict on whether the content is likely factual or opinion-based.

🛠️ Tech Stack
Frontend: Streamlit

AI Model: OpenAI GPT-4o-mini

Data Extraction: Newspaper3k

Language: Python 3.x

📦 Installation & Setup
Clone the repository:

Bash

git clone https://github.com/your-username/truthlens.git
cd truthlens
Install dependencies:

Bash

pip install streamlit openai newspaper3k lxml_html_clean
Set up your API Key: Open app.py and replace "your-openai-key-here" with your actual OpenAI API key.

Run the application:

Bash

streamlit run app.py
📖 How to Use
Find a news article you want to analyze.

Copy the URL and paste it into the TruthLens input box.

Click "Analyze Credibility".

Review the AI-generated report on bias and sensationalism.

🛡️ Limitations
Works best with English-language news articles.

Accuracy depends on the depth of the article provided.

Requires an active internet connection to fetch articles and contact the OpenAI API.
