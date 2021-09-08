import torch
print("Cuda available: ", torch.cuda.is_available())
print("Device name:", torch.cuda.get_device_name())