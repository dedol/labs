import random


class Medic():
    """
    Работник больницы - посетитель
    """

    def visit_patient(self, patient):
        # Посетить пациента
        pass


class Patient():
    """
    Пациент (конкретный человек)
    """

    def __init__(self, name):
        self.name = name
        self.temperature = "не измерена"
        self.analyzes = "не сданы"
        self.diagnosis = "не поставлен"

    def __str__(self):
        return (f"Пациент: {self.name}\n" +
            f"\t\tТемпература тела: {self.temperature}\n" +
            f"\t\tРезультаты анализов: {self.analyzes}\n" + 
            f"\t\tДиагноз: {self.diagnosis}")

    def measure_temperature(self):
        self.temperature = round(random.uniform(36, 39), 1)
        print(f"\t\tИзмерили температуру: {self.temperature}")

    def get_analyzes(self):
        self.analyzes = random.choice(["хорошие", "плохие"])
        print(f"\t\tВзяли анализы: {self.analyzes}")

    def accept(self, medic=Medic):
        print(f"\tПациент: {self.name}")
        medic.visit_patient(self)


class Hospital_ward():
    """
    Палата, в которой находятся пациенты
    """

    def __init__(self, ward_num, patient_names):
        self.ward_num = ward_num
        self.patients = []
        for name in patient_names:
            self.patients.append(Patient(name))

    def __str__(self):
        result = f"Палата №{self.ward_num}\n"
        for patient in self.patients:
            result += "\t" + str(patient) + "\n"
        return result[:-1]

    def accept(self, medic=Medic):
        print(f"Палата №{self.ward_num}")
        for patient in self.patients:
            patient.accept(medic)


class Nurse(Medic):
    """
    Медсестра, конктретный работник больницы
    """

    # Что именно должна делать медсестра при посещении пациента
    def visit_patient(self, patient=Patient):
        patient.measure_temperature()
        patient.get_analyzes()


class Doctor(Medic):
    """
    Врач, тоже конктретный работник больницы
    """

    # А врач должен только поставить диагноз
    def visit_patient(self, patient=Patient):
        if patient.temperature <= 37.5 and patient.analyzes == "плохие":
            patient.diagnosis = "Отравление"
        elif patient.temperature <= 37.5 and patient.analyzes == "хорошие":
            patient.diagnosis = "Переутомление"
        elif patient.temperature > 37.5 and patient.analyzes == "плохие":
            patient.diagnosis = "Коронавирус"
        elif patient.temperature > 37.5 and patient.analyzes == "хорошие":
            patient.diagnosis = "Простуда"
        else:
            patient.diagnosis = "не удается поставить"
        print(f"\t\tПоставили анализ: {patient.diagnosis}")


class WardLooper():
    """
    Итератор, проходящий по списку палат
    """

    def __init__(self, collection=[]):
        self.collection = collection
        self.cursor = 0

    def current(self):
        if self.cursor < len(self.collection):
            return self.collection[self.cursor]

    def next(self):
        if len(self.collection) >= self.cursor + 1:
            self.cursor += 1

    def has_next(self):
        has = len(self.collection) >= self.cursor + 1
        if not has: self.cursor = 0
        return has

    def add(self, item):
        self.collection.append(item)


if __name__ == '__main__':
    wards = WardLooper()
    wards.add(Hospital_ward(1, ["Иванов Михаил", "Смирнов Максим"]))
    wards.add(Hospital_ward(2, ["Кузнецов Артем", "Попов Марк"]))

    print("--- Начальное состояние ---")
    while wards.has_next():
        print(str(wards.current()))
        wards.next()

    print("\n\n--- Обход палат медсестрой ---")
    nurse = Nurse()
    while wards.has_next():
        wards.current().accept(nurse)
        wards.next()

    print("\n\n--- Обход палат врачем ---")
    doc = Doctor()
    while wards.has_next():
        wards.current().accept(doc)
        wards.next()

    print("\n\n--- Конечное состояние ---")
    while wards.has_next():
        print(str(wards.current()))
        wards.next()
