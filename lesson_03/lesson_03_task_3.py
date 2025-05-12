from address import Address
from mailing import Mailing

from_address = Address("555999", "Москва", "Ленина", "55", "99")
to_address = Address("111333", "Санкт-Петербург", "Ленина", "11", "33")

mailing = Mailing(from_address=from_address, to_address=to_address, cost=500, track="Qwer1234")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},"
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment}"
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street},"
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
