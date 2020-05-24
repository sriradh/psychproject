from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
from datetime import datetime
import json

# pychwelcomepage.html remove action as shown <form name="WelcomePageForm" method="POST" action="/friends">

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

now=datetime.utcnow()
nowstr= now.strftime("%S%d%H%M")
print(nowstr)

gameLeader = {"dummysession": "dummyPerson"}
players = {"dummysession": ["dummyPerson"]}
categories = {"dummysession": "History"}
sessions = {"sessions": ["dummyPysch"]}


@app.route('/friends', methods=['GET'])
def friends():
        # request.get.args can be used only when this page has parameters coming as ? in the url
        # use request.args.get("parameterkey")

        # form-data is from a form, exactly the same as get.args
        # language = request.form.get('language')

        print("inside friends..")
        data = request.data()
        print(data)
        doublequoteddata = '\"'.join(data.split("'"))
        dictdata = json.dumps(doublequoteddata)
        players = dictdata["players"]
        print(players)

        # data = request.get_json()
        # players = data["players"]
        # print(players)
        # gameLeader = request.args.get('gameLeader')
        # newOrExisting = request.args.get('newOrExisting')
        # sessionId = request.args.get("sessionId")
        # category = request.args.get("category")
        # playerName = request.args.get("playerName")
        # print("printing all the variables now..")
        # print(players)
        # print(type(playersdict))

        # return "Hi!"
        return render_template("askpeopletojoinpage.html", players=players, gameLeader=gameLeader, newOrExisting=newOrExistingGame, sessionId=sessionId, category=category, playerName=playerName)


@app.route('/psychwelcomepage', methods=['GET', 'POST'])
def psychwelcome():
    if request.method == "POST":

        print(request.data)
        playerName = request.form.get("playerName")
        newOrExistingGame = request.form.get("newOrExistingRadio")

        print(playerName)
        print(newOrExistingGame)

        if newOrExistingGame == "existing":
            # for existing sessions, get the session info from the form
            sessionName = request.form["sessionGametoJoinField"]
            players[sessionName].append(playerName)
        else:
            # for new sessions, the nowstr is the actual session name
            sessionName = nowstr
            gameLeader[sessionName] = playerName
            players[sessionName] = [playerName]
            newGameCategory = request.form["gamecategories"]
            categories[sessionName] = newGameCategory
            sessions["sessions"].append(sessionName)

        print(sessionName)
        print(gameLeader)
        print(players)
        print(categories)
        print(sessions)

        data = {"sessionPlayers": players[sessionName],
                "gameLeader": gameLeader[sessionName],
                "newOrExistingGame": newOrExistingGame,
                "sessionId" : sessionName,
                "category" : categories[sessionName],
                "playerName": playerName
                }

        headers = {"Content-Type": "application/json"}

        # return render_template("askpeopletojoinpage.html", players={"sessionPlayers": players[sessionName]}, gameLeader={"gameLeader": gameLeader[sessionName]}, newOrExisting={"newOrExistingGame": newOrExistingGame}, sessionId=sessionName, category=categories[sessionName], playerName=playerName)
        # return redirect(url_for('friends', data=jsonify(data), headers=headers))

    return render_template("psychwelcomepage.html", validSessions=sessions)


if __name__ == "__main__":
    app.run(debug=True, port=1234)

