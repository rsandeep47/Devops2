import markdown

def convert_md_to_html(md_file, html_file):
    with open(md_file, 'r', encoding='utf-8') as md_input:
        md_content = md_input.read()
        html_content = markdown.markdown(md_content)
        with open(html_file, 'w', encoding='utf-8') as html_output:
            html_output.write(html_content)

if __name__ == "__main__":
    convert_md_to_html("README.md", "README.html")
