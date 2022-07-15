male_count = 0
female_count = 0

with open('input_files/employees.prn') as file_object:
	#contents = file_object.read()
	#print(contents)
	for l in file_object:

		if l[8:14] == "Female":
			female_count += 1

		if l[8:12] == "Male":
			male_count += 1

print(f"Females : {female_count}")
print(f"Males   : {male_count}")

