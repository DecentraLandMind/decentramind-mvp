# app/model_runner.py

def run_model(prompt: str) -> str:
    return f"You said: {prompt}"

#import subprocess

#def run_model(prompt: str) -> str:
#   result = subprocess.run([
#     "docker", "run", "--rm", "llama-runner",
#      "./main", "-m", "models/tiny.gguf", "-p", prompt
#   ], capture_output=True, text=True)
#
#    return result.stdout.strip()
