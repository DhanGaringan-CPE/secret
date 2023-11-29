from flask import Flask, jsonify, request 
app = Flask(__name__) 

hearts = [
    {
        "heart_id":"heart_1",
        "date": "29/11/23",
        "heart_rate":"120bpm"
    },
    {
        "heart_id":"heart_2",
        "date": "29/11/23",
        "heart_rate":"110bpm"
    }
]

@app.route("/hearts", methods = ['Get'])
def getHearts():
    return jsonify(hearts)
    
@app.route("/hearts", methods=['POST']) 
def add_hearts():     
    heart = request.get_json()     
    hearts.append(hearts)     
    return {'id': len(hearts)}, 200 
@app.route('/hearts/<int:index>', methods=['DELETE']) 
def delete_heart(index):     
    hearts.pop(index)     
    return 'The heart rate has been deleted', 200 
    
    
    
    
if __name__ == "__main__":     
    app.run()
