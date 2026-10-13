"""
Distributed under the Boost Software License, Version 1.0. (See accompanying

file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

Official repository: https://github.com/cppalliance/wg21-paperflow
"""

from __future__ import annotations

from typing import Any

from tomd.domain.metadata import PaperMetadata
from tomd.lib.metadata_yaml.format import format_front_matter


def _drop_blank(value: Any) -> Any:
    """Return ``value`` without blank content, or None when nothing is left."""
    if isinstance(value, (list, tuple)):
        items = [v for v in value if str(v).strip()]
        return items or None
    if value is None or not str(value).strip():
        return None
    return value


def write_front_matter(metadata: PaperMetadata | dict[str, Any] | None) -> str:
    """Format metadata as YAML front matter via the canonical ``format_front_matter``."""
    if isinstance(metadata, PaperMetadata):
        data = metadata.to_dict()
    elif isinstance(metadata, dict):
        data = dict(metadata)
    else:
        return ""

    cleaned = {k: v for k, v in ((k, _drop_blank(v)) for k, v in data.items()) if v is not None}
    return format_front_matter(cleaned)


__all__ = ["write_front_matter"]
