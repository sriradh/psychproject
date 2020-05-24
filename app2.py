from flask import Flask, render_template, request, redirect, flash, url_for, make_response, jsonify
from datetime import datetime
import json

# pychwelcomepage.html add action as shown <form name="WelcomePageForm" method="POST" action="/friends">

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

now=datetime.utcnow()
nowstr= now.strftime("%S%d%H%M")
print(nowstr)

gameLeader = {"dummysession": "dummyPerson"}
players = {"dummysession": ["dummyPerson"]}
categories = {"dummysession": "History"}
sessions = {"sessions": ["dummyPysch"]}


@app.route('/friends', methods=['GET', 'POST'])
def friends():

        if request.method == 'POST':

            # request.get.args can be used only when this page has parameters coming as ? in the url
            # use request.args.get("parameterkey")

            # form-data is from a form, exactly the same as get.args
            # language = request.form.get('language')

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

            return render_template('friends', players=players.get(sessionName), gameLeader=gameLeader.get(sessionName), newOrExisting=newOrExistingGame, sessionId=sessionName, category=newGameCategory, playerName=playerName)
            return redirect(url_for('friends', data=jsonify(sessionPlayers=players[sessionName],
                                                            gameLeader = gameLeader[sessionName],
                                                            newOrExistingGame= newOrExistingGame,
                                                            sessionId= sessionName,
                                                            category= categories[sessionName],
                                                            playerName= playerName)))


        # the below is for GET
        print('inside GET')
        jsondata = request.get_json()
        print(jsondata)
        strdata = request.args.get("data")
        print(strdata)
        dictdata = json.dumps(strdata)
        print(dictdata.get("sessionPlayers"))
        return "<h1>Hi there!</h1>"
        return render_template('friends', players=players, gameLeader=gameLeader, newOrExisting=newOrExistingGame, sessionId=sessionId, category=category, playerName=playerName)


@app.route('/psychwelcomepage', methods=['GET'])
def psychwelcome():
    if request.method == "GET":
       return render_template("psychwelcomepage.html", validSessions=sessions)


if __name__ == "__main__":
    app.run(debug=True, port=4567)

