import numpy as np

u = np.array([8,2,5])

a = np.array([9,1,2])
b = np.array([1,9,8])
c = np.array([7,2,6])

def cosine_similarity(x, y):
    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

def find_best_movie(user, movies):
    best_movie = None
    best_similarity = -1

    for movie in movies:
        similarity = cosine_similarity(user, movie)
        if similarity > best_similarity:
            best_similarity = similarity
            best_movie = movie
    return best_movie

print(cosine_similarity(u, a))
print(cosine_similarity(u, b))
print(cosine_similarity(u, c))
print(find_best_movie(u, [a, b, c]))
