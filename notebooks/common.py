FIGURE_FOLDER = '../figures'
DATA_FOLDER = '../data'


cluster_id_to_name = {24: 'Rods', 25: 'Cones', 26: 'Bipolar cells (group1)',
                      27: 'Bipolar cells (group2)',
                      33: 'Bipolar cells (group3)', 34: 'Muller glia'}
cluster_name_to_ids = {'Horizontal cells': 1, 'Retinal ganglion cells': 2,
                       'Amacrine cells': range(3, 24), "Rods": 24,
                       'Cones': 25, 'Bipolar cells': range(26, 34),
                       'Muller glia': 34, 'Astrocytes': 35,
                       'Fibroblasts': 36, 'Vascular endothelium': 37,
                       'Pericytes': 38, 'Microglia': 39}
