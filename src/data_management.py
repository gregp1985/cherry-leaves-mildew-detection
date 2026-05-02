import os


def load_image_paths(folder_path):
    """
    Returns a list of image file paths from a given folder.
    """
    files = []
    for file in os.listdir(folder_path):
        files.append(os.path.join(folder_path, file))
    return files