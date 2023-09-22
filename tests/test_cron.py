from collections import OrderedDict

from cron.cron import Cron


class TestCron:

    def test_all_values_with_valid_cron(self):
        # Given
        cron = "*/15 0 1,15 * 1-5 /usr/bin/find"
        expected = OrderedDict(
            [
                ('minutes', [0, 15, 30, 45]),
                ('hours', [0]),
                ('day_of_month', [1, 15]),
                ('month', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
                ('day_of_week', [1, 2, 3, 4, 5])
            ]
        )

        # When
        c = Cron(cron)
        result = c.results

        # Then
        for field, values in result.items():
            assert values == expected[field]


    def test_all_values_with_valid_complex_cron(self):
        # Given
        cron = "2,3-15/15,*/45,50-59 0-2,4-5,* 1,15 * 1-5/6 rm -rf"
        expected = OrderedDict(
            [
                ('minutes', [0, 2, 3, 45, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]),
                ('hours', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]),
                ('day_of_month', [1, 15]),
                ('month', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
                ('day_of_week', [1])
            ]
        )

        # When
        c = Cron(cron)
        result = c.results

        # Then
        for field, values in result.items():
            assert values == expected[field]
