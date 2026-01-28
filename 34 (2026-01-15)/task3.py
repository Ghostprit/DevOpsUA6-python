from flask import Flask, render_template, request

app = Flask(__name__)

class allUsers:
    def __init__(self):
        self.users = [{
            'username': 'User',
            'email': 'user@email.com'
        },
        {
            'username': 'User2',
            'email': 'user2@email.com'
        }]
    
    def getUsers(self):
        return self.users
    
    def exists(self, userInput):
        return userInput in self.users
    

@app.route('/')
def displayForm():
    return render_template('task3template.html')

@app.route('/inputGet', methods=['GET'])
def inputGet():
    
    userInput = {'username': request.args['username'],
                 'email': request.args['email']}
    
    users = allUsers()

    if users.exists(userInput):
        return "<p>Welcome, "+userInput['username']+"</p>" \
        "<p>Your email is: "+userInput['email']+"</p>"
    else:
        return "<strong>Wrong username or password</strong>"