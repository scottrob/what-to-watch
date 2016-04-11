import csv

class Rating:
	def __init__(self, movie_id, user_id, rating):
		self.m_id = movie_id
		self.u_id = user_id
		self.rating = rating

	def __str__(self):
		return '{}: {}, {}'.format(self.m_id, self.u_id, self.rating)

class Movie:
	def __init__(self, movie_id, title):
		self.m_id = movie_id
		self.m_title = title

	def __str__(self):
		return '{}: {}'.format(self.m_id, self.m_title)

	def movie_object():
		pass

class User:
	def __init__(self, user_id, occupation):
		self.u_id = user_id
		self.u_title = occupation

	def __str__(self):
		return '{}: {}'.format(self.u_id, self.u_title)

movies = {}
users = {}
ratings = {}

with open('u.item', encoding='latin_1') as item_file:
	reader = csv.DictReader(item_file, delimiter='|', fieldnames=['movie_id', 'title'])
	for row in reader:
		movie = Movie(row['movie_id'], row['title'])
		movies[movie.m_id] = movie

movies_list = [movies[key] for key in movies]

user_input = input('Enter part of a movie title: ').lower()
for movie in movies_list:
	if user_input in movie.m_title.lower():
		print(movie)

with open('u.user', encoding='latin_1') as user_file:
	reader = csv.DictReader(user_file, delimiter='|', fieldnames=['user_id', 'age', 'sex', 'occupation', 'zip_code'])
	for row in reader:
		user = User(row['user_id'], row['occupation'])
		users[user.u_id] = user

users_list = [users[key] for key in users]

user_input = input('enter a job: ').lower()
for user in users_list:
	if user_input in user.u_title.lower():
		print(user)

with open('u.data', encoding='latin_1') as data_file:
	reader = csv.DictReader(data_file, delimiter='\t', fieldnames=['user_id', 'movie_id', 'rating', 'timestamp'])
	for row in reader:
		rating = Rating(row['movie_id'], row['user_id'], row['rating'])
		ratings[rating.m_id] = rating

rating_list = [ratings[key] for key in ratings]

for movie_id in rating_list:
	if rating in rating_list:
		print(rating)
