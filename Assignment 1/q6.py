# Ask number of games played in a tournament. Ask the user number of
# games won and number of games loss. Calculate number of tie and total
# Points. (1 win= 4 points, 1 tie =2 points)

noOfGames = int(input("Enter no of games played in a tournament:"))
wonGames = int(input("Enter the number of games won in a tournament:"))
lossGames = int(input("Enter the number of games loss in a tournament"))

tieGames = noOfGames - wonGames - lossGames

totalPoints = (noOfGames * 4) + (tieGames * 2)
print("Total Points:", totalPoints)
