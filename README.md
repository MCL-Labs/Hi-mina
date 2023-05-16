# Hi-mina
An API Service for Open Sourced LLMs 


## Prepare

```bash
# BLAS for CPU
sudo apt-get install libopenblas-dev
# or cuBLAS for Nividia GPU
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda
# install pdm
curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python -
```

## Install

```bash
# cuBlAS
CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
# OpenBLAS
CMAKE_ARGS="-DLLAMA_OPENBLAS=on" FORCE_CMAKE=1 pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

## Local Build LLama cpp python with cuBLAS

```bash
export PATH=/usr/local/cuda/bin:$PATH
cd vendor/llama.cpp
LLAMA_CUBLAS=1 make
```


## References

- https://github.com/abetlen/llama-cpp-python/issues/199
- https://github.com/abetlen/llama-cpp-python/issues/196
- https://github.com/abetlen/llama-cpp-python/issues/131
- https://stackoverflow.com/questions/25185405/using-gpu-from-a-docker-container
- https://github.com/ggerganov/llama.cpp/issues/1464
- https://huggingface.co/eachadea
- https://twitter.com/9hills/status/1649676874405277703?lang=en
- https://github.com/ymcui/Chinese-LLaMA-Alpaca/wiki/%E6%89%8B%E5%8A%A8%E6%A8%A1%E5%9E%8B%E5%90%88%E5%B9%B6%E4%B8%8E%E8%BD%AC%E6%8D%A2 
- https://github.com/ymcui/Chinese-LLaMA-Alpaca
- https://huggingface.co/decapoda-research
