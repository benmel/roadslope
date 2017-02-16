import csv
from probe_point import ProbePoint
from link import Link
from node import Node

def parse_probe_points(filename):
  probe_points = []
  with open(filename, 'r') as f:
    csvreader = csv.reader(f)
    for line in csvreader:
      probe_points.append(ProbePoint(*line))
  return probe_points

def parse_link_data(filename):
  links = []
  with open(filename, 'r') as f:
    csvreader = csv.reader(f)
    for line in csvreader:
      links.append(Link(*line))
  return links

def extract_nodes(links):
  nodes = []
  for link in links:
    for shape_point in link.shape_points:
      nodes.append(Node(shape_point[0], shape_point[1], shape_point[2], link))
  return nodes
