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

# Section 2: Division with Fractions - NOW WITH FIXED INTERACTIVE PIZZA CUTTER!
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

# FIXED INTERACTIVE PIZZA CUTTER WITH PERFECT SYMMETRY AND REALISTIC PEPPERONI!
st.markdown("#### 🍕 Interactive Pizza Division with Real Pizza Cutter!")
st.markdown("**Try the interactive pizza cutter below to see division in action:**")

# Embed the FIXED interactive pizza cutter HTML with realistic pepperoni distribution
pizza_cutter_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            margin: 0;
            padding: 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        .pizza-container {{
            background: rgba(255, 255, 255, 0.95);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
            max-width: 700px;
            width: 100%;
        }}

        .controls {{
            margin-bottom: 20px;
            text-align: center;
        }}

        .slider-label {{
            font-size: 1.2em;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
            display: block;
        }}

        .slider {{
            width: 100%;
            height: 12px;
            border-radius: 6px;
            background: linear-gradient(90deg, #8B4513, #D2691E, #CD853F);
            outline: none;
            -webkit-appearance: none;
            margin: 15px 0;
            position: relative;
            box-shadow: inset 0 3px 6px rgba(0, 0, 0, 0.3);
            border: 2px solid #654321;
        }}

        .slider::-webkit-slider-thumb {{
            -webkit-appearance: none;
            appearance: none;
            width: 80px;
            height: 80px;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 90 90"><defs><linearGradient id="woodHandle" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:%23DEB887"/><stop offset="20%" style="stop-color:%23D2691E"/><stop offset="50%" style="stop-color:%23CD853F"/><stop offset="80%" style="stop-color:%23A0522D"/><stop offset="100%" style="stop-color:%238B4513"/></linearGradient><radialGradient id="metalWheel" cx="50%" cy="50%" r="50%"><stop offset="0%" style="stop-color:%23F5F5F5"/><stop offset="40%" style="stop-color:%23E8E8E8"/><stop offset="70%" style="stop-color:%23C0C0C0"/><stop offset="100%" style="stop-color:%23808080"/></radialGradient></defs><ellipse cx="45" cy="22" rx="10" ry="22" fill="url(%23woodHandle)" stroke="%23654321" stroke-width="1.5"/><line x1="38" y1="8" x2="40" y2="36" stroke="%23654321" stroke-width="1" opacity="0.7"/><line x1="50" y1="6" x2="52" y2="38" stroke="%23654321" stroke-width="1" opacity="0.7"/><ellipse cx="45" cy="12" rx="8" ry="2.5" fill="none" stroke="%23654321" stroke-width="0.8" opacity="0.5"/><ellipse cx="45" cy="17" rx="8" ry="2.5" fill="none" stroke="%23654321" stroke-width="0.8" opacity="0.5"/><ellipse cx="45" cy="22" rx="8" ry="2.5" fill="none" stroke="%23654321" stroke-width="0.8" opacity="0.5"/><ellipse cx="45" cy="27" rx="8" ry="2.5" fill="none" stroke="%23654321" stroke-width="0.8" opacity="0.5"/><ellipse cx="45" cy="32" rx="8" ry="2.5" fill="none" stroke="%23654321" stroke-width="0.8" opacity="0.5"/><ellipse cx="45" cy="8" rx="9" ry="4" fill="%23A0522D" stroke="%23654321" stroke-width="1"/><rect x="40" y="40" width="10" height="12" fill="%23A9A9A9" stroke="%23696969" stroke-width="1.5" rx="1"/><circle cx="43" cy="44" r="1.5" fill="%23696969"/><circle cx="47" cy="48" r="1.5" fill="%23696969"/><circle cx="45" cy="65" r="20" fill="url(%23metalWheel)" stroke="%23696969" stroke-width="2.5"/><circle cx="45" cy="65" r="18" fill="none" stroke="%23B8B8B8" stroke-width="1.5" opacity="0.8"/><circle cx="45" cy="65" r="15" fill="none" stroke="%23D3D3D3" stroke-width="1" opacity="0.6"/><circle cx="45" cy="65" r="4" fill="%23696969"/><circle cx="45" cy="65" r="19" fill="none" stroke="%23FF6B6B" stroke-width="1.5" opacity="0.4" stroke-dasharray="3,2"/></svg>') center/contain no-repeat;
            cursor: grab;
            border-radius: 50%;
            transition: all 0.3s ease;
            filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.2));
        }}

        .slider::-webkit-slider-thumb:hover {{
            transform: scale(1.1) rotate(10deg);
            filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.3));
        }}

        .slider::-webkit-slider-thumb:active {{
            cursor: grabbing;
            transform: scale(1.05) rotate(-8deg);
        }}

        .slice-display {{
            background: linear-gradient(135deg, #ffeaa7, #fab1a0);
            padding: 15px;
            border-radius: 12px;
            margin: 15px 0;
            text-align: center;
            border: 2px solid #fdcb6e;
        }}

        .slice-count {{
            font-size: 1.8em;
            font-weight: bold;
            color: #2d3436;
            margin: 0;
        }}

        .fraction-display {{
            font-size: 1.2em;
            color: #636e72;
            margin: 5px 0;
        }}

        .math-explanation {{
            background: linear-gradient(135deg, #a8e6cf, #dcedc1);
            padding: 15px;
            border-radius: 12px;
            margin: 15px 0;
            border: 2px solid #81c784;
        }}

        .highlight {{
            background: rgba(255, 235, 59, 0.8);
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: bold;
        }}

        .cutting-board {{
            background: linear-gradient(45deg, #D2691E, #CD853F);
            border-radius: 8px;
            padding: 8px;
            margin: 10px 0;
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
        }}

        .instruction-text {{
            font-size: 0.9em;
            color: #555;
            margin: 10px 0;
            font-style: italic;
        }}

        .pepperoni {{
            animation: pepperoniPop 0.6s ease-out;
        }}

        @keyframes pepperoniPop {{
            0% {{ transform: scale(0); opacity: 0; }}
            60% {{ transform: scale(1.2); opacity: 0.9; }}
            100% {{ transform: scale(1); opacity: 1; }}
        }}

        .slice-line {{
            stroke: #000;
            stroke-width: 4;
            stroke-linecap: round;
            opacity: 1;
        }}

        .permanent-line {{
            animation: sliceDrawOnce 0.8s ease-out;
        }}

        @keyframes sliceDrawOnce {{
            0% {{ stroke-dasharray: 300; stroke-dashoffset: 300; }}
            100% {{ stroke-dasharray: none; stroke-dashoffset: 0; }}
        }}
    </style>
</head>
<body>
    <div class="pizza-container">
        <div class="controls">
            <label class="slider-label">🔪 Drag the Pizza Cutter: <span id="sliceValue">{divisor}</span> slices</label>
            <div class="instruction-text">← Fewer Slices &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; More Slices →</div>
            <div class="cutting-board">
                <input type="range" min="2" max="16" value="{divisor}" class="slider" id="sliceSlider">
            </div>
            
            <div class="slice-display">
                <p class="slice-count" id="sliceCount">{divisor} slices</p>
                <p class="fraction-display">Each slice = <span class="highlight" id="fractionDisplay">1/{divisor}</span> of the pizza</p>
            </div>
        </div>

        <div style="display: flex; justify-content: center; margin: 20px 0 40px 0;">
            <svg width="400" height="400" id="pizzaSvg" style="filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.2));">
                <circle cx="200" cy="200" r="160" fill="#D2691E" stroke="#8B4513" stroke-width="4"/>
                <circle cx="200" cy="200" r="155" fill="#FFD700" opacity="0.8"/>
                <circle cx="200" cy="200" r="150" fill="none" stroke="#F4D03F" stroke-width="1" opacity="0.5"/>
            </svg>
        </div>

        <div class="math-explanation">
            <div id="mathExplanation">
                <p><strong>🍕 Pizza ÷ {divisor} = {divisor} equal slices</strong></p>
                <p>Each slice = <span class="highlight">1/{divisor}</span> = <span class="highlight">{1/divisor:.3f}</span></p>
                <p><strong>🔢 Algebra:</strong> If pizza = n, then each slice = <span class="highlight">n/{divisor}</span></p>
            </div>
        </div>
    </div>

    <script>
        const slider = document.getElementById('sliceSlider');
        const sliceValue = document.getElementById('sliceValue');
        const sliceCount = document.getElementById('sliceCount');
        const fractionDisplay = document.getElementById('fractionDisplay');
        const mathExplanation = document.getElementById('mathExplanation');
        const pizzaSvg = document.getElementById('pizzaSvg');

        const centerX = 200;
        const centerY = 200;
        const radius = 150;

        // FIXED: Realistic pepperoni distribution like real pizza makers do it!
        function generatePepperoni(numSlices) {{
            const pepperoniData = [];
            
            // Use consistent seed for same results every time
            let seed = 42069;
            function seededRandom() {{
                seed = (seed * 9301 + 49297) % 233280;
                return seed / 233280;
            }}
            
            // REALISTIC PIZZA APPROACH: Distribute pepperoni across the whole pizza first,
            // then let the slice lines cut through wherever they fall - just like real pizza!
            
            const totalPepperoni = Math.max(16, numSlices * 2); // More pepperoni for bigger pizzas
            
            // Create rings of pepperoni from center outward (like real pizza makers)
            const rings = [
                {{ radius: 0.2, count: 3 }},     // Center ring - a few pieces
                {{ radius: 0.45, count: 6 }},    // Middle ring - moderate amount  
                {{ radius: 0.7, count: 8 }},     // Outer ring - most pieces
                {{ radius: 0.85, count: 4 }}     // Edge ring - just a few near crust
            ];
            
            rings.forEach(ring => {{
                const angleStep = (2 * Math.PI) / ring.count;
                
                for (let i = 0; i < ring.count; i++) {{
                    // Start with evenly spaced angles, then add realistic randomness
                    const baseAngle = i * angleStep;
                    const angleJitter = (seededRandom() - 0.5) * 0.8; // Realistic placement variation
                    const angle = baseAngle + angleJitter;
                    
                    // Add distance variation for natural look
                    const radiusJitter = (seededRandom() - 0.5) * 0.15;
                    const distance = (ring.radius + radiusJitter) * radius;
                    
                    // Make sure pepperoni stays on the pizza
                    const finalDistance = Math.min(distance, radius * 0.9);
                    
                    const x = centerX + finalDistance * Math.cos(angle);
                    const y = centerY + finalDistance * Math.sin(angle);
                    
                    pepperoniData.push({{ 
                        x: x, 
                        y: y, 
                        size: 8 + seededRandom() * 4 // Vary pepperoni sizes slightly
                    }});
                }}
            }});
            
            // Add a few random scattered pieces for realism
            for (let i = 0; i < 4; i++) {{
                const angle = seededRandom() * 2 * Math.PI;
                const distance = seededRandom() * radius * 0.8;
                const x = centerX + distance * Math.cos(angle);
                const y = centerY + distance * Math.sin(angle);
                
                pepperoniData.push({{ 
                    x: x, 
                    y: y, 
                    size: 7 + seededRandom() * 3
                }});
            }}
            
            return pepperoniData;
        }}

        // FIXED: Perfect symmetrical pizza slicing
        function updatePizza() {{
            const numSlices = parseInt(slider.value);
            
            sliceValue.textContent = numSlices;
            sliceCount.textContent = `${{numSlices}} slices`;
            fractionDisplay.textContent = `1/${{numSlices}}`;
            
            const decimalValue = (1/numSlices).toFixed(3);
            const percentage = ((1/numSlices) * 100).toFixed(1);
            
            mathExplanation.innerHTML = `
                <p><strong>🍕 Pizza ÷ ${{numSlices}} = ${{numSlices}} equal slices</strong></p>
                <p>Each slice = <span class="highlight">1/${{numSlices}}</span> = <span class="highlight">${{decimalValue}}</span> = <span class="highlight">${{percentage}}%</span></p>
                <p><strong>🔢 Algebra:</strong> If pizza = n, then each slice = <span class="highlight">n/${{numSlices}}</span></p>
            `;

            // Clear ALL existing elements
            const existingPepperoni = pizzaSvg.querySelectorAll('.pepperoni');
            const existingLines = pizzaSvg.querySelectorAll('.slice-line');
            existingPepperoni.forEach(p => p.remove());
            existingLines.forEach(l => l.remove());

            // FIX: Calculate EXACT angles with perfect symmetry
            const exactAngleStep = (2 * Math.PI) / numSlices; // Perfect mathematical division
            
            // Add pepperoni using REALISTIC pizza distribution!
            const pepperoniData = generatePepperoni(numSlices);
            pepperoniData.forEach((pep, index) => {{
                setTimeout(() => {{
                    const pepperoni = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                    pepperoni.setAttribute('cx', pep.x);
                    pepperoni.setAttribute('cy', pep.y);
                    pepperoni.setAttribute('r', pep.size || 10); // Use variable sizes
                    pepperoni.setAttribute('fill', '#DC143C');
                    pepperoni.setAttribute('stroke', '#8B0000');
                    pepperoni.setAttribute('stroke-width', '1');
                    pepperoni.setAttribute('class', 'pepperoni');
                    pizzaSvg.appendChild(pepperoni);
                }}, index * 15); // Faster animation
            }});

            // FIX: Draw lines with PERFECT symmetry - each calculated independently using i * (2π / numSlices)
            for (let i = 0; i < numSlices; i++) {{
                setTimeout(() => {{
                    // CRITICAL FIX: Beautiful formula in action! Calculate each angle independently from zero
                    const exactAngle = i * exactAngleStep; // No accumulation, no drift - pure math!
                    
                    // Calculate endpoint with maximum precision
                    const x2 = centerX + radius * Math.cos(exactAngle);
                    const y2 = centerY + radius * Math.sin(exactAngle);
                    
                    const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                    line.setAttribute('x1', centerX);
                    line.setAttribute('y1', centerY);
                    line.setAttribute('x2', x2.toFixed(2)); // Round to prevent floating point issues
                    line.setAttribute('y2', y2.toFixed(2));
                    line.setAttribute('stroke', '#000');
                    line.setAttribute('stroke-width', '4');
                    line.setAttribute('stroke-linecap', 'round');
                    line.setAttribute('class', 'slice-line permanent-line');
                    pizzaSvg.appendChild(line);
                }}, i * 60 + 50);
            }}
        }}

        slider.addEventListener('input', function() {{
            const pizzaSvg = document.getElementById('pizzaSvg');
            pizzaSvg.style.transform = 'rotate(1deg) scale(1.02)';
