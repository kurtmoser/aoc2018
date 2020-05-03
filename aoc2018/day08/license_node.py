class LicenseNode():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.metadata = []
        self.node_length = 2

        child_count = data[0]
        metadata_count = data[1]

        for i in range(child_count):
            child = self.get_child(self.node_length)
            self.children.append(child)
            self.node_length += child.node_length

        self.node_length += metadata_count
        self.metadata = self.data[(self.node_length - metadata_count):self.node_length]

    def get_child(self, child_node_start):
        return LicenseNode(self.data[child_node_start:])

    def get_cumulative_metadata_sum(self):
        metadata_sum = 0

        for child in self.children:
            metadata_sum += child.get_cumulative_metadata_sum()

        metadata_sum += sum(self.metadata)

        return metadata_sum

    def get_complex_metadata_sum(self):
        metadata_sum = 0

        if not self.children:
            metadata_sum = sum(self.metadata)
        else:
            for i in self.metadata:
                if i > 0 and i <= len(self.children):
                    metadata_sum += self.children[i - 1].get_complex_metadata_sum()

        return metadata_sum
