from flask import Flask, render_template, request

app = Flask(__name__)

# Function to generate unique permutations
def generate_unique_permutations(s, current="", result=None):
    if result is None:
        result = set()  # Initialize the result set to keep unique permutations
    
    if len(s) == 0:
        result.add(current)  # Add the permutation to the result set
        return
    
    for i in range(len(s)):
        # Skip duplicate characters to avoid generating the same permutation
        if i > 0 and s[i] == s[i-1]:
            continue
        # Recursively generate permutations of the remaining string
        generate_unique_permutations(s[:i] + s[i+1:], current + s[i], result)
    
    return result

# Home route that displays the form and results
@app.route('/', methods=['GET', 'POST'])
def index():
    permutations = []
    num_permutations = 0  # Variable to store the number of permutations
    if request.method == 'POST':
        user_input = request.form['string_input']
        permutations = generate_unique_permutations(user_input)
        num_permutations = len(permutations)  # Get the number of unique permutations
    return render_template('index.html', permutations=permutations, num_permutations=num_permutations)

if __name__ == '__main__':
    app.run(debug=True)
