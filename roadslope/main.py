import parser
import map_match

def load_data(link_data_filename, probe_points_filename):
  links = parser.parse_link_data(link_data_filename)
  nodes = parser.extract_nodes(links)
  probe_points = parser.parse_probe_points(probe_points_filename)
  return (links, nodes, probe_points)

def match_probe_points(links, nodes, probe_points):
  map_match.sort_nodes(nodes)
  nodes_index = map_match.get_nodes_index(nodes)
  map_match.add_matched_link(probe_points, nodes, nodes_index)
  return (links, nodes, probe_points)

def calculate_links_slope(links):
  for link in links:
    link.calculate_slope()
    link.calculate_percent_error_slope()
  return links
