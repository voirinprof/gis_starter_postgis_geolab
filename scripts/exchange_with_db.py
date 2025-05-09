# -- Extraire les données d'une table PostgreSQL et faire un fichier CSV --

# on importe pandas et sqlalchemy
import pandas as pd
from sqlalchemy import create_engine


user = "gisuser"
password = "gispass"
host = "postgis"
port = "5432"
dbname = "gisdb"

# on définit une connexion
db_url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
con = create_engine(db_url)

# on définit une requête SQL (non spatiale)
sql = "SELECT NAME, CAPITAL, APPROX FROM world_borders"
# on fait le DataFrame à partir du SQL
df = pd.read_sql(sql, con)
# on conserve le DataFrame dans un fichier CSV
df.to_csv('/workspaces/gis_starter_postgis_geolab/data/world_borders.csv', index=False)

# -- Alimenter une table PostgreSQL à partir d'un fichier CSV --

# on importe pandas et sqlalchemy
import pandas as pd
from sqlalchemy import create_engine
# on définit une connexion
db_url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
con = create_engine(db_url)
# on lit le fichier CSV
df = pd.read_csv('/workspaces/gis_starter_postgis_geolab/data/world_borders.csv')
# on écrit les données dans la table
# Attention, le fichier CSV doit avoir la même structure que la table (sinon
# corriger le dataframe)
# exemple si des colonnes n'ont pas le même nom, on peut faire ceci:
# df.rename(columns={'code':'code_status'}, inplace=True)
df.to_sql('world_borders_csv', con, if_exists='append', index=False)


# -- Extraire une table de PostGIS et faire un fichier csv --

# on importe geopandas et sqlalchemy
import geopandas as gpd
from sqlalchemy import create_engine
# on définit une connexion
db_url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
con = create_engine(db_url)

# on définit une requête spatiale
sql = "select * from world_borders"
# on va créer un GeoDataframe à partir du SQL
gdf = gpd.GeoDataFrame.from_postgis(sql, con, geom_col="geometry")
# on peut simplement sauvegarder le résultat de la requête en CSV
gdf.to_csv('/workspaces/gis_starter_postgis_geolab/data/world_borders.csv', index=False)


# -- Lire un fichier CSV et écrire dans une table PostGIS --

# on importe pandas, geopandas et sqlalchemy
import pandas as pd
import geopandas as gpd
from sqlalchemy import create_engine
# on définit une connexion
db_url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
con = create_engine(db_url)
# on lit un fichier CSV
# ex:
# id,sort_name,iso_country,geospatial,designation,full_name
# 3,West,WA,POINT (11.45310702221933 -14.501953125),West Africa,Africa
# ...
df = pd.read_csv('/workspaces/gis_starter_postgis_geolab/data/world_borders.csv')

# CAS #1 - notre CSV a exactement la structure de la table
# on va simplement convertir la colonne geospatial en geometry
df['geometry'] = gpd.GeoSeries.from_wkt(df['geometry'])
# on peut facilement créer une GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:4326")
# on peut ensuite envoyer les données dans PostGIS
# attention il faut que le CSV respecte la structure de la table (sinon corriger
# avant l'envoi)
gdf.to_postgis('world_borders_csv2', con, if_exists='append')

# CAS #2 - Les points sont conservés avec LON, LAT
# donc pas besoin de conversion à partir du WKT
# on va créer les géométries à partir des lon, lat
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat), crs="EPSG:4326")
# on doit simplement enlever les colonnes LON, LAT
# et on doit renommer la colonne Géométrie pour qu'elle respecte le nom
# dans la table
gdf.drop(['lon'], axis=1, inplace=True)
gdf.drop(['lat'], axis=1, inplace=True)
gdf.rename_geometry('geospatial', inplace=True)
# on envoie dans la table
gdf.to_postgis('city', con, if_exists='append')