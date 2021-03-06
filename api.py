# API File containing all the HTML query parsing functions For WebApp
''' 1. Compare two player in XXX
	2. Similar player suggestion
	3. Get player attributes
	'''
import math, psycopg2, getpass, flask

database = getpass.getuser()
user = getpass.getuser()
try:
	connection = psycopg2.connect(database=database, user=user, password='moon329tiger')
except Exception as e:
	print(e)
	exit() 

try:
	cur = connection.cursor()
except Exception as e:
	print('Cursor error: {}'.format(e))
	connection.close()
	exit()

app = flask.Flask(__name__)

def getAllPlayer():
	# return entire database as a list
	try:
		findAllPlayer = "SELECT * FROM players;"
		cur.execute(findAllPlayer)
		allplayer = cur.fetchall()
	except Exception as e:
		print('Cursor error: {}'.format(e))
		connection.close()
		exit()
	return allplayer

@app.route('/Search/Player/<Name>')
def getAllAttributes(Name):
	# return a list of search result for a specific player, such as name, age, ability...
	'''player.printAllattributes()
	'''

	try:
		findPlayer = "SELECT * FROM players WHERE name = (%s);"
		data = (str(Name),)
		cur.execute(findPlayer,data)
		player = cur.fetchall()
	except Exception as e:
		print('Cursor error: {}'.format(e))
		connection.close()
		exit()
	if len(player) < 1:
		return -1
	return player[0]


@app.route('/Search/Compare/<Player1>/<Player2>')
def compareDifference(player1, player2):
	# return a list of the difference between two player, such as age, ability...
	# using Player1 attribute - Player2 attribute
	difference = []
	Attr1 = getAllAttributes(str(player1))
	Attr2 = getAllAttributes(str(player2))
	if Attr1 == -1 or Attr2 == -1:
		return [-1, -1, -1]
	for i in range(3, len(Attr1), 1):
		difference.append(Attr1[i] - Attr2[i])
	return [Attr1, Attr2, difference]


@app.route('/Search/Similar/<Player>')
def similarPlayer(player):
	# return a list player objects that have similar attributes with given player
	playerList = getAllPlayer()
	playerAttr = getAllAttributes(player)

	if playerAttr == -1:
		return [-1, -1]
	differenceDictionary = dict()
	for ComparePlayer in playerList:
		angle = CalculateCos(9, playerAttr[3:],ComparePlayer[3:])
		differenceDictionary[angle] = ComparePlayer[1]	
	result = list(differenceDictionary.keys())
	result.sort()
	# The most similar player should be this player itself, so we choose the second player as the start to print.
	similarList = []
	for i in range(-8,-1,1):
		similarList.append(differenceDictionary[result[i]])
	if len(similarList) < 1:
		return [-1, -1]
	angleList = result[-8:-1]
	return [similarList, angleList]


def CalculateCos(N, vector1, vector2):
	# This function is used to find the difference of two players using the Cos Theory
	# It calculates the Cos vaule  of the angle between N-dimision two vector made by player attributes
	# and turn a exaggrated number

	dotProduct = 0
	vectorLen1 = 0
	vectorLen2 = 0
	for i in range(0,len(vector1),1):
		dotProduct += vector1[i]*vector2[i]
	for attr1 in vector1:
		vectorLen1 += attr1*attr1
	vectorLength1 = math.sqrt(vectorLen1)
	#print(vectorLength1)
	for attr2 in vector2:
		vectorLen2 += attr2*attr2
	vectorLength2 = math.sqrt(vectorLen2)
	# print(vectorLength1,vectorLength2,vectorLength2*vectorLength1)
	if vectorLength1*vectorLength2 == 0:
		return 99
	cosV1V2 = dotProduct / (vectorLength1*vectorLength2)
	return cosV1V2**50

# We tried to have this feature but we decided not to.
# @app.route('/AdvancedSearch/')
# def AdvancedSearch(search, key):
# 	# using keywords such as name,age, attribute to form a Sql quiry that
# 	# search the database and return list of results.
# 	validCols = ['surname','name','age', 'accel', 'agility','react','balance',
# 		'stamina','strength', 'intercept', 'position', 'vision','attributes']
# 	try:
# 		if search in validCols:
# 			findPlayer = 'SELECT * FROM players WHERE ' + search + '=%s'
# 		else:
# 			print("Invalid column name")
# 			exit()
# 		keyword = (str(key),)
# 		cur.execute(findPlayer, keyword)
# 		player = cur.fetchall()
# 	except Exception as e:
# 		print('Cursor error: {}'.format(e))
# 		connection.close()
# 		exit()
# 	return player[0]