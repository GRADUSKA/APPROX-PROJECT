def bruteForceRec(unit_list, trait_list, index):
	
	if (index == len(unit_list)):
		return 0
	if (unit_list[index].compatible(trait_list)):
		E = trait_list + unit_list.traits
		return max(1 + bruteForce(unit_list, E, index + 1), bruteForce(unit_list, trait_list, index + 1))
	return bruteForce(unit_list, trait_list, index + 1)


def bruteForce(unit_list):

	return bruteForceRec(unit_list, [], 0)
