stream=open("movies.txt")
movielist=[movie.rstrip("\n").split(",") for movie in stream]

# No of movies released in 2022

movies2022=[movie for movie in movielist if movie[1]=="2022"]
print(len(movies2022))

# Number of malayalam movies

malayalammovies=[movie for movie in movielist if movie[-2]=="malayalam"]
print(len(malayalammovies))
# Theater released movies

theatermovies=[movie for movie in movielist if movie[-1]=="theater"]
print(theatermovies)
# list of movies rating greater than 4

ratingmovies=[movie for movie in movielist if int(movie[2])>4]
print(ratingmovies)
# {2022:4,2021:6,2020:2}
yearmovie={}
for movie in movielist:
    if yearmovie.get(movie[1]):
        yearmovie[movie[1]]+=1
    else:
        yearmovie[movie[1]]=1
print(yearmovie)


# which year is maximum movies released

for year in yearmovie.keys():
    if yearmovie[year]==max(yearmovie.values()):
        print(year)

