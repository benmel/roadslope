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
    self.shape_points = self.parse_shape_info(shape_info)
    self.curvature_info = curvature_info
    self.slope_info = slope_info

  def parse_shape_info(self, shape_info):
    shape_points = map(lambda x: x.split('/'), shape_info.split('|'))
    for shape_point in shape_points:
      shape_point[:2] = map(float, shape_point[:2])
      shape_point[2] = float(shape_point[2]) if shape_point[2] else None
    return shape_points
