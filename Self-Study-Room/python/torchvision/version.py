__version__ = '0.4.0'
git_version = 'd31eafa9c59cd59533dd0b89a36d371e55337a48'
from torchvision import _C
if hasattr(_C, 'CUDA_VERSION'):
    cuda = _C.CUDA_VERSION
