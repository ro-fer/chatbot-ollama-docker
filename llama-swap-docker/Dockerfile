FROM ghcr.io/ggerganov/llama.cpp:server-cuda@sha256:e4c166bca0b0f154673f619dfda41bf4ee9a927920de438603a449c13b0b1feb

# Install wget for downloading llama-swap
RUN apt-get update && apt-get install -y \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Download and install llama-swap v172
RUN wget https://github.com/mostlygeek/llama-swap/releases/download/v172/llama-swap_172_linux_amd64.tar.gz -O /tmp/llama-swap.tar.gz \
    && tar -xzf /tmp/llama-swap.tar.gz -C /tmp \
    && mv /tmp/llama-swap /usr/bin/llama-swap \
    && chmod +x /usr/bin/llama-swap \
    && rm /tmp/llama-swap.tar.gz \
    && llama-swap --version

WORKDIR /app

ENTRYPOINT ["llama-swap"]
CMD ["--config", "/config/llama-swap.yaml", "--listen", "0.0.0.0:8090"]
