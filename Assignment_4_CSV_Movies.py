import csv

"""
with open("T:\Analytics and Improvement-Private\CAMP\Aaron V\Toolbox\Training\Python\Files\movies.csv","w",newline="") as f:
    write=csv.writer(f,delimiter=",")
    write.writerow(["Top Gun","Risky Business","Minority Report"])
    write.writerow(["Titanic","The Revenant","Inception"])
    write.writerow(["Training Day","Man on Fire","Flight"])
"""

movies = [["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]

with open("movies.csv","w") as moviefile:
    moviewriter = csv.writer(moviefile,delimiter=",")
    for movie_list in movies:
        moviewriter.writerow(movie_list)
