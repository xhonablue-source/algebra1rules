import streamlit as st
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="MathCraft | Understanding Algebra Notation", 
    layout="centered",
    page_icon="🧮"
)

# Header with logo-style branding
st.markdown("""
<div style="text-align: center; padding: 1rem; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 10px; margin-bottom: 2rem;">
    <h2 style="color: white; margin: 0; font-weight: bold;">🧮 MathCraft</h2>
    <p style="color: #f0f0f0; margin: 0; font-style: italic;">Hands-On Mathematical Thinking</p>
    <p style="color: #e0e0e0; margin: 0; font-size: 0.8rem; margin-top: 0.5rem;">© All Rights Reserved - Xavier Honablue M.Ed</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #4f46e5;'>🔤 Understanding Algebra Notation</h1>", unsafe_allow_html=True)

# Initialize session state
if "responses" not in st.session_state:
    st.session_state.responses = {}
if "all_responses" not in st.session_state:
    st.session_state.all_responses = []

# Student Information
if "responses" not in st.session_state:
    st.session_state.responses = {}
if "all_responses" not in st.session_state:
    st.session_state.all_responses = []

# Michigan Learning Standards
st.markdown("---")
st.markdown("### 📚 Michigan Learning Standards Addressed")
with st.expander("Click to view aligned standards"):
    st.markdown("""
    **6.EE.2** - Write, read, and evaluate expressions in which letters stand for numbers.
    *Applied through: Reading algebraic notation like 3x and n/8, translating between algebraic and arithmetic expressions*
    
    **6.EE.6** - Use variables to represent numbers and write expressions when solving real-world problems.
    *Applied through: Using variables in multiplication and division contexts, connecting to real situations*
    
    **5.OA.2** - Write simple expressions and interpret patterns in expressions.
    *Applied through: Recognizing patterns in algebraic notation, understanding structure of expressions*
    
    **Mathematical Practices:**
    - **MP.1** - Make sense of problems and persevere in solving them
    - **MP.2** - Reason abstractly and quantitatively *(translating between notation systems)*
    - **MP.3** - Construct viable arguments *(explaining why 3x means 3 · x)*
    - **MP.6** - Attend to precision *(using correct mathematical notation)*
    - **MP.7** - Look for structure *(recognizing patterns in algebraic expressions)*
    """)
st.markdown("---")
st.markdown("### 👨‍🎓 Student Information")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Name:", key="student_name")
with col2:
    date = st.text_input("Date:", key="student_date")

st.session_state.responses.update({"Name": name, "Date": date})

# Learning Objective
st.markdown("---")
st.markdown("""
### 🧠 Learning Objective
Learn to read and understand basic algebra notation by connecting symbols to their meanings through visual representations.

**Key Concept:** Algebra notation is just a shorter way to write math operations we already know!
""")

# Section 1: Multiplication Without the · Symbol
st.markdown("---")
st.markdown("### ✖️ Section 1: Multiplication Without the · Symbol")
st.markdown("**The Big Idea:** In algebra, we often skip writing the multiplication symbol!")

# Interactive multiplication examples
st.markdown("#### 🎯 Interactive Examples")
multiplier = st.slider("Choose a number for the examples:", 1, 10, 3, key="mult_slider")

# Create visual for 3x, 5x, etc.
fig1, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Visual 1: 3x means 3 times x
x_value = 4  # We'll use 4 as our x value for visualization
groups = multiplier
items_per_group = x_value

# Draw groups of x's
for group in range(groups):
    for item in range(items_per_group):
        x_pos = group * 1.5
        y_pos = item * 0.3
        ax1.text(x_pos, y_pos, 'x', fontsize=20, ha='center', va='center', 
                bbox=dict(boxstyle="circle,pad=0.1", facecolor="lightblue"))

ax1.set_xlim(-0.5, groups * 1.5)
ax1.set_ylim(-0.5, items_per_group * 0.3 + 0.5)
ax1.set_title(f'{multiplier}x means {multiplier} groups of x\n(if x = {x_value}, then {multiplier}x = {multiplier} · {x_value} = {multiplier * x_value})', 
              fontsize=14, fontweight='bold')
ax1.axis('off')

# Visual 2: Show the translation
ax2.text(0.5, 0.7, f'{multiplier}x', fontsize=36, ha='center', va='center', fontweight='bold', color='blue')
ax2.text(0.5, 0.5, '=', fontsize=24, ha='center', va='center')
ax2.text(0.5, 0.3, f'{multiplier} · x', fontsize=24, ha='center', va='center', color='red')
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.set_title('Algebra Notation ↔ Regular Math', fontsize=14, fontweight='bold')
ax2.axis('off')

# Visual 3: Multiple examples
examples = [f'{multiplier}x = {multiplier} · x', f'{multiplier}y = {multiplier} · y', f'{multiplier}n = {multiplier} · n']
for i, example in enumerate(examples):
    ax3.text(0.5, 0.8 - i*0.2, example, fontsize=16, ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow"))

ax3.set_xlim(0, 1)
ax3.set_ylim(0, 1)
ax3.set_title('Pattern Recognition', fontsize=14, fontweight='bold')
ax3.axis('off')

st.pyplot(fig1)

# Practice questions for multiplication
st.markdown("#### 🎮 Practice: What do these mean?")
practice_col1, practice_col2 = st.columns(2)

with practice_col1:
    q1 = st.selectbox("What does 5x mean?", 
                     ["5 + x", "5 · x", "5 - x", "5 ÷ x"], key="q1")
    q2 = st.selectbox("What does 7y mean?", 
                     ["7 + y", "7 · y", "7 - y", "7 ÷ y"], key="q2")

with practice_col2:
    q3 = st.selectbox("If n = 6, what is 4n?", 
                     ["10", "24", "2", "1.5"], key="q3")
    q4 = st.selectbox("Which means the same as 8 · m?", 
                     ["8 + m", "8m", "m + 8", "m - 8"], key="q4")

# Section 2: Division with Fractions
st.markdown("---")
st.markdown("### ➗ Section 2: Division Using Fraction Notation")
st.markdown("**The Big Idea:** n/8 means n divided by 8, just like a fraction!")

# Interactive division examples
divisor = st.slider("Choose a divisor for examples:", 2, 10, 8, key="div_slider")

# COMPLETELY REDESIGNED Division Visualization
st.markdown("#### 🎯 Visual Examples: What n/8 Really Means")

# Create a much larger, clearer figure
fig2, ax = plt.subplots(figsize=(14, 8))

# Set up the layout
n_value = 24
groups = divisor
items_per_group = n_value // groups

# Title and explanation at the top
ax.text(0.5, 0.95, f'n/{divisor} means n ÷ {divisor}', 
        transform=ax.transAxes, fontsize=24, ha='center', va='top', fontweight='bold', color='blue')
ax.text(0.5, 0.88, f'If n = {n_value}, then n/{divisor} = {n_value} ÷ {divisor} = {items_per_group}', 
        transform=ax.transAxes, fontsize=18, ha='center', va='top', color='red')

# Draw large, clear groups
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57', '#FF9FF3', '#54A0FF', '#5F27CD']
group_width = 0.8 / groups  # Divide the width among groups
item_size = min(group_width * 0.8, 0.08)  # Reasonable item size

for group in range(groups):
    # Group background
    group_x = 0.1 + group * group_width
    group_color = colors[group % len(colors)]
    
    # Draw background rectangle for each group
    rect = plt.Rectangle((group_x, 0.3), group_width * 0.9, 0.4, 
                        facecolor=group_color, alpha=0.2, edgecolor=group_color, linewidth=2)
    ax.add_patch(rect)
    
    # Add group label
    ax.text(group_x + group_width * 0.45, 0.75, f'Group {group+1}', 
            ha='center', va='center', fontsize=12, fontweight='bold', color=group_color)
    
    # Draw items in each group
    items_per_row = 3
    for item in range(items_per_group):
        row = item // items_per_row
        col = item % items_per_row
        
        item_x = group_x + (col + 0.5) * (group_width * 0.9 / items_per_row)
        item_y = 0.35 + row * 0.08
        
        circle = plt.Circle((item_x, item_y), item_size/2, 
                          facecolor=group_color, edgecolor='black', linewidth=1)
        ax.add_patch(circle)
    
    # Show count for each group
    ax.text(group_x + group_width * 0.45, 0.2, f'{items_per_group} items', 
            ha='center', va='center', fontsize=11, fontweight='bold')

# Add the equation at the bottom
ax.text(0.5, 0.1, f'{n_value} items ÷ {divisor} groups = {items_per_group} items per group', 
        transform=ax.transAxes, fontsize=16, ha='center', va='center', 
        bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", edgecolor="orange"))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

st.pyplot(fig2)

# Add a separate, clear pizza example
st.markdown("#### 🍕 Real-World Example: Pizza Division")
fig3, ax_pizza = plt.subplots(figsize=(8, 8))

# Draw a large, clear pizza
pizza_center = (0.5, 0.5)
pizza_radius = 0.35

# Pizza base
pizza = plt.Circle(pizza_center, pizza_radius, color='#D2691E', alpha=0.9, edgecolor='#8B4513', linewidth=3)
ax_pizza.add_patch(pizza)

# Add cheese layer
cheese = plt.Circle(pizza_center, pizza_radius * 0.95, color='#FFD700', alpha=0.7)
ax_pizza.add_patch(cheese)

# Add pepperoni
np.random.seed(42)
for _ in range(12):
    angle = np.random.uniform(0, 2*np.pi)
    distance = np.random.uniform(0, pizza_radius * 0.8)
    x = pizza_center[0] + distance * np.cos(angle)
    y = pizza_center[1] + distance * np.sin(angle)
    pepperoni = plt.Circle((x, y), 0.025, color='#DC143C', alpha=0.9)
    ax_pizza.add_patch(pepperoni)

# Draw slice lines
for i in range(divisor):
    angle = i * 2 * np.pi / divisor
    x_end = pizza_center[0] + pizza_radius * np.cos(angle)
    y_end = pizza_center[1] + pizza_radius * np.sin(angle)
    ax_pizza.plot([pizza_center[0], x_end], [pizza_center[1], y_end], 'k-', linewidth=3)

# Add labels
ax_pizza.text(0.5, 0.9, f'Pizza ÷ {divisor} = {divisor} equal slices', 
             transform=ax_pizza.transAxes, fontsize=16, ha='center', va='center', fontweight='bold')
ax_pizza.text(0.5, 0.1, f'Each person gets 1/{divisor} of the pizza', 
             transform=ax_pizza.transAxes, fontsize=14, ha='center', va='center',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue"))

ax_pizza.set_xlim(0, 1)
ax_pizza.set_ylim(0, 1)
ax_pizza.set_aspect('equal')
ax_pizza.axis('off')

st.pyplot(fig3)

# Analytical Thinking Questions
st.markdown("---")
st.markdown("### 🧠 Analytical Thinking: Why Does This Work?")
st.markdown("*Think deeply about these concepts:*")

analytical1 = st.text_area(
    "1. **Pattern Recognition**: Look at 2x, 3x, 4x, 5x. What pattern do you notice? Why do you think mathematicians decided to drop the multiplication symbol?",
    height=100,
    key="analytical1",
    placeholder="Think about: What's the same? What changes? Why might this be easier to write?"
)

analytical2 = st.text_area(
    "2. **Real-World Connections**: Give three examples from everyday life where you might use division notation like n/4. Explain why fraction notation might be clearer than writing '÷'.",
    height=100,
    key="analytical2", 
    placeholder="Examples: sharing pizza, dividing money, splitting time, etc."
)

analytical3 = st.text_area(
    "3. **Mathematical Reasoning**: If 3x means 3 · x, what do you think 3xy might mean? Explain your reasoning and give an example with numbers.",
    height=100,
    key="analytical3",
    placeholder="Think about: How does the pattern extend? What would happen if x=4 and y=5?"
)

analytical4 = st.text_area(
    "4. **Order of Operations**: In the expression 6x/2, which operation happens first and why? How might parentheses help make this clearer?",
    height=100,
    key="analytical4",
    placeholder="Consider: multiplication vs division, left to right, what parentheses would show the order clearly"
)

st.session_state.responses.update({
    "Analytical_1": analytical1,
    "Analytical_2": analytical2,
    "Analytical_3": analytical3,
    "Analytical_4": analytical4
})
st.markdown("#### 🎮 Practice: What do these mean?")
practice_col3, practice_col4 = st.columns(2)

with practice_col3:
    q5 = st.selectbox("What does x/4 mean?", 
                     ["x + 4", "x × 4", "x - 4", "x ÷ 4"], key="q5")
    q6 = st.selectbox("What does m/10 mean?", 
                     ["m + 10", "m × 10", "m - 10", "m ÷ 10"], key="q6")

with practice_col4:
    q7 = st.selectbox("If y = 20, what is y/5?", 
                     ["25", "100", "4", "15"], key="q7")
    q8 = st.selectbox("Which means the same as n ÷ 3?", 
                     ["3n", "n/3", "n + 3", "3/n"], key="q8")

# Section 3: Combined Operations
st.markdown("---")
st.markdown("### 🔄 Section 3: Combining Operations")
st.markdown("**The Big Idea:** We can combine multiplication and division in algebra notation!")

# Interactive combined examples
st.markdown("#### 🎯 Complex Examples")
coeff = st.slider("Choose a coefficient:", 2, 6, 3, key="coeff_slider")
divisor2 = st.slider("Choose a divisor:", 2, 8, 4, key="div2_slider")

fig3, (ax7, ax8) = plt.subplots(1, 2, figsize=(12, 5))

# Visual 1: 3x/4 breakdown
ax7.text(0.5, 0.9, f'{coeff}x/{divisor2}', fontsize=32, ha='center', va='center', fontweight='bold', color='purple')
ax7.text(0.5, 0.7, '↓', fontsize=24, ha='center', va='center')
ax7.text(0.5, 0.6, f'({coeff} · x) ÷ {divisor2}', fontsize=18, ha='center', va='center', color='blue')
ax7.text(0.5, 0.4, 'First multiply, then divide!', fontsize=14, ha='center', va='center', 
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen"))

if_x = 8
result = (coeff * if_x) // divisor2
ax7.text(0.5, 0.2, f'If x = {if_x}:', fontsize=14, ha='center', va='center')
ax7.text(0.5, 0.1, f'{coeff}x/{divisor2} = ({coeff} · {if_x}) ÷ {divisor2} = {coeff * if_x} ÷ {divisor2} = {result}', 
         fontsize=12, ha='center', va='center', color='red')

ax7.set_xlim(0, 1)
ax7.set_ylim(0, 1)
ax7.set_title('Order of Operations', fontsize=14, fontweight='bold')
ax7.axis('off')

# Visual 2: Visual representation
# Show coeff groups of x, then divide by divisor2
total_x = coeff * if_x
items_per_group = total_x // divisor2

for group in range(divisor2):
    group_color = plt.cm.Set1(group / divisor2)
    for item in range(items_per_group):
        x_pos = group + item * 0.1
        y_pos = 0.5 + group * 0.1
        ax8.text(x_pos, y_pos, 'x', fontsize=12, ha='center', va='center',
                bbox=dict(boxstyle="circle,pad=0.05", facecolor=group_color))

ax8.text(2, 0.8, f'{coeff}x = {total_x} total x\'s', fontsize=12, ha='center', va='center')
ax8.text(2, 0.2, f'÷ {divisor2} = {items_per_group} in each group', fontsize=12, ha='center', va='center')

ax8.set_xlim(-0.5, 4)
ax8.set_ylim(0, 1)
ax8.set_title(f'Visual: {coeff}x/{divisor2} with x = {if_x}', fontsize=14, fontweight='bold')
ax8.axis('off')

st.pyplot(fig3)

# Final practice
st.markdown("#### 🎮 Challenge Practice")
practice_col5, practice_col6 = st.columns(2)

with practice_col5:
    q9 = st.selectbox("What does 6y/3 mean?", 
                     ["(6 · y) ÷ 3", "6 + y ÷ 3", "6 · y · 3", "6 ÷ y ÷ 3"], key="q9")
    q10 = st.selectbox("If a = 10, what is 2a/5?", 
                      ["4", "7", "25", "1"], key="q10")

with practice_col6:
    q11 = st.selectbox("What's another way to write (4 · n) ÷ 8?", 
                      ["4n/8", "4 + n/8", "4/n8", "n/4 · 8"], key="q11")
    q12 = st.selectbox("Which operation happens first in 5x/2?", 
                      ["Division", "Multiplication", "Addition", "Subtraction"], key="q12")

# Answer key and feedback
st.markdown("---")
st.markdown("### ✅ Check Your Understanding")

# Store all responses
st.session_state.responses.update({
    "Q1": q1, "Q2": q2, "Q3": q3, "Q4": q4,
    "Q5": q5, "Q6": q6, "Q7": q7, "Q8": q8,
    "Q9": q9, "Q10": q10, "Q11": q11, "Q12": q12
})

# Answer key
correct_answers = {
    "Q1": "5 · x", "Q2": "7 · y", "Q3": "24", "Q4": "8m",
    "Q5": "x ÷ 4", "Q6": "m ÷ 10", "Q7": "4", "Q8": "n/3",
    "Q9": "(6 · y) ÷ 3", "Q10": "4", "Q11": "4n/8", "Q12": "Multiplication"
}

score = 0
for q_num in correct_answers:
    if st.session_state.responses.get(q_num) == correct_answers[q_num]:
        score += 1

if st.button("🎯 Check My Answers", type="primary"):
    st.markdown(f"### 📊 Your Score: {score}/12 ({(score/12)*100:.0f}%)")
    
    if score == 12:
        st.success("🌟 Perfect! You've mastered algebra notation!")
    elif score >= 10:
        st.success("🎯 Excellent work! You understand the concepts very well!")
    elif score >= 8:
        st.info("👍 Good job! Review the concepts you missed and try again!")
    else:
        st.warning("📚 Keep practicing! Focus on the visual examples above.")

# Summary section
st.markdown("---")
st.markdown("### 📝 Key Takeaways")
st.markdown("""
**Remember these patterns:**

1. **3x** means **3 · x** (multiplication without the · symbol)
2. **n/8** means **n ÷ 8** (division using fraction notation)  
3. **5y/4** means **(5 · y) ÷ 4** (multiply first, then divide)

**The secret:** Algebra notation is just shorthand for operations you already know!
""")

# Submit section
st.markdown("---")
if st.button("✅ Submit My Work", type="primary"):
    if name and date:
        st.session_state.all_responses.append(st.session_state.responses.copy())
        st.success(f"Great work {name}! Your score: {score}/12 ({(score/12)*100:.0f}%)")
    else:
        st.error("Please enter your name and date before submitting!")

# Teacher access (password protected)
st.markdown("---")
teacher_password = st.text_input("🏫 Teacher Access Code:", type="password", key="teacher_pass")

if teacher_password == "algebra2025":
    st.markdown("### 📊 Teacher Dashboard")
    if st.session_state.all_responses:
        df = pd.DataFrame(st.session_state.all_responses)
        st.dataframe(df, use_container_width=True)
        
        # Calculate class average
        if len(df) > 0:
            # Count correct answers for each student
            total_scores = []
            for _, row in df.iterrows():
                student_score = 0
                for q_num in correct_answers:
                    if row.get(q_num) == correct_answers[q_num]:
                        student_score += 1
                total_scores.append(student_score)
            
            avg_score = np.mean(total_scores)
            st.metric("Class Average", f"{avg_score:.1f}/12 ({(avg_score/12)*100:.0f}%)")
            
        # Download option
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download Class Data",
            data=csv,
            file_name="algebra_notation_responses.csv",
            mime="text/csv"
        )
    else:
        st.info("No student responses yet.")
elif teacher_password and teacher_password != "algebra2025":
    st.error("❌ Incorrect access code")

st.markdown("---")
st.markdown("*Keep practicing! Algebra notation gets easier with repetition! 🌟*")
