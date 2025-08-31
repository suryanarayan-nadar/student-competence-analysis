


# 📄 code/generate_prompt.py

from transformers import AutoModelForCausalLM, AutoTokenizer # type: ignore

# Load Code Llama model (small instruct variant for demo)
model_name = "codellama/CodeLlama-7b-Instruct-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

student_code = """\
# Student's Python code for computing factorial
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
"""

prompt = (
    "A student wrote the following code. "
    "Without giving the answer, ask a question that guides the student to reflect on their logic:\n\n"
    + student_code + "\n"
)

input_ids = tokenizer(prompt, return_tensors="pt").input_ids
output = model.generate(input_ids, max_new_tokens=80)
question = tokenizer.decode(output[0], skip_special_tokens=True)

print("Generated guiding question:\n", question)
