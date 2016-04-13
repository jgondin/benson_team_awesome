# benson_team_awesome
Project 1 for  MetisBootcamp

Who are you presenting to?
Food vendors.

What is the problem we’re addressing?

The late-night crowd lacks food options.  And from the food vendors’ perspective - they are leaving money on the table.  
Third shift workers and late-night revelers lack places to eat.  There is a real business opportunity here.

How will we address this problem with the data?

We are going to focus on midnight to 4 AM.

We will separate weekdays and weekends.

We will take entries + exits to measure traffic.  

We will use total traffic data as a proxy for how popular an area is.
We will make recommendations for food vendor placement from this data.

Step 1, clean the data:

- create a Pandas Dataframe
- add a turnstyle delta column
- filter out times that are outside of 12:00am - 4:00am
- create a histogram for each day 