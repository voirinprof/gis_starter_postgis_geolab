import geopandas as gpd
from sqlalchemy import create_engine

user = "gisuser"
password = "gispass"
host = "postgis"
port = "5432"
dbname = "gisdb"

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")

# Exemple : création d'une table si elle n'existe pas
world = gpd.read_file("data/world.shp")
world.to_postgis("world_borders", engine, if_exists="replace", index=False)

print("✅ Données insérées dans PostGIS avec succès.")
