import argparse
import gettext
import os



# TODO: highlight text that's changed since the last translation update.
#       Goal: only send strings that have changed to the translator.

def main(args=None):
    parser = argparse.ArgumentParser(
        description='i18n hello world')
    parser.add_argument('lang')

    parsed_args = parser.parse_args(args)
    domain = 'messages'
    localedir = os.path.join(os.path.dirname(__file__), 'i18n')
    print(parsed_args)

    # If we're provided with a .mo file, just use that.
    if os.path.exists(parsed_args.lang):
        print(f'Using .mo file at {parsed_args.lang}')
        with open(parsed_args.lang, 'rb') as mo_file:
            gettext.GNUTranslations(mo_file).install()
    else:
        print(f"Loading translation for {parsed_args.lang} from {localedir}")
        gettext.translation(
            domain,
            localedir=localedir,
            fallback=True,  # Use english if lang not found
            languages=[parsed_args.lang]).install()

    # I18N-NOTE: This is the standard greeting.
    print(_("Hello, world!"))


if __name__ == '__main__':
    main()
