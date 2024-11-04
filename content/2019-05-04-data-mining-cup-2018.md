Title: Data Mining Cup 2018
Date: 2019-05-04
Category: data science


<link rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.css"
      crossorigin="anonymous">

As part of a practical course from IPD we took part in this years' Data Mining Cup (DMC) sponsored by prodsys.

The DMC is a yearly competition where teams from universities around the world try to solve a data mining task. To quote the task from the [official website](https://www.data-mining-cup.com/reviews/dmc-2018/):

> The task for the participating teams is to use the sales data from a period of four months to develop a prediction model, which can be used to predict the products time of sell out in the following month. The aim is to predict as accurately as possible the precise day when items will sell out.

Each competitor had to submit a file with the predicted sold out dates for February.

The course was split into four teams named after the four houses of Game of Thrones. My team consisted of 4 students and we competed against the other teams - the winner would be allowed to send their solution to the official jury. However, it was a very friendly competition -- with each team presenting their progress and sharing their ideas and findings every two weeks.

## Data

Each team worked with the same data set which had the following form:

    $ head –n 1 prices.csv
    > pid | size | 2017-01-10 | … | 2018-02-28

    $ head –n 1 train.csv
    > date | pid | size | units

    $ head –n 1 items.csv
    > pid | size | color | brand | rrp | mainCategory | category | subCategory | stock | releaseDate

## Evaluation

The goal of the competition was to minimize the error function

$$
E = \sqrt{\sum_i|d_i - \hat d_i|}
$$

where $d_i$ is the actual sold-out date for item $i$ and $\hat d_i$ is the predicted sold-out date for item $i$.

__Example__: For an example item with a actual sold out date of 2018-02-24 and a predicted sold out date of 2018-02-20 the error is 2.

## Plan of attack

Solving this exercise can't be too hard, right? So we as a team decided to stick to the common data analysis framework:

1. Check the given data visually
2. Clean the data, clean outliers
3. Train a model
4. ...
5. Profit

However, it turned out that producing a good prediction was _very_ hard.

## Models tested

We did lots of experimenting with different approaches and models after we cleaned the data and inspected it visually:

- ARIMA / SARIMA models
- Linear Regression
- Lots and lots of trees
- Neural nets

However, nothing really worked.

## The winning approach (for KIT)

What actually worked best for low-stock items is a prediction with this magic formula:

$$
\hat d_i = \min{(\frac{stock_i}{0.08}, 28)}
$$

Based on this value we can infer the sold-out date by using it as an offset from the 1st of February.

With this prediction we were able to reach the 2nd place in our practical course. As the 1st place submitted in the wrong format they were disqualified and we got to submit our solution to the actual competition where we made 11th place - one place short of winning a trip to Berlin.

## Final remarks

Taking part in the DMC was a very fun experience and everyone involved learned a lot. It made clear, once again, that solving real-world problems with machine learning is harder than one thinks.

Scoring 11th place with the formula given above also shows that a simple approach can trump over more sophisticated algorithms if the data and / or the problem at hand are an ill-fit for these algorithms.
