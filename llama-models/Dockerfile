# Dockerfile
FROM ubuntu:22.04

RUN apt update && apt install -y git build-essential cmake curl

WORKDIR /app
RUN git clone https://github.com/ggerganov/llama.cpp .
RUN make LLAMA_CUBLAS=0

COPY models/ ./models/

CMD ["./main", "-m", "models/tiny.gguf", "-p", "Hello!"]
