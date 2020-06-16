import argparse
import yaml

def main():
	# get location of blenderFoamDict
	parser = argparse.ArgumentParser(description='+--- BlenderFOAM ---+')
	parser.add_argument(dest='yaml_path', help='must specify the path of blenderFoamDict.yaml')
	args = parser.parse_args()

	print(args)
	
	# parse case configuration settings
	#yaml_file = open(yaml_file_path)
	#parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)
	#print(parsed_yaml_file.items())

	return None
	
	
	
	
if __name__ == '__main__':
	main()
