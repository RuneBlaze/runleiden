import typer
import leidenalg as la
from igraph import Graph
from enum import Enum

class Quality(str, Enum):
    cpm = "cpm"
    modularity = "mod"

def main(
    input: str = typer.Option(..., "--input", "-i"),
    quality: Quality = typer.Option(Quality.cpm, "--quality", "-q"),
    resolution: float = typer.Option(1.0, "--gamma", "-r"),
    output: str = typer.Option(..., "--output", "-o"),
):
    g = Graph.Load(input, format='edgelist', directed=False)
    print(g.summary())
    parter = la.CPMVertexPartition if quality == Quality.cpm else la.ModularityVertexPartition
    partition = la.find_partition(
        g, parter, resolution_parameter=resolution
    )
    print(len(partition))
    return
    with open(output, "w+") as fh:
        for i in range(len(partition)):
            nodes = partition[i]
            for n in nodes:
                fh.write(f"{n} {i}\n")

def entry_point():
    typer.run(main)

if __name__ == '__main__':
    entry_point()