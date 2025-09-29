
# import pygraphviz as pgv
# G = pgv.AGraph("./result.dot")

# # Iterate over nodes
# for n in G.nodes():
#     label = n.attr.get("label", "")
#     if "IDENTIFIER" in label:
#         print(n, "=>", label)
# import pydot

# graphs = pydot.graph_from_dot_file("result.dot")
# graph = graphs[0]

# for node in graph.get_nodes():
#     label = node.get_label()
#     if label and "IDENTIFIER" in label:
#         print(label)   # prints only the label, not the numeric ID

import pygraphviz as pgv
import re

# Load the DOT file
G = pgv.AGraph("./result.dot")

functions, blocks, locals_, identifiers, literals, parameters = [], [], [], [], [], []

for n in G.nodes():
    label = n.attr.get("label", "")
    if not label:
        continue
    if "METHOD" in label:
        functions.append(label)
    elif "BLOCK" in label:
        blocks.append(label)
    elif "LOCAL" in label:
        locals_.append(label)
    elif "IDENTIFIER" in label:
        identifiers.append(label)
    elif "LITERAL" in label:
        literals.append(label)
    elif "PARAMETER" in label:
        parameters.append(label)

# Helper to extract the "middle" line (e.g., variable name) from the label
def extract_name(label):
    parts = re.split(r"<BR/>", label)
    if len(parts) >= 2:
        return parts[1].strip()
    return None

print("Functions:", [extract_name(f) for f in functions])
print("Blocks:", len(blocks))
print("Locals:", [extract_name(l) for l in locals_])
print("Identifiers:", [extract_name(i) for i in identifiers])
print("Literals:", [extract_name(l) for l in literals])
print("Parameters:", [extract_name(p) for p in parameters])
