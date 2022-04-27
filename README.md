[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6498019.svg)](https://doi.org/10.5281/zenodo.6498019)

# MACS 30200 "Perspectives on Computational Research": Major industry-wide and sub-industry-wide changes in interview questions during the Covid-19

Author: Zhe Zhang

## Introduction

Due to the epidemic, remote is becoming more and more a work option for companies, and the effect of remote work varies for different companies. For the IT industry, the impact may not be significant. For financial companies, it is more difficult for employees to maintain their relationships with customers than before because of remote work. And the timing of full remote working varies from company to company, with IT being the first, and traditional consumer goods being largely unavailable for remote working. I wanted to verify that "for most companies, remote work actually affected (positively/negatively) the company's growth" by examining company interview questions at different times during the epidemic. I also tried to summarize the impact of remote work for different types of companies and their respective attitudes towards remote work.

## Collect the Data

- The files used to scrap the data from Glassdoor are saved in folder `project/Communication_and_high_tech`;`Consumer_Discretionary_and_traditional`;`Consumer_Financials_and_Services`. 
- Use the `crawling.py` file to download all the interviews from Glassdoor.  
- The data are uploaded here: Because analysis requires summary data for different categories and all categories, the file is too large to upload. Summary data can be viewed from Google Drive.
- link is here: https://drive.google.com/drive/folders/1NTSGLYtsNZalSykyduELiRfrWWnMuEmo?usp=sharing
- Please refer to this CSV file [source.csv](https://github.com/macs30200-s22/replication-materials-ZHE-ZHANG-0213/files/8569605/source.csv)
 for company selection and their interview questions website.

## Step 2: Wordfrequency Analysis

I expect to use Tfidf to analyze the word frequency of the data and to determine the importance of different words based on their frequency. And to monitor if the change in "word frequency/day" of words related to remote is significant over the three time periods (the word frequency/day is used because the three time periods have different time totals)

For details, please see file 

[Initial analysis for Communication_and_high_tech.ipynb](https://github.com/macs30200-s22/replication-materials-ZHE-ZHANG-0213/blob/master/Project/Initial%20analysis%20for%20Communication_and_high_tech.ipynb).

[Initial analysis for Consumer_Discretionary_and_traditional.ipynb](https://github.com/macs30200-s22/replication-materials-ZHE-ZHANG-0213/blob/master/Project/Initial%20analysis%20for%20Consumer_Discretionary_and_traditional.ipynb).

[Initial analysis for Financials_and_Services.ipynb](https://github.com/macs30200-s22/replication-materials-ZHE-ZHANG-0213/blob/master/Project/Initial%20analysis%20for%20Financials_and_Services.ipynb).

## Results

Initially, the length of the interview questions does not determine whether you are accepted or not.
![distribution](https://user-images.githubusercontent.com/89925916/165461863-e48e8a3d-de65-496a-bbd9-cea1054245c0.png)

For different industries, many completely different changes have taken place.

In general, the epidemic can be said to be fatal for traditional industries. The frequency analysis shows that the situation of traditional industries is not optimistic, and the frequency of words such as offer and store have fallen off a cliff; in addition, the response of the financial services industry is also expected, and the decline in the frequency of words for job and customer also shows that the epidemic has made the financial services industry The decline in the frequency of the words job and customer also suggests that the epidemic has left the financial services industry with a whole new challenge of maintaining customer relationships, as mentioned in the introduction and many articles.

In contrast, although Internet companies were also affected by the epidemic, the structure of the industry has changed, as reflected by the strong increase in the frequency of words such as online, team, and leadership. To some extent, Internet companies are trying a new model of recruitment. That is to say, the work situation with group work and online work as the main direction is developing well in Internet & information companies.

Overall, if you want to get better interviews in the post-epidemic era. Based on the results of the big picture analysis, you should give good consideration to the role you play on the team and your efforts to fit in with the work group.

![whole](https://user-images.githubusercontent.com/89925916/165461752-b9a92304-7378-43b0-9b21-05230f9503d0.png)
![Financials_and_Services](https://user-images.githubusercontent.com/89925916/165461753-e5e666c8-6cb3-46cc-9311-7270f6622502.png)
![Consumer_Discretionary_and_traditional](https://user-images.githubusercontent.com/89925916/165461754-4e498ae1-23be-4a22-8859-bb154dd7fb08.png)
![Communication_and_high_tech](https://user-images.githubusercontent.com/89925916/165461755-f0cd7a7b-cec4-4461-a661-e406babb52d1.png)

## Future Plans

Due to glassdoor's new firewall mechanism, I had to use a different crawling method, which was to use selenium for simulated click crawling, which could bypass the firewall restrictions.

But again, the newly acquired data also brought a lot of new content, the most surprising of which was the interview evaluation and interview result data I obtained from label, so my next idea was to build a machine learning model that uses term frequency-inverse document frequency approach to machine learning prediction of the questions you are asked and your interview results. And hopefully get a valid answer that will provide more effective help to the candidate.
