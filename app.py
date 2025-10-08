import streamlit as st
import anthropic
import re

# Page config
st.set_page_config(page_title="Prompt Engineering Workshop", layout="wide")

# Initialize session state
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""
if 'exercise_status' not in st.session_state:
    st.session_state.exercise_status = {}

# Custom CSS for success highlighting
st.markdown("""
<style>
.success-box textarea {
    background-color: #d4edda !important;
    border: 2px solid #28a745 !important;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🎓 Prompt Engineering Workshop")
st.markdown("### Learn to write better prompts with Few-Shot Learning and XML Tags")

# API Key Input
with st.sidebar:
    st.header("🔑 API Configuration")
    api_key_input = st.text_input(
        "Enter your Claude API Key",
        type="password",
        value=st.session_state.api_key,
        help="Your API key is only stored for this session"
    )
    if api_key_input:
        st.session_state.api_key = api_key_input
        st.success("API Key set!")
    else:
        st.warning("Please enter your API key to use the exercises")

# Helper function to call Claude API
def call_claude(prompt, api_key):
    try:
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"

# Validation functions
def validate_sentiment(response):
    response_lower = response.lower()
    return "positive" in response_lower or "negative" in response_lower or "neutral" in response_lower

def validate_multi_label(response):
    response_lower = response.lower()
    categories = ["technical", "pricing", "customer service", "delivery"]
    found = sum(1 for cat in categories if cat in response_lower)
    return found >= 2

def validate_xml_basic(response):
    return "<instruction>" in response or "<context>" in response or "<task>" in response

def validate_xml_advanced(response):
    xml_tags = ["<customer_data>", "<analysis_requirements>", "<output_format>"]
    found = sum(1 for tag in xml_tags if tag in response)
    return found >= 2

# Exercise component
def exercise_box(exercise_id, title, description, initial_prompt, validation_func, solution_prompt, test_input):
    st.subheader(title)
    st.markdown(description)
    
    # Check if exercise is completed
    is_completed = st.session_state.exercise_status.get(exercise_id, False)
    
    # Prompt input
    if is_completed:
        st.markdown('<div class="success-box">', unsafe_allow_html=True)
    
    user_prompt = st.text_area(
        "Your Prompt:",
        value=initial_prompt,
        height=150,
        key=f"prompt_{exercise_id}",
        disabled=is_completed
    )
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("Test Prompt", key=f"test_{exercise_id}", disabled=not st.session_state.api_key or is_completed):
            if st.session_state.api_key:
                with st.spinner("Testing your prompt..."):
                    # Combine user prompt with test input
                    full_prompt = user_prompt + "\n\n" + test_input
                    response = call_claude(full_prompt, st.session_state.api_key)
                    
                    st.markdown("**Claude's Response:**")
                    st.info(response)
                    
                    # Validate response
                    if validation_func(response):
                        st.success("✅ Great job! Your prompt works correctly!")
                        st.session_state.exercise_status[exercise_id] = True
                        st.rerun()
                    else:
                        st.error("❌ Not quite right. Try to improve your prompt based on the concept explanation.")
    
    with col2:
        if st.button("Show Solution", key=f"solution_{exercise_id}"):
            st.markdown("**Solution Prompt:**")
            st.code(solution_prompt, language="text")
    
    if is_completed:
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")

# Main content
tabs = st.tabs(["📚 Few-Shot Learning", "🏷️ XML Tags"])

# TAB 1: Few-Shot Learning
with tabs[0]:
    st.header("Few-Shot Learning")
    
    st.markdown("""
    ### What is Few-Shot Learning?
    
    Few-shot learning means providing the AI with a few examples of what you want it to do before giving it the actual task. 
    This helps the model understand the pattern and format you're looking for.
    
    **Example:**
    Instead of just asking "Classify this review", you show examples:
    
    ```
    Review: "This product is amazing!" → Sentiment: Positive
    Review: "Terrible quality, broke after one day." → Sentiment: Negative
    Review: "It's okay, nothing special." → Sentiment: Neutral
    
    Now classify this review: "Best purchase ever!"
    ```
    
    The model learns from the examples and applies the same pattern to new inputs.
    """)
    
    st.markdown("### 🎯 Practice Exercises")
    
    # Exercise 1: Easy - Basic Sentiment
    exercise_box(
        exercise_id="fs_easy",
        title="Exercise 1: Basic Sentiment Classification",
        description="Improve the prompt to classify customer reviews as Positive, Negative, or Neutral.",
        initial_prompt="Classify this review.",
        validation_func=validate_sentiment,
        solution_prompt="""Here are some examples of review classifications:

Review: "Absolutely love this product! Worth every penny."
Sentiment: Positive

Review: "Worst purchase ever. Complete waste of money."
Sentiment: Negative

Review: "It's decent. Does the job but nothing impressive."
Sentiment: Neutral

Now classify the following review:""",
        test_input='Review: "Great quality and fast shipping!"'
    )
    
    # Exercise 2: Hard - Multi-label Classification
    exercise_box(
        exercise_id="fs_hard",
        title="Exercise 2: Multi-Category Classification",
        description="Improve the prompt to identify ALL relevant categories (Technical, Pricing, Customer Service, Delivery) mentioned in customer feedback.",
        initial_prompt="Tell me what this feedback is about.",
        validation_func=validate_multi_label,
        solution_prompt="""Here are examples of feedback categorization:

Feedback: "The app crashes frequently and customer support hasn't responded to my emails."
Categories: Technical, Customer Service

Feedback: "Great product but quite expensive. Shipping took forever."
Categories: Pricing, Delivery

Feedback: "Setup was complicated and the price is too high for what you get."
Categories: Technical, Pricing

Now categorize this feedback:""",
        test_input='Feedback: "The software is buggy and overpriced. Support team was unhelpful."'
    )

# TAB 2: XML Tags
with tabs[1]:
    st.header("XML Tags for Structured Prompts")
    
    st.markdown("""
    ### Why Use XML Tags?
    
    XML tags help structure your prompts, making it crystal clear to the AI where different parts of your instruction begin and end. 
    This is especially useful for complex prompts with multiple components.
    
    **Example:**
    
    Instead of:
    ```
    Analyze this customer feedback and create a summary. The feedback is: "Great product!" 
    Focus on sentiment and key themes.
    ```
    
    Use XML tags:
    ```
    <instruction>
    Analyze the customer feedback and create a summary focusing on sentiment and key themes.
    </instruction>
    
    <feedback>
    Great product! Fast shipping and excellent quality.
    </feedback>
    ```
    
    This makes your prompt more readable and helps the AI distinguish between instructions and data.
    """)
    
    st.markdown("### 🎯 Practice Exercises")
    
    # Exercise 3: Easy - Basic XML Structure
    exercise_box(
        exercise_id="xml_easy",
        title="Exercise 1: Basic XML Structure",
        description="Use XML tags to clearly separate the instruction from the text that needs to be summarized.",
        initial_prompt="Summarize this article about climate change: Climate change is affecting global temperatures and weather patterns.",
        validation_func=validate_xml_basic,
        solution_prompt="""<instruction>
Summarize the following article in 2-3 sentences.
</instruction>

<article>
Climate change is affecting global temperatures and weather patterns.
</article>""",
        test_input=""
    )
    
    # Exercise 4: Hard - Complex XML Structure
    exercise_box(
        exercise_id="xml_hard",
        title="Exercise 2: Complex Multi-Section Structure",
        description="Structure a complex prompt with customer data, analysis requirements, and output format using appropriate XML tags.",
        initial_prompt="Analyze this customer: John, 28, bought 3 items. Tell me about their behavior and suggest products in a bullet list.",
        validation_func=validate_xml_advanced,
        solution_prompt="""<customer_data>
Name: John
Age: 28
Purchase history: 3 items in electronics category
</customer_data>

<analysis_requirements>
1. Analyze purchasing behavior patterns
2. Identify customer segment
3. Suggest relevant product recommendations
</analysis_requirements>

<output_format>
Provide your analysis in the following structure:
- Customer Profile
- Behavior Analysis  
- Product Recommendations (as bullet list)
</output_format>""",
        test_input=""
    )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Built with Streamlit and Claude API | For educational purposes</p>
</div>
""", unsafe_allow_html=True)
