import ollama

# preparing a prompt for generating a Kubernetes deployment YAML for a given application

PROMPT = """
ONLY generate Kubernetes YAML manifests.
Include:
- Namespace
- Deployment
- Service
- ConfigMap
- HPA
Follow Kubernetes best practices.
Do not add explanations.
"""

# write a function to generate the Kubernetes YAML using the Ollama API 
def generate_kubernetes_yaml(app_name, image_name):
    full_prompt = PROMPT + f"\nApplication Name: {app_name}\nImage Name: {image_name}\n"
    response = ollama.chat(model='llama3.1:8b', messages=[{'role': 'user', 'content': full_prompt}])
    return response['message']['content']

# invoke the function and print the result
if __name__ == '__main__':
    app_name = input("Enter the application name: ")
    image_name = input("Enter the Docker image name: ")
    kubernetes_yaml = generate_kubernetes_yaml(app_name, image_name)
    print("\nGenerated Kubernetes YAML:\n")
    print(kubernetes_yaml)

    