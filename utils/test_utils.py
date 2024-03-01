import numpy as np
import glob
import os
def find_local_idx(path, ext):
    """
    Find the local index of the last file in the directory
    """

    files = glob.glob(os.path.join(path, f'*.{ext}'))
    if not files:
        return 0
    
    files = [os.path.basename(file) for file in files]
    files = [os.path.splitext(file)[0] for file in files]

    return int(sorted(files)[-1].lstrip('0'))

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_hspace(save_location, name, h_space):

    os.makedirs(save_location, exist_ok=True)
    h_space = h_space.cpu().detach().numpy()
    np.save(os.path.join(save_location, f'{name}.npy'), h_space)
