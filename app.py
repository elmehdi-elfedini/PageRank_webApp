from flask import Flask, render_template, request 
import networkx as nx
import xml.etree.ElementTree as ET

app = Flask(__name__)


@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/home")
def upload():
    return render_template('upload.html')

def is_xml_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'xml'


def read_graph_from_xml(file_data):
    graph = nx.DiGraph()
    nodes = []
    edges = []
    root = ET.fromstring(file_data)
    for node_elem in root.findall('node'):
        node_name = node_elem.get('name')
        nodes.append({'id': node_name, 'label': f'Node {node_name}'})
        for neighbor_elem in node_elem.find('neighbors'):
            neighbor_name = neighbor_elem.text
            edges.append({'from': node_name, 'to': neighbor_name})
            graph.add_edge(node_name, neighbor_name)

    return graph, nodes, edges



@app.route("/", methods=["GET", "POST"])
def upload_xml():
    if request.method == "POST":
        if "file" in request.files:
            file = request.files["file"]
            if file.filename == "":
                return "No selected file"
                return redirect(url_for("upload"))

            if not is_xml_file(file.filename):
                return "Please select a valid XML file"
                return redirect(url_for("upload"))

            if file:
                xml_data = file.read()
                graph, nodes, edges = read_graph_from_xml(xml_data)
                #pour calculer pagerank
                pagerank = nx.pagerank(graph, alpha=0.85)
                return render_template("result.html", nodes=nodes, edges=edges, pagerank=pagerank)

    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)
