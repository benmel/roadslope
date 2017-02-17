import parser
import map_match
import csv

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

def output_links(links, output_filename):
  with open(output_filename, 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    for link in links:
      writer.writerow(link.csv_output())

def output_unmatched(probe_points, output_filename):
  unmatched = 0
  for probe_point in probe_points:
    if probe_point.matched_link is None:
      unmatched += 1
  with open(output_filename, 'wb') as f:
    f.write('Number of probe points: ' + str(len(probe_points)))
    f.write('\nNumber of unmatched probe points: ' + str(unmatched))
