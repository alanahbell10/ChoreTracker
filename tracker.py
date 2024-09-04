import json

# Initialize an in-memory list to store completed chores
completed_chores = []

def lambda_handler(event, context):
    if event['request']['type'] == 'LaunchRequest':
        return on_launch()
    elif event['request']['type'] == 'IntentRequest':
        return on_intent(event['request'])
    elif event['request']['type'] == 'SessionEndedRequest':
        return on_session_end()

def on_launch():
    return build_response("Welcome to the Chore Tracker! You can say, 'I swept the floor' to add a chore or 'What chores have I completed?' to list them.")

def on_intent(request):
    intent_name = request['intent']['name']

    if intent_name == 'AddChoreIntent':
        return add_chore(request['intent'])
    elif intent_name == 'ListChoresIntent':
        return list_chores()
    else:
        return build_response("Sorry, I don't understand that request.")

def on_session_end():
    return build_response("Goodbye!")

def add_chore(intent):
    global completed_chores
    chore = intent['slots']['Chore']['value']
    completed_chores.append(chore)
    return build_response(f"Added {chore} to the list of completed chores.")

def list_chores():
    global completed_chores
    if not completed_chores:
        return build_response("You haven't completed any chores yet.")
    chores_list = ", ".join(completed_chores)
    return build_response(f"You have completed the following chores: {chores_list}.")

def build_response(speech_text):
    return {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': speech_text
            },
            'shouldEndSession': True
        }
    }
