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


## References

- https://github.com/abetlen/llama-cpp-python/issues/199
- https://github.com/abetlen/llama-cpp-python/issues/196
