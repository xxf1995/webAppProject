import unittest, os.path, sys, psycopg2, getpass
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import api
from unittest import TestCase


# This is a API tester Class that will check the functionality of all the function in api.py
class apiTester(TestCase):
	# def testGetAllPlayer(self):
	#     print(api.getAllPlayer())
	#     self.assertTrue(api.getAllAttributes() != [])

	def testGetAllAttributes(self):
		print(api.getAllAttributes("Cristiano Ronaldo"))
		self.assertTrue(api.getAllAttributes("Cristiano Ronaldo") != [])

	def testCompareDifference(self):
		self.assertTrue(api.compareDifference("Cristiano Ronald","Pepe") != [])
	def testSimilarPlayer(self):
		self.assertTrue(api.similarPlayer("Cristiano Ronaldo") != [])
	def testCalculateCos(self):
		player1 = [10, 10, 20, 30, 10, 20, 10, 40, 25]
		player2 = [20, 20, 5, 10, 20, 30, 10, 20, 15]
		self.assertTrue(api.CalculateCos(9, player1, player2) != 0)

	def testAdvancedSearch(self):
		self.assertTrue(api.AdvancedSearch("age" , 30) != [])


if __name__ == '__main__':
	# # link to database
	# database = getpass.getuser()
	# user = getpass.getuser()
	# #password = getpass.getpass('Enter PostgreSQL password for user {}: '.format(user))

	# # Login to the database
	# try:
	#     connection = psycopg2.connect(database=database, user=user, password="moon329tiger")
	# except Exception as e:
	#     print(e)
	#     exit() 
		   
	unittest.main()
