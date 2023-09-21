import argparse

from cron.cron import Cron
from cron.validator import CronValidator


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Cron scheduler')
    parser.add_argument('--cron', type=str, help='Add your cron job here.')
    parser.add_argument('--example', default=False, help='Examle CRON: */15 0 1,15 * 1-5 /usr/bin/find')
    parser.add_argument('--verbose', default=False, help='Show info messages.')
    args = parser.parse_args()

    # Check if the --show-help argument is provided
    if args.example:
        parser.print_help()
    else:
        # Access the mandatory cron_expression argument
        cron_expression = args.cron

        # Access the optional verbose argument
        verbosity_level = args.verbose

        cv = CronValidator()
        c = Cron("*/15 0 1,15 * 1-5 /usr/bin/find")
        print(c)




if __name__ == '__main__':
    main()
