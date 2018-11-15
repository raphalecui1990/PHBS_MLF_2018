# PHBS_MLF_2018
# Prediction model of stock price based on change of demand price elasticity 

# Team member： Cui Jianfu 1801213535

Motivation：

If we can predict stock prices five days from now with appropriate data and algorithms, we will solve two very important problems in the investment market:

1.Give investor some useful suggestion in stock market
2.Calculate the probability of the prediction, and then use The Kelly Criterion to achieve better asset allocation

# One: Data process function 

The price elasticity of demand is the degree of reaction of a commodity demand change to product prices in a certain period of time in economic principles.We know that the outstanding shares in the securities market will be announced in the financial report, and at the same time, the data on institutional holdings, restricted shares, and executive holdings will be announced. On this basis, we can announce the above through the price elasticity of demand. The tradable shares in the financial report are added together, and the total tradable shares are compared, and finally the approximate number of shares held by other retail investors is obtained.

![1](https://github.com/raphalecui1990/PHBS_MLF_2018/blob/master/WechatIMG95.png)

That means,if the number of shares held by the institution accounts for a large proportion of the total number of shares outstanding, the probability of increase is greater.

The above inference is based on the following assumptions:

1.Based on the conclusions in Graham's "Smart Investors" book, institutional holdings are mostly maintained for about eight months, while in China's securities market, although this value has declined, for weekly forecasts, the impact is relatively Controllable.

2.Institutional investors have a relatively low proportion of securities sold and total tradable shares in a week. A small number of stocks will be sold in a week, while most other companies will not face such situations.

In summary, if the relatively stable number of shares held in a listed company is higher, then the tradable shares that are out of circulation are less, and such stocks are more likely to rise when the demand is the same. Based on this assumption, we can predict the probability of stocks rising and falling from the demand side, and give a relative interval through linear regression to assist investment decisions.

# Two: Algorithm selection

First, we preprocess the data.

We collect and collect the number of shares in circulation, institutional holdings, and restricted shares in the financial report issued by the listed company, and finally form a matrix of one data per line, and then corresponding the data of each line to the daily stock trading. The volume and turnover will eventually form an X value, and then the closing price will be set to the Y value for linear regression.

![2](https://github.com/raphalecui1990/PHBS_MLF_2018/blob/master/m1.png)

![3](https://github.com/raphalecui1990/PHBS_MLF_2018/blob/master/m2.png)

Then we will select the algorithm.

After doing the data processing, we can use linear regression to predict the stock price after one day, and we can use cross-validation and random sampling to test the accuracy of the stock forecast price and prepare for subsequent modeling. In the case where the forecast results in a single day are relatively ideal, we assume that the trading volume in the next week, the large shareholders' selling situation is relatively stable, and the market information is relatively stable. Based on this, we will further predict the stock price after one week.

The stock price forecast after one week is based on the following three points:

1. The overall market news is relatively stable, and there will be no major news affecting macros, industries and companies.
2, the market is relatively stable, the transaction volume is relatively stable in the near future
3. The sales situation of major shareholders is not high among all the more than 3,000 listed companies.

Finally, based on the above three assumptions, we will average the predicted volume plus the volume of the previous four days, assuming that this value is the volume of the next four days, and use this as the X value to further predict the next day. The stock price on the third day until one week later, and then based on this prediction, comparing the true value, and finally came to two conclusions:

First, the probability that the stock's predicted price and the real price are relatively consistent
Second, the difference between the stock price and the real price

The first of the above two conclusions will have a very large effect on the subsequent position control, and the other will become the basis for investment decisions, helping investors to manage risk.

![5](https://github.com/raphalecui1990/PHBS_MLF_2018/blob/master/A.png)

# Three: Further assumptions based on the model

For the forecasting model, it only solves part of the problem of securities investment, not only through external factors to predict changes in stock prices, but also in part through changes in stock prices caused by financial accounting, behavioral finance, macroeconomic policies, and industrial policies. Therefore, the current forecast is only a preliminary model, and more data needs to be added later to provide better support for the forecast and improve the final forecast.

In the first part, the probability of predicting the result can be calculated by Kelly formula, and finally the approximate asset allocation of short-term investment is obtained.

The Kelly formula is a probability formula evolved from a casino. Based on this formula, the proportion of funds for each investment can be calculated.
![4](https://github.com/raphalecui1990/PHBS_MLF_2018/blob/master/m3.png)

Among them:

f:The proportion of the next bet that should be made for existing funds;
b:The odds available for betting (the odds here are the net odds);
p:The winning rate;

Asset allocation is the focus of the securities investment process. Excellent asset allocation can effectively reduce market risk and maximize profit. However, this formula is not very effective in the past application, because the probability of profit and loss in securities investment is very difficult. Forecasting, and after big data and machine learning are added, we can use the corresponding model to get a stock or all stocks' ups and downs, and then compare the forecast with the actual situation to give a profit and loss probability. , and then through the formula to optimize the asset allocation.

In the second part, add new variables to make the model richer.

Since the model only predicts market prices through demand elasticity through institutional holdings, restricted shares, etc., there will be many situations beyond the scope of the model's capabilities, such as the impact of corporate finance on stock prices and the impact of macro news on stock prices. Therefore, in the future model iteration, the impact variables on company finance, company operations, industry information, macro data, etc. should also be added to the model in different ways to improve the prediction effect of the model.

# Conclusion

Although we have found a way to predict stock prices through the demand price elasticity function, due to over-fitting and variable sample problems, we need to add further data to finally apply the forecast results to actual stock trading.
