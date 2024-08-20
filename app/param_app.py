from typing import Optional
from pydantic import Field
from typing_extensions import Annotated


sql_to_pydantics = {
    "url": Optional[str],
    "id_name": Optional[str],
    "valor": Optional[int],
    "moneda": Optional[str],
    "gastos_comunes": Optional[float],
    "sup_total": Optional[float],
    "sup_terraza": Optional[float],
    "sup_util": Optional[float],
    "dormitorios": Optional[float],
    "banos": Optional[float],
    "estacionamiento": Optional[float],
    "bodega": Optional[float],
    "ambientes": Optional[float],
    "piso_unidad": Optional[float],
    "tot_pisos": Optional[float],
    "dept_x_piso": Optional[float],
    "antiguedad": Optional[float],
    "tipo_depa": Optional[str],
    "orientacion": Optional[str],
    "vendedor": Optional[str],
    "calle": Optional[str],
    "barrio": Optional[str],
    "comuna": Optional[str],
    "ciudad": Optional[str],
    "direccion": Optional[str],
    "fecha_scrap": Optional[str],
    "descripcion": Optional[str],
    "id_publicacion": Optional[str],
    "quality_scrap": Optional[float],
    "gusto": Optional[int]
}
