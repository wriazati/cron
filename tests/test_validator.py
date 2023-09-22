from cron.validator import CronValidator


class TestValidator:

    def test_is_valid_cron_with_valid_cron(self):
        # Given
        cron = '*/15 0 1,15 4 1-5 /usr/bin/find yourmom'

        # When
        result = CronValidator.is_valid(cron)

        # Then
        assert result == True

    def test_is_valid_cron_with_invalid_cron(self):
        # Given
        cron = 'hello world'

        # When
        result = CronValidator.is_valid(cron)

        # Then
        assert result == False

    def test_validate_with_valid_cron(self):
        # Given
        cron = "*/15 0 1,15 4 1-5 /usr/bin/find"

        # When
        result = CronValidator.validate(cron)

        # Then
        expected = ['*/15', '0', '1,15', '4', '1-5', '/usr/bin/find']
        for val, expected_val in zip(result, expected):
            assert val == expected_val

