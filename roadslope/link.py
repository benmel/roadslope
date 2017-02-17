import math

class Link:
  def __init__(self, link_pvid, ref_node_id, nref_node_id, length, functional_class, direction_of_travel, 
    speed_category, from_ref_speed_limit, to_ref_speed_limit, from_ref_num_lanes, to_ref_num_lanes, 
    multi_digitized, urban, time_zone, shape_info, curvature_info, slope_info):
    self.link_pvid = int(link_pvid)
    self.ref_node_id = int(ref_node_id)
    self.nref_node_id = int(nref_node_id)
    self.length = float(length)
    self.functional_class = int(functional_class)
    self.direction_of_travel = direction_of_travel
    self.speed_category = int(speed_category)
    self.from_ref_speed_limit = int(from_ref_speed_limit)
    self.to_ref_speed_limit = int(to_ref_speed_limit)
    self.from_ref_num_lanes = int(from_ref_num_lanes)
    self.to_ref_num_lanes = int(to_ref_num_lanes)
    self.multi_digitized = multi_digitized == 'T'
    self.urban = urban == 'T'
    self.time_zone = float(time_zone)
    self.shape_info = shape_info
    self.shape_points = self.parse_shape_info(shape_info)
    self.curvature_info = curvature_info
    self.slope_info = slope_info
    self.slope_points = self.parse_slope_info(slope_info)
    self.matched_probe_points = []
    self.calculated_slope = None
    self.percent_error_slope = None

  def parse_shape_info(self, shape_info):
    shape_points = map(lambda x: x.split('/'), shape_info.split('|'))
    for shape_point in shape_points:
      shape_point[:2] = map(float, shape_point[:2])
      shape_point[2] = float(shape_point[2]) if shape_point[2] else None
    return shape_points

  def parse_slope_info(self, slope_info):
    slope_points = map(lambda x: x.split('/'), slope_info.split('|'))
    if slope_points[0][0]:
      slope_points = [map(float, slope_point) for slope_point in slope_points]
    else:
      slope_points = None
    return slope_points

  def calculate_slope(self):
    if len(self.matched_probe_points) > 1:
      self.matched_probe_points.sort(key=lambda x: x.latitude)
      start_point = self.matched_probe_points[0]
      end_point = self.matched_probe_points[-1]
      dx = haversine_distance(start_point.latitude, start_point.longitude, end_point.latitude, end_point.longitude)
      dy = end_point.altitude - start_point.altitude
      slope = dy / dx
      self.calculated_slope = math.degrees(math.atan(slope))

  def calculate_percent_error_slope(self):
    if self.slope_points and self.calculated_slope:
      expected_slope = self.slope_points[-1][1]
      if expected_slope != 0:
        self.percent_error_slope = (self.calculated_slope - expected_slope) / expected_slope * 100

  def csv_output(self):
    matched_probe_points_ids_strings = []
    matched_probe_points_info_strings = []
    for point in self.matched_probe_points:
      matched_probe_points_ids_strings.append(str(point.sample_id))
      matched_probe_points_info_strings.append('/'.join(map(str, [point.latitude, point.longitude, point.altitude])))
    matched_probe_points_ids = '|'.join(matched_probe_points_ids_strings)
    matched_probe_points_info = '|'.join(matched_probe_points_info_strings)
    return [self.link_pvid, self.ref_node_id, self.nref_node_id, self.length, self.shape_info, self.slope_info,
            matched_probe_points_ids, matched_probe_points_info, self.calculated_slope, self.percent_error_slope]

def haversine_distance(lat1, lon1, lat2, lon2):
  radius = 6371000
  dLat = math.radians(lat2 - lat1)
  dLon = math.radians(lon2 - lon1)
  lat1 = math.radians(lat1)
  lat2 = math.radians(lat2)

  a = math.sin(dLat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dLon/2)**2
  c = 2 * math.asin(math.sqrt(a))
  return radius * c
