from flask 
import Flask, jsonify, request 
app = Flask(__name__) 
hearts =    [{"heart_id": "h1", "date": "11/15/2023", "heart_rate": "120bpm"},     
            {"heart_id": "h2", "date": "11/17/2023", "heart_rate": "170bpm"},] 
@app.route("/hearts", methods=['GET']) 

def getHearts():     
    return jsonify(hearts) 
@app.route("/hearts", methods=['POST']) 
def add_hearts():     
    heart = request.get_json()     
    hearts.append(heart)     
    return {'id': len(hearts)}, 200 
@app.route('/hearts/<int:index>', methods=['DELETE']) 
def delete_heart(index):     
    hearts.pop(index)     
    return 'The heart rate has been deleted', 200 
if __name__ == "__main__":     
    app.run()
