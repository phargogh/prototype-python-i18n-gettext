import shutil
import argparse
import gettext
import os

import babel
from babel.messages import frontend



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
        if parsed_args.lang.endswith('.mo'):
            print(f'Using .mo file at {parsed_args.lang}')
            message_object_file = parsed_args.lang
        elif parsed_args.lang.endswith('.po'):
            locale_dir = '.temp-locale'

            locale = os.path.splitext(os.path.basename(parsed_args.lang))[0]

            target_path = os.path.join(locale_dir, locale, 'LC_MESSAGES')
            if not os.path.exists(target_path):
                os.makedirs(target_path)

            frontend.CommandLineInterface().run(
                ["pybabel", "compile",
                    f"--directory={locale_dir}",
                    f"--input-file={parsed_args.lang}",
                    f"--locale={locale}",
                ])
            message_object_file = os.path.join(target_path, f"{locale}.mo")
        else:
            raise Exception(f"Unrecognized behavior for {parsed_args.lang}")

        with open(message_object_file, 'rb') as mo_file:
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
