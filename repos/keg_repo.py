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
        result = results[0]
        beer = beer_repo.select(result['beer_id'])
        keg = Keg(beer,result['capacity'],result['cost'],result['price'],result['id'])
    return keg

