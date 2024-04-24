from nbconvert import HTMLExporter
from nbformat import read
import io

# Specify the path to the notebook file
notebook_file = './Crime_Data_Visualization.ipynb'

# Read the notebook file
with open(notebook_file, 'r', encoding='utf-8') as f:
    notebook_content = f.read()

# Load the notebook content
notebook_node = read(io.StringIO(notebook_content), as_version=4)

# Create an HTML exporter
html_exporter = HTMLExporter()

# Convert the notebook to HTML
html_output, resources = html_exporter.from_notebook_node(notebook_node)

# Save the HTML output to a file
with open('Crime_Data_Visualization', 'w', encoding='utf-8') as f:
    f.write(html_output)
