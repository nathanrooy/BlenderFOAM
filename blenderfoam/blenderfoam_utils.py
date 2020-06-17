from scipy.optimize import minimize


def run_case(configs):

	# load initial values
	x0 = 'something'

	# initialize optimizer
	res = minimize(cost_func, x0, method=configs['optimizer']['name'])
	
	
	return
	
		
def cost_function(configs):

	# apply mesh deformation and save new geometry
	
	# prepare new openfoam iteration

	# run openfoam
	
	# collect results
	
	return cost
