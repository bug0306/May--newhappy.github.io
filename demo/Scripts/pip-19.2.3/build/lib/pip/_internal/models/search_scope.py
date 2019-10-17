import itertools
import logging
import os
import posixpath

from pip._vendor.packaging.utils import canonicalize_name
from pip._vendor.six.moves.urllib import parse as urllib_parse

from pip._internal.models.index import PyPI
from pip._internal.utils.compat import HAS_TLS
from pip._internal.utils.misc import normalize_path, redact_password_from_url
from pip._internal.utils.typing import MYPY_CHECK_RUNNING

if MYPY_CHECK_RUNNING:
    from typing import List


logger = logging.getLogger(__name__)


class SearchScope(object):

    """
    Encapsulates the locations that pip is configured to search.
    """

    @classmethod
    def create(
        cls,
        find_links,  # type: List[str]
        index_urls,  # type: List[str]
    ):
        # type: (...) -> SearchScope
        """
        Create a SearchScope object after normalizing the `find_links`.
        """
        # Build find_links. If an argument starts with ~, it may be
        # a local file relative to a home directory. So try normalizing
        # it and if it exists, use the normalized version.
        # This is deliberately conservative - it might be fine just to
        # blindly normalize anything starting with a ~...
        built_find_links = []  # type: List[str]
        for link in find_links:
            if link.startswith('~'):
                new_link = normalize_path(link)
                if os.path.exists(new_link):
                    link = new_link
            built_find_links.append(link)

        # If we don't have TLS enabled, then WARN if anyplace we're looking
        # relies on TLS.
        if not HAS_TLS:
            for link in itertools.chain(index_urls, built_find_links):
                parsed = urllib_parse.urlparse(link)
                if parsed.scheme == 'https':
                    logger.warning(
                        'pip is configured with locations that require '
                        'TLS/SSL, however the ssl module in Python is not '
                        'available.'
                    )
                    break

        return cls(
            find_links=built_find_links,
            index_urls=index_urls,
        )

    def __init__(
        self,
        find_links,  # type: List[str]
        index_urls,  # type: List[str]
    ):
        # type: (...) -> None
        self.find_links = find_links
        self.index_urls = index_urls

    def get_formatted_locations(self):
        # type: () -> str
        lines = []
        if self.index_urls and self.index_urls != [PyPI.simple_url]:
            lines.append(
                'Looking in indexes: {}'.format(', '.join(
                    redact_password_from_url(url) for url in self.index_urls))
            )
        if self.find_links:
            lines.append(
                'Looking in links: {}'.format(', '.join(
                    redact_password_from_url(url) for url in self.find_links))
            )
        return '\n'.join(lines)

    def get_index_urls_locations(self, project_name):
        # type: (str) -> List[str]
        """Returns the locations found via self.index_urls

        Checks the url_name on the main (first in the list) index and
        use this url_name to produce all locations
        """

        def mkurl_pypi_url(url):
            loc = posixpath.join(
                url,
                urllib_parse.quote(canonicalize_name(project_name)))
            # For maximum compatibility with easy_install, ensure the path
            # ends in a trailing slash.  Although this isn't in the spec
            # (and PyPI can handle it without the slash) some other index
            # implementations might break if they relied on easy_install's
            # behavior.
            if not loc.endswith('/'):
                loc = loc + '/'
            return loc

        return [mkurl_pypi_url(url) for url in self.index_urls]
