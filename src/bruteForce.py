def bruteForceRec(unit_list, trait_set, index):
	if (index == len(unit_list)):
		return 0
	if (unit_list[index].compatible(trait_set)):
		E = trait_set | set(unit_list[index].traits)
		return max(1 + bruteForceRec(unit_list, E, index + 1), bruteForceRec(unit_list, trait_set, index + 1))
	return bruteForceRec(unit_list, trait_set, index + 1)


def bruteForce(unit_list):
	return bruteForceRec(unit_list, set(), 0)
