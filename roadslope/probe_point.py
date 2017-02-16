from datetime import datetime

class ProbePoint:
  def __init__(self, sample_id, date_time, source_code, latitude, longitude, altitude, speed, heading):
    self.sample_id = int(sample_id)
    self.date_time = datetime.strptime(date_time, '%m/%d/%Y %H:%M:%S %p')
    self.source_code = int(source_code)
    self.latitude = float(latitude)
    self.longitude = float(longitude)
    self.altitude = int(altitude)
    self.speed = int(speed)
    self.heading = int(heading)
    self.closest_node = None
    self.closest_link = None
