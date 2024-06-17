import argparse
from jinja2 import Template
from pathlib import Path

from minimal_molview.templates.resources import HTML_TEMPLATE

def render(pdb_file, output_file):
    with open(pdb_file, "rt") as fin:
        # read the pdb file
        pdb_data = fin.read()
    
    data = {
        "PDB_INSERT": pdb_data,
    }
    
    # render the template with Jinja
    template_str = open(HTML_TEMPLATE).read()
    template = Template(template_str)
    
    if output_file is None:
        # take stem of pdb_file and append .html
        output_file = Path(pdb_file).stem + ".html"
        
    with open(output_file, "wt") as fout:
        fout.write(template.render(data))
    
    print(f"Rendered HTML saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Render PDB file into HTML using Jinja2 template.")
    parser.add_argument("pdb_file", type=str, help="Input PDB file")
    parser.add_argument("-o", "--output", type=str, default=None,
                        help="Output HTML file (default: render.html)")
    args = parser.parse_args()
    render(args.pdb_file, args.output)

if __name__ == "__main__":
    main()
