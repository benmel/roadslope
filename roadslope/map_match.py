import math

nodes_latitude_step = 0.01

def floor_two_decimals(value):
  return math.floor(value * 100.0) / 100.0

def sort_nodes(nodes):
  nodes.sort(key=lambda x: x.latitude)

def get_nodes_index(nodes):
  min_node_latitude = nodes[0].latitude
  node_lower = floor_two_decimals(min_node_latitude)

  nodes_index = {node_lower: 0}
  next_index = node_lower + nodes_latitude_step

  for idx, node in enumerate(nodes):
    if node.latitude >= next_index:
      current_index = floor_two_decimals(node.latitude)
      nodes_index[current_index] = idx
      next_index = current_index + nodes_latitude_step

  return nodes_index

def add_closest_link(probe_points, nodes, nodes_index):
  for probe_point in probe_points:
    closest_node = find_closest_node(probe_point.latitude, probe_point.longitude, nodes, nodes_index)
    if closest_node:
      probe_point.closest_node = closest_node
      probe_point.closest_link = closest_node.link

def find_closest_node(latitude, longitude, nodes, nodes_index):
  closest_node = None
  closest_distance = float('inf')

  latitude_index = floor_two_decimals(latitude)
  start_latitude_index = round(latitude_index - nodes_latitude_step, 2)
  end_latitude_index = round(latitude_index + 2*nodes_latitude_step, 2)

  start_nodes_index = nodes_index.get(start_latitude_index, 0)
  end_nodes_index = nodes_index.get(end_latitude_index, len(nodes))

  for i in range(start_nodes_index, end_nodes_index):
    node = nodes[i]

    if abs(longitude - node.longitude) > 0.01:
      continue

    distance = math.hypot(node.longitude - longitude, node.latitude - latitude)
    if distance < closest_distance:
      closest_node = node
      closest_distance = distance

  return closest_node
