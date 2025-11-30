import json

# Read the notebook
with open('basic.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Fix the first cell
if len(notebook['cells']) > 0:
    cell = notebook['cells'][0]
    if cell['cell_type'] == 'code':
        # Replace the source with corrected code
        cell['source'] = [
            "class Student:\n",
            "    def __init__(self, name=\"\"):\n",
            "        self.name = name\n",
            "\n",
            "s1 = Student()\n",
            "\n"
        ]
        # Clear the error output
        cell['outputs'] = []

# Write back
with open('basic.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print("Notebook fixed!")


