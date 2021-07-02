import styvio

tickerList = ["LUV", "AAPL", "HD", "COST"]

topNews = []

for i in range(0, len(tickerList)):
    print("Getting Data for Stock: " + str(i+1) + " out of " + str(len(tickerList)))
    overallData = styvio.get_data(tickerList[i])
    data = overallData["dailyPrices"]
    newsArticle1 = overallData["newsArticle1"]
    newsArticle2 = overallData["newsArticle2"]
    newsArticle3 = overallData["newsArticle3"]
    newsArticle4 = overallData["newsArticle4"]
    newsArticle5 = overallData["newsArticle5"]

    initial = data[0]
    final = data[len(data)-1]

    ret = (((final)-(initial))/(initial))*100

    if(ret > 0):
        topNews.append(newsArticle1)
        topNews.append(newsArticle2)
        topNews.append(newsArticle3)
        topNews.append(newsArticle4)
        topNews.append(newsArticle5)
    

print(topNews)
