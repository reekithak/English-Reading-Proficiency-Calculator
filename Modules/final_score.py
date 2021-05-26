def final_score(score_1,score_2):
        if(score_1>=0.5 and score_2>=0.5):
        Final_Score = (score_1 + score_2) / 2
        elif(score_1<0.5 and score_2>0.9):
            Final_Score = score_1
        elif(score_1>0.9 and score_2<0.5):
            Final_Score = (score_1 + (score_2+0.25))/2
        else:
            Final_Score = (score_1 + score_2) / 2
    
#Added bonuses based on biasing and model-drawing performance possibilities . [Corner Cases]