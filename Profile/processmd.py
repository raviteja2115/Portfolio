import markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

class CodeBlockWrapper(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(CodeBlockPreprocessor(md), 'code-block', 10)

class CodeBlockPreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        copy_button = '<button class="btn btn-sm btn-secondary float-right copy-btn" onclick="copyCode(this)">Copy</button>'

        in_code_block = False
        for line in lines:
            if line.strip().startswith("```"):
                if not in_code_block:
                    line = '<div class="card mb-3"><div class="card-body"><code>'
                    in_code_block = True
                else:
                    line = f"</code>{copy_button}</div></div>"
                    in_code_block = False
            new_lines.append(line)
        return new_lines

def convert_md_to_html(md_file, html_file):
    with open(md_file, 'r') as f:
        md_content = f.read()

    md = markdown.Markdown(extensions=[CodeBlockWrapper()])
    html_content = md.convert(md_content)

    # Wrap HTML content in Bootstrap table
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <table class="table table-bordered">
                <tbody>
                    <tr>
                        <td>{html_content}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <script>
            function copyCode(button) {{
                var code = button.parentNode.querySelector('code').innerText;
                navigator.clipboard.writeText(code);
            }}
        </script>
    </body>
    </html>
    """

    with open(html_file, 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    md_file = "./Gun_Violence_Data_Statistical_Analysis.md"
    html_file = "./census.html"
    convert_md_to_html(md_file, html_file)
