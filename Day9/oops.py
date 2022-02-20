class Anime:
    def __init__(self,anime_name,anime_episode):
        self.name = anime_name
        self.episode = anime_episode

    def overview(self):
        print("Anime Name:",self.name)
        print("Its Episode:",self.episode)

anime1 = Anime("Psycho Pass",41)  #first instance
anime1.overview()
anime2 = Anime("Vinland Saga",24) #second instance
anime2.overview()
anime3 = Anime("Ergo Proxy",23) #third instance
anime3.overview()
anime4 = Anime() #error, it cant be empty
anime4.overview()