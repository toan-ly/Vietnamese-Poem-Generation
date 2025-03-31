import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Vietnamese Poem Generator",
    page_icon='📝',
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Vietnamese Poem Generator")

with st.expander("Instructions"):
    st.write("""
    1. Enter a few words or sentences as a suggestion for the poem.
    2. Adjust the parameters to change the way the poem is generated:
       - Temperature: Higher values produce more diverse results.
       - Top-k: The number of words with the highest probability to choose from at each step.
       - Top-p: Cumulative probability threshold for word selection.
       - Repetition penalty: Adjust to avoid repetition.
    3. Press the "Generate Poem" button to create the poem.
    """)

prompt_input = st.text_area("Enter words or sentences to start:",
                          value="2 3 con mực\n",
                          height=100)

col1, empty_col, col2 = st.columns([0.7, 0.3, 1.0])
with col1:
    max_length = st.slider("Max Output Tokens:", 10, 200, 75)
    temperature = st.slider("Temperature:", 0.1, 1.5, 0.8)
    top_k = st.slider("Top-k:", 1, 100, 50)
    top_p = st.slider("Top-p:", 0.1, 1.0, 0.95)
    repetition_penalty = st.slider("Repetition Penalty:", 1.0, 2.0, 1.2)

with empty_col:
    st.empty()

with col2:
    if st.button("Generate Poem ✨"):
        with st.spinner("Generating poem..."):
            try:
                generator = pipeline('text-generation', model='thangduong0509/gpt2_viet_poem_generation')
                results = generator(
                    prompt_input,
                    max_new_tokens=max_length,
                    do_sample=True,
                    top_k=top_k,
                    top_p=top_p,
                    temperature=temperature,
                    repetition_penalty=repetition_penalty
                )

                generated_text = results[0]['generated_text']
                st.subheader("Generated Poem:")

                for line in generated_text.split('\n'):
                    st.write(line)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")