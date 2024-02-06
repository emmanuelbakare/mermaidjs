# run this code in the first Jupyer notebook cell
# make sure you have imported all the necessary module e.g. pip install matplotlib to import matplotlib module
import base64
from IPython.display import Image, display
import matplotlib.pyplot as plt

def drawm(graph):
    graphbytes = graph.encode("utf8")
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")
    display(Image(url="https://mermaid.ink/img/" + base64_string))

# Write your mermaid.js code in subsequent cells in your Jupyter notebook
# remember to add the semi-colon at the back of every statement
drawm("""
graph LR;
    A--> B & C & D;
    B--> A & E;    
""")