# surfs_up

## Project Overview 
Analyze the temperature trends for the months of June and December in Oahu, in order  to evaluate the year-round sustainability of a surf and ice cream shop business.<br/>
We used Python, Pandas, SQLite and SQLAlchemy for this analysis.

## Resources
- Data Sources: [hawaii.sqlite](https://github.com/cedoula/surfs_up/blob/master/hawaii.sqlite)
- Software: Python 3.7.7, Anaconda Navigator 1.9.12, Conda 4.8.4, Jupyter Notebook 6.0.3

## Results
<br/>
 <p align="center">
  <img src="https://user-images.githubusercontent.com/68669675/94208588-d1b06c00-fe8f-11ea-980c-5b013b4407e7.png">
  <img src="https://user-images.githubusercontent.com/68669675/94208585-d117d580-fe8f-11ea-8eff-267885bffc4a.png">
<br/><br/>

- June temperatures range from 64 to 85 degF whereas December Temps range from 56 to 83 degF.
- The average temperature in June is 75 degF whereas in December it is 71 degF. Also 50% of June and December temperatures are above 75 and 71 degF respectively.
- Temperature in December are more spread out than in June since the standard deviation for December temperatures is higher.

## Summary
The temperatures in December are slightly lower than June but suitable for a surf and ice cream shop business.<br/>
More interesting weather data could be gatherered by analyzing the following queries:
 - the total precipitation levels for June and December,
 ```
 session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 6).all()

 session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 12).all()
```
 - the amount of precipitation at the most active station for June and December.
 ```
 session.query(Measurement.prcp).filter(Measurement.station == 'USC00519281').filter(extract('month', Measurement.date) == 6).all()

 session.query(Measurement.prcp).filter(Measurement.station == 'USC00519281').filter(extract('month', Measurement.date) == 12).all()
 ```