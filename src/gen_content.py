import os
from markdown_blocks import markdown_to_html_node



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    page_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(page_content)
        
        
def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        line = line.strip()  
        if line.startswith("# "):  
            return line[2:].strip()  
    raise ValueError("No H1 header found")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            
            if file.endswith(".md"):
                
                md_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(md_file_path, dir_path_content)
                html_file_name = relative_path.replace(".md", ".html")

                html_file_path = os.path.join(dest_dir_path, html_file_name)
                os.makedirs(os.path.dirname(html_file_path), exist_ok=True)

                print(f"Generating page from {md_file_path} to {html_file_path}")
                generate_page(md_file_path, template_path, html_file_path)