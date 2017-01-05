# Run script from console
# python test_pandas.py for get all data
# python test_pandas.py 'New York Giants' for get filter by team
# python test_pandas.py 'New York Giants'  1955 for get filter by team and season
# python test_pandas.py 'New York Giants'  1955 7 for get filter by team, season and week
# ##################################################### 
# order of argument list away_team, season y week.
import sys
from data_pandas import dataPandas
dp = dataPandas()

dp.setArgs(sys.argv)

