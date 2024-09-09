movies = {
    'Duty After School': ['action', 'thriller', 'sci-fi'],
    'Ganganam Beauty' : ['comedy' , 'romanance'],
    'Extraordinary You' : ['drama' , 'fiction'],
    'My name' : ['sport' , 'adventure'],
    'Sweet Home' : ['zombies' ,'horror','action'],
    'Descendants Of the sun' : ['army','doctor','suspense'],
    'My love from the star' : ['drama','romance','sciencefiction','supernatural'],
    'My demon' : ['adventor' ,'fantasy'],
    'Squid Game' : ['death','game','life'],
}

def calculate_overlap(user_input, movie_features):

    return len(set(movie_features)& set(user_input.split()))

def recommend_movie(user_input, movies_data):

    best_match = None
    max_overlap = 0

    for movie, features in movies_data.items():
        overlap = calculate_overlap(user_input, features)
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = movie

    return best_match

user_input = input("Enter the Genre of movie you want to see:")

recommended_movie = recommend_movie(user_input,movies)

if recommended_movie:
    print(f"We recommend you these movies : {recommended_movie}")
else:
    print("Sorry! no recommendation found.")    
