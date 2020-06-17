import os
import argparse
import yaml

from benderfoam.blenderfoam_utils import run_case

def main():

	# get location of blenderFoamDict
	parser = argparse.ArgumentParser(description='+--- BlenderFOAM ---+')
	parser.add_argument(dest='yaml_path', help='must specify the path of blenderFoamDict.yaml')
	args = parser.parse_args()
	
	# check that blenderFoamDict exists
	assert os.path.exists(args.yaml_path), 'Cannot find blenderFoamDict.yaml based off the specified path...'
	
	# parse case configuration settings
	yaml_file = open(args.yaml_path)
	configs = yaml.load(yaml_file, Loader=yaml.FullLoader)
	print(configs.items())
	
	# begin main event loop
	run_case(configs)
	
	pass
	
	
if __name__ == '__main__':
	main()
