import os
import shutil
from copystatic import copy_files_recursive
from gen_content import generate_page, generate_pages_recursive

def delete_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)

if __name__ == "__main__":
    # paths
    dir_path_content = './content'
    dir_path_public = './public'
    template_path = './template.html'

    delete_directory(dir_path_public)

    copy_files_recursive('./static', './public')

    generate_pages_recursive(dir_path_content, template_path, dir_path_public)