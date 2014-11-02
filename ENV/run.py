from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)

callers = {
    "+14158675309": "Curious George",
    "+15622219630": "Tim Lau",
    "+17147878889": "Tammy Hua",
}
 
@app.route("/inbound", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
 
    from_number = request.values.get('From', None)
    from_body = request.values.get('Body', None)

    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Monkey, thanks for the message!"

    resp = twilio.twiml.Response()
    resp.message(message)
    
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)