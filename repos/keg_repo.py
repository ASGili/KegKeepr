from db.run_sql import run_sql
from models.brewery import Brewery
from models.beer import Beer
from models.keg import Keg
import repos.beer_repo as beer_repo
import repos.brewery_repo as brew_repo
import repos.keg_repo as keg_repo

def delete_all():
    sql = "DELETE FROM kegs"
    run_sql(sql)

def delete(id):
    sql="DELETE FROM kegs WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def save(keg):
    sql = "INSERT INTO kegs (beer_id,fill_level,capacity,cost,price) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [keg.beer.id,keg.fill_level,keg.capacity,keg.cost,keg.price]
    result = run_sql(sql,values)
    keg.id = result[0]['id']
    return keg

def select(id):
    sql = "SELECT * FROM kegs WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)

    if results:
        row = results[0]
        beer = beer_repo.select(row['beer_id'])
        keg = Keg(beer,row['capacity'],row['cost'],row['price'],row['id'])
    return keg

def select_all():
    kegs = []
    sql = "SELECT * FROM kegs"
    results = run_sql(sql)

    for row in results:
        beer = beer_repo.select(row['beer_id'])
        keg = Keg(beer,row['capacity'],row['cost'],row['price'],row['id'])
        kegs.append(keg)
    return kegs

def update(keg):
    sql = "UPDATE kegs SET (fill_level, capacity, cost, price, beer_id) = (%s,%s,%s,%s,%s) WHERE id = %s"
    values= [keg.fill_level,keg.capacity,keg.cost,keg.price,keg.beer.id,keg.id]
    run_sql(sql, values)
