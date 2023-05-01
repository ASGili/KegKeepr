from db.run_sql import run_sql
from models.beer import Beer

def delete_all():
    sql = "DELETE FROM beers"
    run_sql(sql)

def save(beer):
    sql = "INSERT INTO beers (name, abv, brewery_id) VALUES (%s, %s, %s) RETURNING id"
    values = [beer.name,beer.abv,beer.brewery.id]
    result = run_sql(sql,values)
    beer.id = result[0]['id']
    return beer
