import sys
import getopt
import time

from LabBrick.core import Attenuator

def attenuation_response(device, status_byte, count, byteblock):
	print device.attenuation_level
	
if __name__ == '__main__':

	try:
		opts, args = getopt.getopt(sys.argv[1:], "hv:p:", ["help", "vid=", "pid="])
	except getopt.GetoptError as err:
		# print help information and exit:
		print str(err)  # will print something like "option -a not recognized"
		usage()
		sys.exit(2)
		
	vid = -1
	pid = -1
		
	for o, a in opts:
		if o in ("-h", "--help"):
			usage()
			sys.exit()
		elif o in ("-v", "--vid"):
			vid = a
		elif o in ("-p", "--pid"):
			pid = a
			
	if vid == -1 or pid == -1:
		usage()
		sys.exit()
	else:
		try:
			vid = int(vid, 0)
			pid = int(pid, 0)
		except:
			usage()

		att = Attenuator(vid = vid, pid = pid, debug=True)
		
		print att.serial
		
		att.get_attenuation(debug=True)
		
		att.set_attenuation(5, debug=True)

	while 1:
		att.set_attenuation(5, debug=True)
		time.sleep(10)
		att.set_attenuation(10, debug=True)
		time.sleep(10)
