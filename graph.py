class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_relasi(self, asal, tujuan):

        if asal not in self.graph:
            self.graph[asal] = []

        self.graph[asal].append(tujuan)

    def tampilkan_graph(self):
        for key, value in self.graph.items():
            print(f"{key} -> {value}")