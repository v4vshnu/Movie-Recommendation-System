import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

def get_similar(movie_name,rating):
    similar_ratings = corrMatrix[movie_name]*(rating-2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    return similar_ratings

ratings=pd.read_csv("Training Dataset/ratings.csv")
movies=pd.read_csv("Training Dataset/movies.csv")
ratings=pd.merge(movies,ratings).drop(['genres','timestamp'],axis=1)
userRatings=ratings.pivot_table(index=['userId'],columns=['title'],values='rating')
userRatings=userRatings.dropna(thresh=10,axis=1).fillna(0,axis=1)
corrMatrix=userRatings.corr(method='pearson')

romantic_lover=np.asarray(pd.read_csv("Test Dataset/romantic_lover.csv"))
similar_movies = pd.DataFrame()
for movie,rating in romantic_lover:
    similar_movies = similar_movies.append(get_similar(movie,rating),ignore_index = True)
pd.DataFrame(similar_movies).to_csv("romantic_lover_recommendations.csv")


action_lover=np.asarray(pd.read_csv("Test Dataset/action_lover.csv"))
similar_movies = pd.DataFrame()
for movie,rating in action_lover:
    similar_movies = similar_movies.append(get_similar(movie,rating),ignore_index = True)
pd.DataFrame(similar_movies).to_csv("action_lover_recommendations.csv")
