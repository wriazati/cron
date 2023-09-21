from cron.validator import CronValidator


class TestValidator:


    def test_is_valid_cron_with_valid_cron(self):
        '''
        Sanity check against known calculator result
        '''
        # Given
        cron = '*/15 0 1,15 4 1-5 /usr/bin/find yourmom'

        # When
        result = CronValidator.is_valid(cron)

        # Then
        assert result == True

    def test_is_valid_cron_with_invalid_cron(self):
        '''
        Sanity check against known calculator result
        '''
        # Given
        cron = 'hello world'

        # When
        result = CronValidator.is_valid(cron)

        # Then
        assert result == False

