import pandas as pd
import numpy as np

class dataPandas:
	def __init__(self):
		self.fields = ['season', 'week', 'away_team', 'a_score', 'away_elo_i', 'home_elo_i','away_elo_f', 'home_elo_f']
		self.df = pd.read_csv('nfl_results.csv', usecols=self.fields, low_memory=False)
		self.away_team = self.season = self.week = 0
	
	# Verify number of arguments, if necesary filter or not
	def setArgs(self, args):
		if len(args) >= 2 and len(args) <= 4:
			try:
				self.away_team = args[1]
			except Exception as e:
				self.away_team = ""
			
			try:
				self.season = args[2]
			except Exception as e:
				self.season = ""

			try:
				self.week = args[3]
			except Exception as e:
				self.week = ""
			
			print 'Valid arguments'
			self.setFilter()
		elif len(args) >= 1 and len(args) <= 2:
			self.getData()
		else:
			print 'Invalid arguments'

	# If not filter, display all data
	def getData(self):
		print self.df.to_string()

	# if necesary filter, depend of arguments we apply an specific filter
	def setFilter(self):
		print "\nFound Elements"
		print "--------"
	
		# Filter by away_team
		if len( self.away_team ) > 0:
			filterBy = ( self.df.away_team == self.away_team.strip() )

		# Filter by season
		if len( self.away_team ) > 0 and len( self.season ) > 0:
			filterBy = ( self.df.away_team == self.away_team.strip() ) & ( self.df.season == int(self.season) )

		# Filter by week
		if len( self.away_team ) > 0 and len( self.season ) > 0 and len( self.week ) > 0:
			filterBy = ( self.df.away_team == self.away_team.strip() ) & ( self.df.season == int(self.season) ) & ( self.df.week == int(self.week) )
		
		findData = self.df[ filterBy ]
		print("Number of found elements: {0}".format(len(findData)))
		
		print findData.to_string()
	
