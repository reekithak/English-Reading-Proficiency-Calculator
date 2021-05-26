def inter_score(prediction_2):
    if(prediction_2[0][0]>=0.6):
        print(True," Possiblity of Interference from anoher Language")
        score_2 = -0.1
    elif(prediction_2[0][1]>=0.6):
        print(True," Possiblity of Interference from Background Noise")
        score_2 = -0.1
    elif(prediction_2[0][2]>=0.9):
        score_2 = 1.0-prediction_2[0][2]
    else:
        score_2 = prediction_2[0][3]
    print(score_2)
    return score_2
    
#Added bonuses based on biasing and model-drawing performance possibilities . [Corner Cases]
    
    
#Added bonuses based on biasing and model-drawing performance possibilities . [Corner Cases]