from core.components.helper import Helper
from core.components.loader import Loader
from core.components.processor import Processor

loader = Loader('features/dataset.csv')

processor = Processor(loader.get_list())
processor.cast()

start = 0
end = 5
print("===================================")
print("Task1: Display {} sorted records".format(end))

for row in processor.sorted_by_rent_desc()[start: end]:
    print('{row[processor.cn_t_name]} \t\t\t\t{row[processor.cn_c_rent]}')

print("===================================\n")

print("Task2: Create a new list of mast data with 'Lease Years' = 25 years."
      .format(end))

a_list_25 = processor.get_for_lease_eq_25()
for row in a_list_25:
    for column in processor.columns:
        print("{}: {}".format(column, row[column]))

    print(f'------')

print('Total rent for Lease Years = 25 : {}'.
      format(processor.get_total_rent(a_list_25)))
print('------')
print("===================================\n")

print(
    "\nTask 3: Dictionary containing tenant name and a count of masts for "
    "each tenant\n")
for name, nb in processor.get_dict_number_properties_per_tenant().items():
    print("{}: {}".format(name, nb))

print("===================================\n")

print("\nTask 4: Rentals with “Lease Start Date” "
      "between 1 st June 1999 and 31st August 2007\n")

for row in processor.get_list_when_lease_start_date_between('1 Jun 1999',
                                                            '31 Aug 2007'):
    print("Tenant {} with lease started @ {}".format(
        row[processor.cn_t_name],
        Helper.change_date_format(row[processor.cn_l_s_date])))

print("===================================\n")
