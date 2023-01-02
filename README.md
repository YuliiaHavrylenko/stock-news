<h1 align="center">STOCK NEWS</h1>

## Description
Python program that sends a message to a phone number via the Twilio API with the daily stock price and news headlines of a specified company (Tesla, Inc. in this case). It uses the Alpha Vantage and NewsAPI services to retrieve the stock price and news data, respectively.

<p align="center">

![](imgs/1.PNG)

</p>

### About the project.
The script first gets the stock price for the current day and previous day, and calculates the difference between the two. If the difference is 5% or more, the program then retrieves the latest news headlines for the current day about the specified company using the NewsAPI and sends a message with the stock price and three headlines to a phone number using the Twilio API.

## Project setup
To use this app, you will need to input your own account_sid, auth_token, api_key, and number. These unique codes and numbers will allow the app to access the Twilio API. 

Inside Terminal:

```
On Mac
python3 main.py run

Windows
python main.py run
```