import re
from collections import OrderedDict
from typing import List

from cron.exceptions import InvalidNumberOfArgumentsException, IllegalCharacterException, ValueOutOfBoundsException, \
    ValidationException

LEGAL_CHAR_PATTERN = r'^[0-9/*,\-]+$'
SPECIAL_CHAR_PATTERN = r'[,*/-]'

TIME_RULES = OrderedDict([
    ('minutes', (0, 59)),
    ('hours', (0, 23)),
    ('day_of_month', (1, 31)),
    ('month', (1, 12)),
    ('day_of_week', (0, 6)),
])

COMMAND_INDEX = len(TIME_RULES.keys())  # command at the end


class CronValidator:

    @staticmethod
    def is_valid(cron: str) -> bool:
        """
        Function to determine if the given cron string is valid.

        :param cron: string representing a cron expression
        :return: boolean if it is valid or not

        */15 0 1,15 * 1-5 /usr/bin/find
        """
        try:
            CronValidator.validate(cron)
        except ValidationException:
            return False
        return True


    @staticmethod
    def validate(cron: str) -> List[str]:
        """
        Function to validate values in cron. Will raise an exception if malformed.

        :param cron: string representing a cron expression
        :return: List of components in cron
        """

        components = CronValidator._split_into_components(cron)
        components = CronValidator._verify_values(components)
        return components


    @staticmethod
    def _split_into_components(cron: str) -> List[str]:
        components = cron.split(' ')
        command_index = COMMAND_INDEX

        # Join all command arguments together
        if len(components) > command_index + 1:
            components[command_index] = ' '.join(components[command_index:])
            components = components[:command_index + 1]
        if len(components) != command_index + 1:
            raise InvalidNumberOfArgumentsException(cron)

        return components

    @staticmethod
    def _verify_values(components: List[str]) -> List[str]:

        for field, user_value in zip(TIME_RULES, components):
            field_bounds = TIME_RULES[field]

            # Check for people using random chars like ?&$%
            if not re.match(LEGAL_CHAR_PATTERN, user_value):
                raise IllegalCharacterException(user_value)

            # Check for people setting month=14 instead of in bound: (1-12)
            for val in re.split(SPECIAL_CHAR_PATTERN, user_value):
                if len(val) > 0 and (int(val) < field_bounds[0] or int(val) > field_bounds[1]):
                    # TODO: Check for order in user_values containing 2 different integers
                    raise ValueOutOfBoundsException(field_bounds, user_value)

        return components

