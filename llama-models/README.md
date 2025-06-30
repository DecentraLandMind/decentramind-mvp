# 🧠 DecentraMind MVP
## `llama-server/` Directory Structure

```

llama-server/
│
├── Dockerfile
├── models/
│   └── tiny.gguf
└── run\_model.sh  # optional script

````

## 🔧 Build Docker Image

To build the Docker image:

```bash
docker build -t llama-runner .
````

## 🚀 Run Example

To run the model with a prompt:

```bash
docker run --rm llama-runner ./main -m models/tiny.gguf -p "What is decentralization?"
```

## 🧠 Model Used: TinyLlama

We use **TinyLlama** for testing:

* [TinyLlama on HuggingFace](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)

To download the model:

```bash
wget https://huggingface.co/cmp-nct/tiny-llama-gguf/resolve/main/TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf -O tiny.gguf
```
