from collections import OrderedDict
from typing import List

from cron.validator import CronValidator

TIME_RULES = OrderedDict([
    ('minutes', (0, 59)),
    ('hours', (0, 23)),
    ('day_of_month', (1, 31)),
    ('month', (1, 12)),
    ('day_of_week', (0, 6)),
])

class Cron():
    def __init__(self, cron_expression):
        self.cron = CronValidator.validate(cron_expression)
        self.results = OrderedDict()

        for field, user_value in zip(TIME_RULES, self.cron):
            field_bounds = TIME_RULES[field]
            self.results[field] = self.all_values(field, field_bounds, user_value)

    def all_values(self, field, field_bounds, user_values) -> List[str]:
        """
        :param field: Name of cron field
        :param field_bounds: Valid start and end bounds for the field
        :param user_values: User input for that field
        :return: valid values with that match bounds
        """
        results = set()

        for user_val in user_values.split(','):

            if user_val.isdigit():
                results.add(int(user_val))
            else:

                start_range, end_range = field_bounds
                iteration_step = 1

                if '/' in user_val:
                    parts = user_val.split('/')
                    start_range, end_range = self._get_range(parts[0], field_bounds)
                    iteration_step = int(parts[1])
                elif '-' in user_val:
                    start_range, end_range = self._get_range(user_val, field_bounds)

                for i in range(start_range, end_range + 1, iteration_step):
                    results.add(i)

        return sorted(list(results))

    def _get_range(self, string, bounds) -> (int, int):

        if string == '*':
            return bounds[0], bounds[1]

        if string.isdigit():
            return int(string), bounds[1]

        if '-' in string:
            c = string.split('-')
            return int(c[0]), int(c[1])

        raise Exception("_get_range: ", string, bounds)

    def _format_results_numbers(self, l: List[str]):
        b = []
        for num in l:
            b.append(str(num))

        return ' '.join(b)

    def __str__(self):
        builder = []

        # Find the maximum length of field names for formatting
        max_field_length = max(len(field) for field in TIME_RULES)

        for field in TIME_RULES:
            results_string = self._format_results_numbers(self.results[field])
            s = f"{field:{max_field_length}}\t{results_string}"
            builder.append(s)
        builder.append(f"command         {self.cron[-1]}")

        return '\n'.join(builder)


    
