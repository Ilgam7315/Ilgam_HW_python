from smartphone import Smartphone

catalog = [
    Smartphone("iPhone", "16 Pro Max", "+7909 000 00 01"),
    Smartphone("Sony", "Xperia 1", "+7909 000 00 02"),
    Smartphone("Siemens", "A31", "+7909 000 00 03"),
    Smartphone("Samsung", "S25", "+7909 000 00 04"),
    Smartphone("HUAWEI", "Mate XT", "+7909 000 00 05")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
