# Prototype Python i18n via stdlib `gettext`

Another natcap project, [OPAL](https://github.com/natcap/opal) used python's
stdlib gettext module to offer translations, which can be a useful resource for
a functioning application.

The goal here is to develop a functional workflow for extracting text strings
from python source and loading them at runtime.

## Process - Initial Translation

1. `gettext.install` installs the `_()` function into the python namespace.
   All text for translation must be marked up with the `_( ... )` function.
   Anything not wrapped by `_()` will not be extracted for translation.
2. Use `pybabel` to build a message catalog template.  This is currently
   written to `gettext-pot/template.pot` and then copied for each language,
   such as `gettext-pot/es.po`.  In Makefile, this is `make pot`
3. Send the `*.po` files to the appropriate translation teams.
4. When translation is complete:
   * Make sure the `fuzzy` tag has been removed.
   * Commit the completed file to `gettext-catalogs`.
5. At compile time, compile the PO files into MO message objects for
   distribution.  In Makefile, this is `make mo`.

To test the rendered translations, try running `python src/application.py
<lang>`, where `lang` is your language code of choice.

## Notes

* Useful definitions for gettext from the [`gawk`
docs](https://www.gnu.org/software/gawk/manual/html_node/Explaining-gettext.html)
* `es_LA` may not be a valid region name.
* The `LC_MESSAGES` directory must exist before the translation files are put
  there.
* When the Message Catalog (POT) file contains a `#, fuzzy` line at the top,
  this indicates that the catalog needs human review because text might have
  changed.  When this line is present, `pybabel` will skip compilation unless
  forced.  Ensure human review and remove the fuzzy tag.
  https://stackoverflow.com/a/12555922/299084

