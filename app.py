import streamlit as st
from agent.question_agent import create_agent



def main():
    st.title("Ask Questions from Any Webpage using Langchain + Google Gemini")

    url = st.text_input("Enter a webpage URL:")
    question = st.text_input("Ask a question about the content of that page:")

    if st.button("Get Answer") and url and question:
        with st.spinner("Thinking..."):
            try:
                agent = create_agent()
                prompt = (
                    f"Use the tool to read the content from this URL: {url}. "
                    f"Then answer: {question}. "
                    f"Make sure the answer is strictly based on the webpage content and does not add anything extra."
                )
                response = agent.invoke(prompt)
                answer = response['output']
                
                # Display nicely formatted answer
                st.markdown("### 📘 Answer:")
                st.markdown(
                    f"""
                    <div style='
                        background-color: #f9f9f9;
                        padding: 1em;
                        border-radius: 10px;
                        border: 1px solid #ddd;
                        font-family: monospace;
                        white-space: pre-wrap;
                    '>{answer}</div>
                    """,
                    unsafe_allow_html=True
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")

# def main():
#     st.title("Ask Questions from Any Webpage using Langchain + Google Gemini")

#     url = st.text_input("Enter a webpage URL:")
#     question = st.text_input("Ask a question about the content of that page:")

#     if st.button("Get Answer") and url and question:
#         with st.spinner("Thinking..."):
#             try:
#                 agent = create_agent()
#                 prompt = f"Use the tool to read the content from this URL: {url}. Then answer: {question}.And make sure that should not add extra think from youe side , final result should be same as from provided URL "
#                 answer = agent.invoke(prompt)['output']
#                 st.success(answer)
#             except Exception as e:
#                 st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
