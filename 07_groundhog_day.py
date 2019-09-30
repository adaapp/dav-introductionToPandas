# -*- coding: utf-8 -*-
"""07 Groundhog Day.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/adaapp/dav-introductionToPandas/blob/master/07%20Groundhog%20Day.ipynb

# Can Punxsutawney Phil really predict the weather?

> Punxsutawney Phil is the name of a groundhog in Punxsutawney, Pennsylvania. On February 2 (Groundhog Day) each year, the borough of Punxsutawney celebrates the legendary groundhog with a festive atmosphere of music and food. During the ceremony, which begins well before the winter sunrise, Phil emerges from his temporary home on Gobbler's Knob, located in a rural area about 2 miles (3 km) southeast of town. According to the tradition, if Phil sees his shadow and returns to his hole, he has predicted six more weeks of winter-like weather. If Phil does not see his shadow, he has predicted an "early spring." The date of Phil's prognostication is known as Groundhog Day in the United States and Canada, and has been celebrated since 1887. Punxsutawney Phil became an international celebrity thanks to the 1993 movie Groundhog Day.

Historical data regarding Groundhog Day is available in the file `groundhog.csv`

The average temperature is recorded for February and March in

- Pennsylvania (which is in the north-eastern USA)
- The North-East more widely
- The Mid-Western US
- The whole country

To start

- Import the data
- Check the datatypes
- Make the year column a datetime object
- Set the year as the index

Some initial exploration

- How frequently does Phil see his full shadow?
- How do temperatures in the different regions compare?
- Has / how has average temperature changed over time?

The main question

- Is there a significant difference between average temperatures when Phil has or has not seen his shadow?
    - In Pennsylvania? More widely?
    
You might find the following functions useful

- `df.rename({'one': 'foo', 'two': 'bar'}, axis='columns')`
"""

import pandas as pd

from scipy import stats

phil = pd.read_csv("https://raw.githubusercontent.com/adaapp/dav-introductionToPandas/master/groundhog.csv")

phil = phil.dropna()[:-1]

phil = phil.rename({"Punxsutawney Phil":"Shadow"}, axis='columns')

phil.query('Shadow == "Full Shadow"').mean()

phil.query('Shadow == "No Shadow"').mean()

phil.query('Shadow == "No Shadow"').mean() - phil.query('Shadow == "Full Shadow"').mean()

stats.ttest_ind(phil.query('Shadow == "No Shadow"')["February Average Temperature"],phil.query('Shadow == "Full Shadow"')["February Average Temperature"], equal_var=False)