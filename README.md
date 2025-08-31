# Student Competence Analysis with Open-Source AI Models

This project evaluates open-source models for analyzing student-written Python code, 
with a focus on generating guiding prompts, detecting misconceptions, and encouraging deeper learning.

## 📌 Features
- Uses **Code Llama (7B - Python instruct)** to generate guiding questions from student code.
- Uses **PyBryt** for automated assessment of student code against reference solutions.
- Includes a research plan with evaluation methodology and reasoning.

Dependencies:

Install Python packages:

pip install transformers torch  # for CodeLlama
pip install pybryt              # for PyBryt (auto-assessment)


Download the model weights (example for CodeLlama 7B Instruct):

pip install git+https://github.com/huggingface/transformers  # if needed
Transformers will fetch weights automatically in the code above, or you can use `from_pretrained` with local cache.


Running the Example:
Save the above Python code into a script (e.g. generate_prompt.py).
Run python generate_prompt.py. The model will output a question guiding the student.
For PyBryt, prepare a reference solution and place student code in a file. Follow PyBryt docs (demo notebooks) to annotate.

Extending:
Fine-tuning: For better results, you could fine-tune the CodeLlama model on a dataset of code explanation dialogues.
Prompt Engineering: Experiment with different prompt templates (e.g. “Why do you think…”, “What will happen if…”) to see which elicit deep reasoning.

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

