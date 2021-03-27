# Workout-Tracking
Python app allowing the user to record his workout exercise stats on a Google Sheet.

The goal of this program is for the user to describe the activity (exercise) he just did and to use natural language to extract information about 
the activity (time, amount of calories spent) and to use such information to create a record in a Google Sheet.

First, we need to create a acount for the Nutritionix API and obtain our credentials (an app id and api key).
Then we need to set the parameters for the POST request which include what we did, our height in cm, our weight in kg and our age.
I hardcoded the value for the "query" key, but it could easily be replaced by an input() function, where the user would describe what he did in the console.

With the response we get, we can extract from it the duration of the exercise, the name of the exercise and the number of calories spent for the exercise.

This is possible thanks to natural language processing of the Nutritionix API (https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.zhjgcprrgvim)

Once we get these informations, we use the Sheety API ( a Google API that can turn a Google Sheet file into a RESTful API)  for our Google Sheet records.
Before that we create a new Google Sheet file in Google Drive.

Then we login into Sheety using our Google credentials, we can get the Sheety endpoint corresponding to our Google Sheet file. For the purpose of our records,
we also need the time at which the exercise was performed (we assume the user uses the program as he as done his exercise). We use the datetime module for that.

We need to set our headers and tha data we intend to send along our POST request in the specified way by the Sheety API. The data we send as JSON corresponds to a row
of our sheet and the keys corresponds to the column names.

Sheety API : https://sheety.co/docs/requests







