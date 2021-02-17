import argparse
import gettext



# TODO: set language
# TODO: check that provided language is known.
#       warn and fall back to english if not.

def main(args=None):
    parser = argparse.ArgumentParser(
        description='i18n hello world')
    parser.add_argument('lang')

    parsed_args = parser.parse_args(args)
    print(parsed_args)

    print("Hello, world!")


if __name__ == '__main__':
    main()
