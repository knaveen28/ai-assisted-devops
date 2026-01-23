import ollama

# preparing a prompt for generating a Dockerfile for a given programming language

PROMPT = """
ONLY Generate an ideal Dockerfile for language. Do not provide any description
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
"""

# write a function to generate the Dockerfile using the Ollama API

def generate_dockerfile(language):
    response = ollama.chat(model='llama3.1:8b', messages=[{'role': 'user', 'content': PROMPT.format(language=language)}])
    return response['message']['content']

# invoke the function and print the result

if __name__ == '__main__':
    language = input("Enter the programming language: ")
    dockerfile = generate_dockerfile(language)
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)