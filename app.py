from flask import Flask,render_template,request 
import pickle
app = Flask(__name__) 

model = pickle.load(open("IplFirstInningsScorePredictor.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html") 

@app.route("/predict",methods=["POST"])
def predict():
    prection_list = []
    if request.method == 'POST':
        batting_team = request.form['batting-team']
        bowling_team = request.form['bowling-team']  
        if batting_team == bowling_team:
            return render_template("index.html",error="Please Select Batting and Bowling team different..!!")
        else:
        #Batting encoding 
            if batting_team == 'csk':
                prection_list = prection_list +[1,0,0,0,0,0,0,0]
            elif batting_team == 'dd':
                prection_list = prection_list +[0,1,0,0,0,0,0,0]
            elif batting_team == 'kxip':
                prection_list = prection_list +[0,0,1,0,0,0,0,0]
            elif batting_team == 'kkr':
                prection_list = prection_list +[0,0,0,1,0,0,0,0]
            elif batting_team == 'mm':
                prection_list = prection_list +[0,0,0,0,1,0,0,0]
            elif batting_team == 'rr':
                prection_list = prection_list +[0,0,0,0,0,1,0,0]
            elif batting_team == 'rcb':
                prection_list = prection_list +[0,0,0,0,0,0,1,0]
            elif batting_team == 'srh':
                prection_list = prection_list +[0,0,0,0,0,0,0,1] 
            else :
                return render_template("index.html",error="Select Batting team Name..!")
            #Bowling encoding
            if bowling_team == 'csk':
                prection_list = prection_list +[1,0,0,0,0,0,0,0]
            elif bowling_team == 'dd':
                prection_list = prection_list +[0,1,0,0,0,0,0,0]
            elif bowling_team == 'kxip':
                prection_list = prection_list +[0,0,1,0,0,0,0,0]
            elif bowling_team == 'kkr':
                prection_list = prection_list +[0,0,0,1,0,0,0,0]
            elif bowling_team == 'mm':
                prection_list = prection_list +[0,0,0,0,1,0,0,0]
            elif bowling_team == 'rr':
                prection_list = prection_list +[0,0,0,0,0,1,0,0]
            elif bowling_team == 'rcb':
                prection_list = prection_list +[0,0,0,0,0,0,1,0]
            elif bowling_team == 'srh':
                prection_list = prection_list +[0,0,0,0,0,0,0,1]
            else:
                return render_template("index.html",error="Select Bowling team Name..!")
            #Overs 
            present_overs = request.form['overs'] 
            if float(present_overs)<5.0:
                return render_template("index.html",error="Overs must be greater then 5.0..!")
            
            prection_list = prection_list + [float(present_overs)]
            present_runs = request.form['runs']
            prection_list = prection_list + [int(present_runs)]
            present_wickets = request.form['wickets']
            prection_list = prection_list + [int(present_wickets)]
            runs_in_5_overs = request.form['runs in previous overs']
            prection_list = prection_list + [int(runs_in_5_overs)]
            wickets_in_5_overs = request.form['wickets in previous overs']  
            prection_list = prection_list + [int(wickets_in_5_overs)]

            res = model.predict([prection_list])
            res = int(res[0])
            return render_template("index.html",result=batting_team + " will score "+str(res)+"runs in 20 Overs")



if __name__ == "__main__":
    app.run(debug=True)