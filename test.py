import os
checkpoint_path = "data\cp.ckpt"

checkpoint_dir = os.path.dirname(checkpoint_path)
if not os.path.exists(checkpoint_dir):
    print("Directory does not exist")