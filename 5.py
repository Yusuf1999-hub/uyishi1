def are_numbers_ascending(text: str) -> bool:
	new = [int(soz) for soz in text.split() if soz.isdigit()]
	if new:
		son = new[0]
		for num in new[1:]:
			if son>=num:
				return False
			son = num
		return True
	else:
		return False

matn = input()
print(are_numbers_ascending(matn))