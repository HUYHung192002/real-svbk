Tv = {'BreakingBad':100, 'GameOfThrones':1292, 'TMKUC' : 88, 'Anime' : 3242} 


for i in range(3):  
    Keymax = max(Tv, key=Tv.get) 
    print(Keymax) 
    del Tv[Keymax]