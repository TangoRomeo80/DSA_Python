def tournamentWinner(competitions, results):
    currentBest = ''
    scores = {currentBest: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        if result == 1:
            scores[homeTeam] += 3
            if scores[homeTeam] > scores[currentBest]:
                currentBest = homeTeam
        elif result == 0:
            scores[awayTeam] += 3
            if scores[awayTeam] > scores[currentBest]:
                currentBest = awayTeam

    return currentBest
