from jinja2 import Template
from minimal_molview.templates.resources import HTML_TEMPLATE

def render(pdb):
    with open(pdb, "rt") as fin:
        # read the pdb file
        pdb_data = fin.read()
    data = {
        "PDB_INSERT": pdb_data,
    }
    # render the template with Jinja
    template_str = open(HTML_TEMPLATE).read()
    template = Template(template_str)
    with open("render.html", "wt") as fout:
        fout.write(template.render(data))

if __name__ == "__main__":
    pdb = "7vxy.pdb"
    render(pdb)