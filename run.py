from roadslope import main
import datetime

(links, nodes, probe_points) = main.load_data('data/Partition6467LinkData.csv', 'data/Partition6467ProbePoints.csv')
print str(datetime.datetime.now()) + ': Finished loading data'
main.match_probe_points(links, nodes, probe_points)
print str(datetime.datetime.now()) + ': Finished matching probe points'
main.calculate_links_slope(links)
print str(datetime.datetime.now()) + ': Finished calculating links slope'
main.output_links(links, 'data/output_links.csv')
print str(datetime.datetime.now()) + ': Finished outputting links'
main.output_unmatched(probe_points, 'data/output_unmatched.txt')
print str(datetime.datetime.now()) + ': Finished outputting unmatched points'
