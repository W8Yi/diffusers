FROM nvidia/cuda:12.1.0-runtime-ubuntu20.04
LABEL maintainer="Hugging Face"
LABEL repository="diffusers"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y bash \
    build-essential \
    git \
    git-lfs \
    curl \
    ca-certificates \
    libsndfile1-dev \
    libgl1 \
    python3.9 \
    python3.9-dev \
    python3-pip \
    python3.9-venv && \
    rm -rf /var/lib/apt/lists

# make sure to use venv
RUN python3.9 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# pre-install the heavy dependencies (these can later be overridden by the deps from setup.py)
RUN python3.9 -m pip install --no-cache-dir --upgrade pip uv && \
    python3.9 -m uv pip install --no-cache-dir \
    torch \
    torchvision \
    torchaudio \
    invisible_watermark && \
    python3.9 -m pip install --no-cache-dir \
    accelerate \
    datasets \
    hf-doc-builder \
    huggingface-hub \
    Jinja2 \
    librosa \
    numpy \
    scipy \
    tensorboard \
    transformers

CMD ["/bin/bash"]
