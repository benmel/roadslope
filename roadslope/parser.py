import csv
from probe_point import ProbePoint
from link import Link

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
