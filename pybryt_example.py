import pybryt # type: ignore

# Reference factorial function
def ref_factorial(n):
    if n <= 1:
        return 1
    return n * ref_factorial(n-1)

# Create PyBryt reference
ref = pybryt.ReferenceImplementation(ref_factorial)

# Example student submission
def student_fact(n):
    if n == 0:
        return 1
    return n * student_fact(n-1)

student_impl = pybryt.StudentImplementation(student_fact)

# Evaluate
res = ref.evaluate(student_impl)
print("PyBryt Feedback:\n", res)
