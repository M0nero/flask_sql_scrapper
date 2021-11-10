from parser import Scrapper
import sys
sys.path.insert(0, '/Users/gorda/Desktop/PyProjects/jwt-flask/src')


scrapper = Scrapper()
print(scrapper.get_data("bitcoin"))
