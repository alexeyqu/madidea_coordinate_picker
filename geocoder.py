import re

regexes = [
	(r'((-?[\d]+)(,|.)([\d]+))\s*(,|;)?\s*((-?[\d]+)(,|.)([\d]+))', 1, 6)
]

def get_coords(text):
	text = text.replace('\r', '')
	print(text)
	data = []
	for regex, group_1, group_2 in regexes:
		seq = re.compile(regex, re.MULTILINE)
		for match in re.finditer(seq, text):
			span = {}
			text_start, text_finish = match.span()
			span['text_start'] = text_start
			span['text_finish'] = text_finish
			span['lat'] = match.group(group_1)
			span['lon'] = match.group(group_2)
			data.append(span)
	return data


if __name__ == '__main__':
	print(get_coords('dsai 56.28282455 58.01387928 djaiso'))