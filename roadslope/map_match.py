import math

def add_closest_link_index(probe_points, links):
  for probe_point in probe_points:
    closest_link = find_closest_link(probe_point.latitude, probe_point.longitude, links)
    probe_point.closest_link = closest_link

def find_closest_link(latitude, longitude, links):
  closest_link = None
  closest_distance = float('inf')

  for link in links:
    if abs(latitude - link.shape_points[0][0]) > 0.01 or abs(longitude - link.shape_points[0][1]) > 0.01:
      continue 

    for shape_point in link.shape_points:
      sp_latitude = shape_point[0]
      sp_longitude = shape_point[1]

      distance = math.hypot(sp_longitude - longitude, sp_latitude - latitude)
      if distance < closest_distance:
        closest_link = link
        closest_distance = distance

  return closest_link
