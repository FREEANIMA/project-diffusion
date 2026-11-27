import diffusers
print(diffusers.__version__)

names = [n for n in dir(diffusers) if "Autoencoder" in n]
print(names)