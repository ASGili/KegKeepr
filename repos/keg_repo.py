from db.run_sql import run_sql
from models.keg import Keg

def delete_all():
    sql = "DELETE FROM breweries"
    run_sql(sql)

def save(keg):
    sql = "INSERT INTO kegs (beer_id,fill_level,capacity) VALUES (%s, %s, %s) RETURNING id"
    values = [keg.beer.id,keg.fill_level,keg.capacity]
    result = run_sql(sql,values)
    keg.id = result[0]['id']
    return keg