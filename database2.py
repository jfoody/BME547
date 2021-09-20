def create_database_entry(patient_name,id_no,age):
	# new_patient = [id_no,age]	#[] creates placeholder for patient info
	patient_dict = {'name': patient_name, 'id_no': id_no, "age": age, 'tests': []}
	return patient_dict

def print_database(db):
	locations = ['room 1','room 2','room 2','room 3']
	for patient, location in zip(db, locations):
		print('{} - {}'.format(patient,location))

def check_age(db,age):
	for ii in db:
		if int(ii[2]) > age:
			print(ii[0], 'is over', age)
		else:
			print(ii[0], 'is not over', age)

def get_patient(db, id_no):
	for patient in db:
		if patient["id_no"] == id_no:
			return patient


def main():
	db = []
	x = create_database_entry("ann ables", 120, 30)
	db.append(x)
	x = create_database_entry('bob',24,31)
	db.append(x)
	x = create_database_entry('chris',33,32)
	db.append(x)
	db.append(create_database_entry('david',14,34))

	patient_id_tested = 24
	test_done = ('HDL',65)

	patient = get_patient(db,patient_id_tested)
	patient["tests"].append(test_done)

	print_database(db)

if __name__ == "__main__":
	main()