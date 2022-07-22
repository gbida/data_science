"""python module for handling csv files with open() and csv.reader()"""

import csv


def load(file, encoding='utf-8'):
	f = open(file, mode='r', encoding=encoding)
	data = csv.reader(f)
	return data


def shape(data):
	for row in data:
		return len(data), len(row)


def head(data, n=3):
	i = 0
	for row in data:
		if i >= 3: break
		print(row)
		i += 1


def toint(data):
	for row in data:
		for i in range(len(row)):
			if isinstance(row[i], str):
				row[i] = int(row[i])
	return data


def rmcomma(data):
	for row in data:
		for i in range(len(row)):
			if ',' in row[i]:
				row[i] = row[i].replace(',', '')
	return data
