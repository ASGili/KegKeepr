from models.beer import Beer
from models.brewery import Brewery
from models.keg import Keg
import repos.beer_repo as beer_repo
import repos.brewery_repo as brew_repo
import repos.keg_repo as keg_repo

# Below are tests for CRUD functions in repos
keg_repo.delete_all()
beer_repo.delete_all()
brew_repo.delete_all()

brewery1 = Brewery("Newbarns") 
brewery2 = Brewery("Moonwake")

brew_repo.save(brewery1)
brew_repo.save(brewery2)
print(brew_repo.select(brewery2.id).name)
print(brew_repo.select_all())

beer1 = Beer("Turbo Shandy",5.0,brewery1)
beer2 = Beer("Pale Ale",3.5,brewery1)

beer_repo.save(beer1)
beer_repo.save(beer2)

keg1 = Keg(beer1,80,5,10)
keg2 = Keg(beer1,40,5,10)
keg3 = Keg(beer2,80,5,10)

keg_repo.save(keg1)
keg_repo.save(keg2)
keg_repo.save(keg3)

