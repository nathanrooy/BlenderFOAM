import yaml

def parse_yaml_config_file(yaml_file_path):
	yaml_file = open(yaml_file_path)
	parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)
	print(parsed_yaml_file.items())

	pass
	
	
yaml_file_path = 'blenderFoamDict.yaml'
parse_yaml_config_file(yaml_file_path)


def run_case(configs):

	# load config values from blenderFoamDict

	return
