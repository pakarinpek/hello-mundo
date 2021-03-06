"""Code for dealing with subversion layouts

This package is intended to encapsulate everything about subversion
layouts.  This includes detecting the layout based on looking at
subversion, mapping subversion paths to hg branches, and doing any
other path translation necessary.

NB: this has a long way to go before it does everything it claims to

"""

from mercurial import util as hgutil

import custom
import single
import standard

__all__ = [
    "layout_from_name",
    ]

# This is the authoritative store of what layouts are available.
# The intention is for extension authors who wish to build their own
# layout to add it to this dict.
NAME_TO_CLASS = {
    "custom": custom.CustomLayout,
    "single": single.SingleLayout,
    "standard": standard.StandardLayout,
}


def layout_from_name(name, meta):
    """Returns a layout module given the layout name

    You should be able to read the layout name from meta.layout but, if
    necessary, you can use one of the meta.layout_from_* functions to get the
    name to pass to this function.

    """

    if name not in NAME_TO_CLASS:
        raise hgutil.Abort('Unknown hgsubversion layout: %s' % name)
    return NAME_TO_CLASS[name](meta)
