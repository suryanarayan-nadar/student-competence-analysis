# Student Competence Analysis with Open-Source AI Models

This project evaluates open-source models for analyzing student-written Python code, 
with a focus on generating guiding prompts, detecting misconceptions, and encouraging deeper learning.

## 📌 Features
- Uses **Code Llama (7B - Python instruct)** to generate guiding questions from student code.
- Uses **PyBryt** for automated assessment of student code against reference solutions.
- Includes a research plan with evaluation methodology and reasoning.

## ⚙️ Setup
```bash
# Clone the repo
git clone https://github.com/<your-username>/student-competence-analysis.git
cd student-competence-analysis

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

🚀 Usage
1. Generate guiding questions (Code Llama)
python code/generate_prompt.py

2. Run PyBryt example
python code/pybryt_example.py
