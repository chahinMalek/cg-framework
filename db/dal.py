from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.cast import cast_triangulation, cast_polygon
from db.db_conf import DB_URI
from db.models import Polygon

from structures.polygon import Polygon as STPolygon
from structures.triangle import Triangle as STTriangle

engine = create_engine(DB_URI)


DBSession = sessionmaker(bind=engine)
session = DBSession()


def save_triangulations(db_session: DBSession, polygon: STPolygon,
                        triangulations: List[List[STTriangle]]) -> Polygon:

    polygon = cast_polygon(polygon)

    for triangulation in triangulations:
        polygon.triangulations.append(cast_triangulation(triangulation))

    db_session.add(polygon)
    db_session.commit()
    return polygon
