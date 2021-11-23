class Rating:

    def __init__(self, userId, movieId, rating, timestamp):
        self._userId = userId
        self._movieId = movieId
        self._rating = rating
        self._timestamp = timestamp