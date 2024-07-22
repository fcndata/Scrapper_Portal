import numpy as np

orientation_types={'N':['norte','n'],
'NO':['nor-oriente','nor-orienteff','nororiente','no','on'],
'NP':['norponiente','nor-poniente','np','pn'],
'S':['sur','s'],
'SO':['sur-oriente','oriente sur','so','os'],
'SP':['sur-poniente','pon-sur','sp','ps'],
'O':['oriente','o'],
'P':['poniente','p'],
'NS':['norte-sur','ns','sn'],
'OP':['oriente-poniente','op','po'],
'NOP':['nororiente-poniente','nor-oriente-poniente','nor / oriente / poniente','nop','npo','pno','pon','opn','onp'],
'SOP':['sur-oriente-poniente','osp','oriente-surponiente'],
'NSO':['nororiente-sur','nos','nor-oriente-sur'],
'NSP':['norponiente-sur','nps'],
'NOSP':['todas','todas las anteriores','nosp'],
np.nan:['1','-'],    
}

housing_types={'Departamento':['departamento','habitacional','completo'],
    'Piso':['piso'],
    'Semi Piso':['semi piso','semi-piso'],
    'Clasico':['clásico','clasico','tradicional','cocina tradicional'],
    'Moderno':['moderno','cocina incorporada'],
    'Monoambiente':['monoambiente','un ambiente','solo un ambiente'],
    'Penthouse':['penthhouse','penhouse','penthouse','penthouse duplex'],
    'Standar':['standar','estándar'],
    'Normal':['normal'],
    'Duplex':['duplex','dúplex','dúpex'],
    'Loft':['loft'],
    'Triplex':['triplex','tríplex'],
    'Oficina':['apto oficina','oficina'],
    'Estudio':['studio','estudio'],
    np.nan:['-']
}

rating_columns = [
    'General_Expenses', 'Size_of_the_flat', 'Bedrooms', 'Bathrooms', 'Seller',
    'metraje', 'sup_terraza', 'sup_util', 'ambientes', 'dormitorios', 'banos',
    'estacionamiento', 'bodegas', 'piso_unidad', 'cant_pisos', 'dept_piso',
    'antiguedad', 'tipo_depa', 'orientacion'
]


name_mapping={
'url':'url', 
'Name_of_the_flat':'id_name', 
'Value':'valor', 'Currency':'moneda', 
'General_Expenses':'gastos_comunes',
'Size_of_the_flat':'metraje',
'Bedrooms':'habitacion', 
'Bathrooms':'bano', 
'Seller':'vendedor', 
'metraje':'sup_total',
'sup_terraza':'sup_terraza',
'sup_util':'sup_util', 
'ambientes':'ambientes', 
'dormitorios': 'dormitorios', 
'banos':'banos',
'estacionamiento':'estacionamiento', 
'bodegas':'bodega', 
'piso_unidad':'piso_unidad', 
'cant_pisos':'tot_pisos', 
'dept_piso':'dept_x_piso',
'antiguedad':'antiguedad', 
'tipo_depa':'tipo_depa', 
'orientacion':'orientacion', 
'Calle':'calle', 
'Barrio':'barrio', 
'Comuna':'comuna',
'Ciudad':'ciudad', 
'Dirección':'direccion', 
'Fecha_Publicacion':'fecha_scrap', 
'Description':'descripcion',
'quality_rate':'quality_scrap'
}