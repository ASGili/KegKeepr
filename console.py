from models.beer import Beer
from models.brewery import Brewery

import repos.beer_repo as beer_repo
import repos.brewery_repo as brew_repo
import repos.keg_repo as keg_repo

beer_repo.delete_all()
brew_repo.delete_all()
keg_repo.delete_all()