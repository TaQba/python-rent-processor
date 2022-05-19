import re

from core.components.helper import Helper


class Processor:
    a_list = []
    cn_t_name = 'Tenant Name'
    cn_c_rent = 'Current Rent'
    cn_p_name = 'Property Name'
    cn_u_name = 'Unit Name'
    cn_l_s_date = 'Lease Start Date'
    cn_l_e_date = 'Lease End Date'
    cn_l_years = 'Lease Years'
    cn_add_1 = 'Property Address [1]'
    cn_add_2 = 'Property  Address [2]'
    cn_add_3 = 'Property Address [3]'
    cn_add_4 = 'Property Address [4]'

    columns = (
        cn_p_name,
        cn_add_1, cn_add_2, cn_add_3, cn_add_4,
        cn_u_name,
        cn_t_name,
        cn_l_s_date, cn_l_e_date, cn_l_years,
        cn_c_rent
    )

    def __init__(self, a_list=[]):
        self.a_list = a_list

    def set_list(self, a_list):
        """

        :param a_list:
        :type a_list: list
        """
        self.a_list = a_list

    def get_list(self):
        """
        :rtype: list of dict
        """
        return self.a_list

    def cast(self):
        for idx, row in enumerate(self.a_list):
            # change rent to float
            self.a_list[idx][self.cn_c_rent] = float(row[self.cn_c_rent])

            # change lease years to int
            self.a_list[idx][self.cn_l_years] = int(row[self.cn_l_years])

    def sorted_by_rent_desc(self):
        """
        Name is a bit overkill by is descriptive ;)
        :rtype: list of dict
        """
        desc = True
        return self.__sorted_by_column_name(self.cn_c_rent, desc)

    def get_total_rent(self, the_list):
        return sum(row[self.cn_c_rent] for row in the_list)

    def get_dict_number_properties_per_tenant(self):
        output = {}
        for row in self.a_list:
            name = self.fix_tenant_name(row[self.cn_t_name])
            if name in output:
                output[name] += 1

            else:
                output[name] = 1

        return output

    def get_list_when_lease_start_date_between(self, start_date, end_date):
        """

        :param start_date:
        :type start_date:string
        :param end_date:
        :type end_date: string
        :return:
        :rtype: list
        """
        return [row for row in self.a_list if Helper.between_dates(
            row[self.cn_l_s_date],
            start_date,
            end_date
        )]

    def get_for_lease_eq_25(self):
        """

        :return:
        :rtype: list
        """
        return self.__get_for_column_equal(self.cn_l_years, 25)

    def __get_for_column_equal(self, column, nb):
        """
        DEMO: list comprehension
        :rtype: list of dict
        """
        return [row for row in self.a_list if row[column] == nb]

    def __sorted_by_column_name(self, column, desc):
        """

        :param column:
        :type column: str
        :param desc:
        :type desc: bool
        :return:
        :rtype: list of dict
        """

        if column in self.columns:
            return sorted(self.a_list, key=lambda d: d[column], reverse=desc)
        else:
            raise ValueError('Column name: "{}" does not exist.' .
                             format(column))

    @staticmethod
    def fix_tenant_name(name):
        """

        :rtype: string
        """
        # strip last dot
        name = name.rstrip('.')

        name = re.sub(
            r'(.*)Arqiva(.*)',
            r'Arqiva Ltd',
            name,
            flags=re.I
        )

        name = re.sub(
            r'(.*)Everything(.*)',
            r'Everything Everywhere Ltd & Hutchison 3G UK Ltd',
            name,
            flags=re.I
        )
        return name
