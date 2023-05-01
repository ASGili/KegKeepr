from db.run_sql import run_sql
from models.brewery import Brewery
from models.beer import Beer
import repos.beer_repo as beer_repo
import repos.brewery_repo as brew_repo
import repos.keg_repo as keg_repo

def delete_all():
    sql = "DELETE FROM beers"
    run_sql(sql)

def delete(id):
    sql="DELETE FROM beers WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def save(beer):
    sql = "INSERT INTO beers (name, abv, brewery_id) VALUES (%s, %s, %s) RETURNING id"
    values = [beer.name,beer.abv,beer.brewery.id]
    result = run_sql(sql,values)
    beer.id = result[0]['id']
    return beer

def select(id):
    sql = "SELECT * FROM beers WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)
    if results:
        result = results[0]
        brewery = brew_repo.select(result['brewery_id'])
        beer = Beer(result['name'],result['abv'],brewery,result['id'])
    return beer

def select_all():
    beers = []
    sql = "SELECT * FROM beers"
    rows = run_sql(sql)
    for row in rows:
        brewery = brew_repo.select(row['brewery_id'])
        beers = Beer(row['name'],row['abv'],brewery,row['id'])
    return beers

def update(beer):
    sql = "UPDATE beers SET (name, abv, brewery_id) = (%s, %s, %s) WHERE id = %s"
    values= [beer.name,beer.abv,beer.brewery.id,beer.id]
    run_sql(sql, values)