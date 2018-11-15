# PHBS_MLF_2018
# Prediction model of stock price based on change of demand price elasticity 

# Team member： Cui Jianfu 1801213535

Motivation：

If we can predict stock prices five days from now with appropriate data and algorithms, we will solve two very important problems in the investment market:

1.Give investor some useful suggestion in stock market
2.Calculate the probability of the prediction, and then use The Kelly Criterion to achieve better asset allocation

# One: Data process function 

The price elasticity of demand is the degree of reaction of a commodity demand change to product prices in a certain period of time in economic principles.We know that the outstanding shares in the securities market will be announced in the financial report, and at the same time, the data on institutional holdings, restricted shares, and executive holdings will be announced. On this basis, we can announce the above through the price elasticity of demand. The tradable shares in the financial report are added together, and the total tradable shares are compared, and finally the approximate number of shares held by other retail investors is obtained.



That means,if the number of shares held by the institution accounts for a large proportion of the total number of shares outstanding, the probability of increase is greater.

The above inference is based on the following assumptions:

1.Based on the conclusions in Graham's "Smart Investors" book, institutional holdings are mostly maintained for about eight months, while in China's securities market, although this value has declined, for weekly forecasts, the impact is relatively Controllable.

2.Institutional investors have a relatively low proportion of securities sold and total tradable shares in a week. A small number of stocks will be sold in a week, while most other companies will not face such situations.

