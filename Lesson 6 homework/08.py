Tv = {'BreakingBad':100, 'GameOfThrones':1292, 'TMKUC' : 88, 'Anime' : 3242} 


for i in range(3):  
    Keymax = max(Tv, key=Tv.get) 
    print(Keymax) 
    del Tv[Keymax]

    # Bài 08: Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict