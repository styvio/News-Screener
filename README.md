# News-Screener
 Simple python screener to get stock news for stocks that are up on the day!
 Youtube video for this lesson: https://www.youtube.com/watch?v=6xHXJb7_olo
 
 <br/>

## Installation
```pip install styvio```

<br/>

## Usage
```
#get_data returns all data for a specific ticker
overallData = styvio.get_data("MSFT")

#using the key "newsArticle1" returns an object with a variety of information from a specific news article related to the ticker "MSFT"
newsArticle1 = overallData["newsArticle1"]
```
