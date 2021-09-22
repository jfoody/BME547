class Patient:

	def __init__(self, name, id_no, age):
		self.name = name
		self.id_no = id_no
		self.age = age
		self.tests = []

# 	def __repr__(self):
# 		return "{}: {}".format(self.id_no, self.name)

# def class_work():
# 	new_patient = Patient("ann ables", 120, 30)
# 	print(new_patient.id_no)
# 	print(new_patient.name)
# 	x = Patient("Bob Boyles", 24, 33)
# 	print(x)


def create_database_entry(patient_name,id_no,age):
	new_patient = Patient(patient_name, id_no, age)
	# new_patient = [id_no,age]	#[] creates placeholder for patient info
	# new_patient = {'name': patient_name, 'id_no': id_no, "age": age, 'tests': []}
	return new_patient

def print_database(db):
	locations = ['room 1','room 2','room 2','room 3']
	for patient, location in zip(db, locations):
		print('{} - {}'.format(patient,location))

def check_age(db,age):
	for patient in db:
		if patient["age"] > age:
			print(ii[0], 'is over', age)
		else:
			print(ii[0], 'is not over', age)

def get_patient(db, id_no):
	patient = db[id_no]
	# for patient in db:
	# 	if patient["id_no"] == id_no:
	# 		return patient


def main():
	# class_work()

	# return

	db = {}
	x = create_database_entry("ann ables", 120, 30)
	db[x.id_no] = x
	x = create_database_entry('bob',24,31)
	db[x.id_no] = x
	x = create_database_entry('chris',33,32)
	db[x.id_no] = x
	x = create_database_entry('david',14,34)
	db[x.id_no] = x
	print(db)

	patient_id_tested = 24
	test_done = ['HDL',65]

	patient = get_patient(db, patient_id_tested)
	patient.tests.append(test_done)
	print(db)

	# print_database(db)

if __name__ == "__main__":
	main()