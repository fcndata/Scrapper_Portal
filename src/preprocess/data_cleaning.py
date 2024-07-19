import pandas as pd
import numpy as np
from datetime import datetime
import re
import pytz
from .param_pre import orientation_types,housing_types,rating_columns

def map_orientation(value):
    if pd.isna(value):
        return np.nan
    value_lower = str(value).lower()
    for categoria, keywords in orientation_types.items():
        if value_lower in keywords: 
            return categoria
    return value

def map_housing(value):
    if pd.isna(value):
        return np.nan
    value_lower = str(value).lower()
    for categoria, keywords in housing_types.items():
        if value_lower in keywords: 
            return categoria
    return str('review_'+value)

def calculate_quality_rate(row, columns=rating_columns):
    total_columns = len(columns)
    non_nan_count = row[columns].notna().sum()
    quality_rate = non_nan_count / total_columns
    return quality_rate

def update_missing_pairs(df):
    """Update missing values in specified pairs of columns."""
    # Update 'Bedrooms' and 'dormitorios'
    df['Bedrooms'] = df['Bedrooms'].fillna(df['dormitorios'])
    df['dormitorios'] = df['dormitorios'].fillna(df['Bedrooms'])
    
    # Update 'Bathrooms' and 'banos'
    df['Bathrooms'] = df['Bathrooms'].fillna(df['banos'])
    df['banos'] = df['banos'].fillna(df['Bathrooms'])
    
    # Update 'Size of the flat' and 'metraje'
    df['Size of the flat'] = df['Size of the flat'].fillna(df['metraje'])
    df['metraje'] = df['metraje'].fillna(df['Size of the flat'])    
    return df

def update_surface_areas(df):
    """Update metraje, sup_util, and sup_terraza columns based on given logic."""
    # Calculate 'metraje' if it is null
    df['metraje'] = df.apply(
        lambda row: row['sup_util'] + row['sup_terraza'] if pd.isnull(row['metraje']) and not pd.isnull(row['sup_util']) and not pd.isnull(row['sup_terraza']) else row['metraje'], 
        axis=1
    )

    # Calculate 'sup_util' if it is null
    df['sup_util'] = df.apply(
        lambda row: row['metraje'] - row['sup_terraza'] if pd.isnull(row['sup_util']) and not pd.isnull(row['metraje']) and not pd.isnull(row['sup_terraza']) else row['sup_util'], 
        axis=1
    )   

    # Calculate 'sup_terraza' if it is null
    df['sup_terraza'] = df.apply(
        lambda row: row['metraje'] - row['sup_util'] if pd.isnull(row['sup_terraza']) and not pd.isnull(row['metraje']) and not pd.isnull(row['sup_util']) else row['sup_terraza'], 
        axis=1
    )
    
    return df

def update_antiguedad(row):
    """Update 'antiguedad' column based on given rules."""
    current_year = datetime.now(pytz.timezone('America/Santiago')).year
    
    antiguedad_value = row['antiguedad']
    
    # If antiguedad is NaN, empty, or None, do nothing
    if pd.isnull(antiguedad_value) or antiguedad_value == '':
        return antiguedad_value
    
    try:
        value = int(antiguedad_value)
    except ValueError:
        return np.nan

    # Replace values less than 0 or greater than 2030 with NaN
    if value < 0 or value > 2030:
        return np.nan
    
    # If value has more than 2 digits, calculate the age
    if len(str(value)) > 2:
        return current_year - value
    
    return value