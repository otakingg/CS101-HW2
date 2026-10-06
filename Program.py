def GetPlayersInfo(): # Reads all the information from "Player.txt", stores each line in a 2D-list, and returns the list
    playerList = list()

    try:
        with open("Players.txt", 'r') as file:
            data = file.readline()

            while(data):
                data = data.strip().split(';')
                playerList.append(data)
                data = file.readline()

            for i in range(len(playerList)):
                for j in range(1, len(playerList[i])):
                    playerList[i][j] = playerList[i][j].strip()
                
                print(playerList[i])
                # print(*playerList[i])

    except FileNotFoundError as e:
        print(f"Error: {e}")

    return playerList

def DisplayBattingAverage(playerList): # Displays each player's info, along with their batting average, in a new file
    displayFile = open("players_battingaverage.txt", 'w')
    for player in playerList:
        atBats = int(player[3])
        hits = int(player[5])

        battingAvg = hits / atBats if atBats > 0 else 0
        displayFile.write(f"{player}\nBatting Average: {battingAvg}\n\n")

    displayFile.close()

def DisplaySluggingPercentage(playerList): # Displays each player's info, along with their slugging percentage, in a new file
    displayFile = open("players_sluggingpercentage.txt", 'w')

    for player in playerList:
        atBats = int(player[3])
        sluggingPercentage = 10

        if atBats > 0:
            hits = int(player[5])
            doubles = int(player[6])
            triples = int(player[7])
            homeRuns = int(player[8])
            singles = hits - (doubles + triples + homeRuns)

            totalBases = singles + (2 * doubles) + (3 * triples) + (4 * homeRuns)
            sluggingPercentage = totalBases / atBats
        else:
            sluggingPercentage = 0

        displayFile.write(f"{player}\nSlugging Percentage: {sluggingPercentage}\n\n")
    displayFile.close()


def HandleCommand(playerList):
    command = input("Please enter 1 of the following COMMANDS: 'QUIT', 'HELP', 'TEAM', 'REPORT': ") # Prompts the user to enter a command
    command = command.upper()

    if command == "QUIT":
        print("Qutting Program")
    elif command == "HELP":
        print("QUIT will exit the program")
        print("TEAM will ask you for a team name and display info about all the players on said team if it exists")
        print("REPORT will ask you to enter BATTING or SLUGGING. BATTING will display all the players' info along with their batting average. SLUGGING will do the same, but with their slugging percentage")
        HandleCommand(playerList)
    elif command == "TEAM":
        teamName = input("Please enter the team name you want information on: ").strip().upper()
        count = 0

        print('\n')
        for player in playerList:
            if player[1].upper() == teamName:
                print(player)
                count += 1

        if count == 0:
            print("No players found for that team name")
        else:
            print('\n')

        HandleCommand(playerList)
    elif command == "REPORT":
        reportType = input("Please enter BATTING or SLUGGING: ").strip().upper()
        if reportType == "BATTING":
            DisplayBattingAverage(playerList)
        elif reportType == "SLUGGING":
            DisplaySluggingPercentage(playerList)
        else:
            print("Invalid report type")
        HandleCommand(playerList)
    else:
        print("Invalid command")
        HandleCommand(playerList)

def main():
    playerList = GetPlayersInfo()
    HandleCommand(playerList)

main()