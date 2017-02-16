import math

links_latitude_step = 0.01

def sort_links(links):
  links.sort(key=lambda x: x.shape_points[0][0])

def get_links_index(links):
  min_link_latitude = links[0].shape_points[0][0]
  link_lower = floor_two_decimals(min_link_latitude)

  links_index = {link_lower: 0}
  next_index = link_lower + links_latitude_step

  for idx, link in enumerate(links):
    latitude = link.shape_points[0][0]
    if latitude >= next_index:
      current_index = floor_two_decimals(latitude)
      links_index[current_index] = idx
      next_index = current_index + links_latitude_step

  return links_index

def floor_two_decimals(value):
  return math.floor(value * 100.0) / 100.0

def add_closest_link_index(probe_points, links, links_index):
  for probe_point in probe_points:
    closest_link = find_closest_link(probe_point.latitude, probe_point.longitude, links, links_index)
    probe_point.closest_link = closest_link

def find_closest_link(latitude, longitude, links, links_index):
  closest_link = None
  closest_distance = float('inf')

  latitude_index = floor_two_decimals(latitude)
  start_latitude_index = round(latitude_index - links_latitude_step, 2)
  end_latitude_index = round(latitude_index + 2*links_latitude_step, 2)

  start_links_index = links_index.get(start_latitude_index, 0)
  end_links_index = links_index.get(end_latitude_index, len(links))

  for i in range(start_links_index, end_links_index):
    link = links[i]

    if abs(longitude - link.shape_points[0][1]) > 0.01:
      continue

    for shape_point in link.shape_points:
      sp_latitude = shape_point[0]
      sp_longitude = shape_point[1]

      distance = math.hypot(sp_longitude - longitude, sp_latitude - latitude)
      if distance < closest_distance:
        closest_link = link
        closest_distance = distance

  return closest_link
