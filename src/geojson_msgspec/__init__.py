from __future__ import annotations

from typing import List, Optional, Tuple, Union

import msgspec

Position = Tuple[float, float]


# Define the 7 standard Geometry types.
# All types set `tag=True`, meaning that they'll make use of a `type` field to
# disambiguate between types when decoding.
class Point(msgspec.Struct, tag=True):  # type: ignore[call-arg]
    coordinates: Position


class MultiPoint(msgspec.Struct, tag=True):  # type: ignore[call-arg]
    coordinates: List[Position]


class LineString(msgspec.Struct, tag=True):  # type: ignore[call-arg]
    coordinates: List[Position]


class MultiLineString(msgspec.Struct, tag=True):  # type: ignore[call-arg]
    coordinates: List[List[Position]]


class Polygon(msgspec.Struct, tag=True):  # type: ignore[call-arg]
    coordinates: List[List[Position]]


class MultiPolygon(msgspec.Struct, tag=True):  # type: ignore[call-arg]
    coordinates: List[List[List[Position]]]


class GeometryCollection(msgspec.Struct, tag=True):  # type: ignore[call-arg]
    geometries: List[Geometry]


Geometry = Union[
    Point,
    MultiPoint,
    LineString,
    MultiLineString,
    Polygon,
    MultiPolygon,
    GeometryCollection,
]


# Define the two Feature types
class Feature(msgspec.Struct, tag=True):  # type: ignore[call-arg]
    geometry: Optional[Geometry] = None
    properties: Optional[dict] = None
    id: Union[str, int, None] = None


class FeatureCollection(msgspec.Struct, tag=True):  # type: ignore[call-arg]
    features: List[Feature]


# A union of all 9 GeoJSON types
GeoJSON = Union[Geometry, Feature, FeatureCollection]


# Create a decoder and an encoder to use for decoding & encoding GeoJSON types
loads = msgspec.json.Decoder(GeoJSON).decode
dumps = msgspec.json.Encoder().encode
