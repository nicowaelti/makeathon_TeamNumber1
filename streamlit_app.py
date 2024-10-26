import streamlit as st
import requests
import json

# Fake API data
def get_fake_title():
    return "AI-Powered Text Analysis Platform"

def get_fake_api_response(text):
    # Simulate API response
    return f"Analysis Result: The text contains {len(text.split())} words and appears to be about technology."

def get_fake_papers():
    return [
        {
            "title": "Attention Is All You Need",
            "url": "https://arxiv.org/pdf/1706.03762",
            "authors": "Vaswani et al."
        },
        {
            "title": "BERT: Pre-training of Deep Bidirectional Transformers",
            "url": "https://arxiv.org/pdf/1706.03762",
            "authors": "Devlin et al."
        },
        {
            "title": "GPT-3: Language Models are Few-Shot Learners",
            "url": "https://arxiv.org/pdf/1706.03762",
            "authors": "Brown et al."
        },
        {
            "title": "Deep Learning for Natural Language Processing",
            "url": "https://arxiv.org/pdf/1706.03762",
            "authors": "Smith et al."
        },
        {
            "title": "The Future of AI in Text Analysis",
            "url": "https://arxiv.org/pdf/1706.03762",
            "authors": "Johnson et al."
        }
    ]

def main():
    # Page config
    st.set_page_config(
        page_title="Text Analysis Platform",
        layout="wide"
    )

    # Title from API 1 (simulated)
    st.title(get_fake_title())

    # Text input field
    user_text = st.text_area(
        "Enter your text for analysis:",
        height=200,
        placeholder="Type or paste your text here..."
    )

    # Analysis button
    if st.button("Analyze Text"):
        if user_text:
            # Get response from API 2 (simulated)
            response = get_fake_api_response(user_text)
            
            # Display response in a box
            st.info(response)
        else:
            st.warning("Please enter some text to analyze.")

    # Horizontal line
    st.markdown("---")

    # Research Papers Section
    st.header("Related Research Papers")
    
    papers = get_fake_papers()
    
    # Display papers in a clean format
    for paper in papers:
        with st.container():
            st.markdown(f"**{paper['title']}** - {paper['authors']}")
            st.markdown(f"[View Paper]({paper['url']})")
            st.markdown("---")

if __name__ == "__main__":
    main()
