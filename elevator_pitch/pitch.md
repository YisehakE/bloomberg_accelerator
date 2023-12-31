# &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Intro

## Casual Description

- I am an undergrad senior majoring in Computer Science major and minoring in Entrepreneurship Management attending the Johns Hopkins University! 

- I am currently seeking full-time new grad opportunities for software engineering roles, and where I would be able to provide my extensive experience as an engineering technician and a software engineer at the US Naval Research Laboratory and Amazon respectively. 

- My other endeavors I enjoy include providing mentorship with organizations and privately, pursuing entrepreneurial ventures as a team lead, developing personal projects in and outside the classroom, dancing as a hobby and for my culture, and meditating on trails in the midst of nature.


## Technical Description
- I am an undergrad senior majoring in Computer Science major and minoring in Entrepreneurship Management attending the Johns Hopkins University! I am currently seeking full-time new grad opportunities for software engineering roles, and where I would be able to provide my extensive experience as an engineering technician and a software engineer at the US Naval Research Laboratory and Amazon respectively. 

- My work at Amazon was involved in both AWS securities as part of Customer Trust and Partner Support (CTPS) organization my first year, and then AWS cloud computing as part of the CloudTrail team my 2nd year, where I worked on Lake datastore. 

- My 1st year was at Amazon's headquarters in Seattle, I was tasked with developing a full-stack standalone site utilizing AWS services - such as DynamoDB (a NoSQL database), & Identity Access Management - in Typescript for the frontend UI and Java for the SpringBoot backend application. 
  - CHECK OUT AMAZON 2021 FOR MORE DETAILS

- My 2nd year, I was brought back on a new CloudTrail team based in Arlington, VA - Amazon's 2nd headquarters closer to home - to integrate a tooling service using even more AWS services - including Glue, Athena, Lambda, Athena, & Identity Access Management - in Python for the command-line entry point and Typescript for the API functions that facilitated the service logic. This was mostly developed using the Software Development Kit under AWS.
  - CHECK OUT AMAZON 2022 FOR MORE DETAILS


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Work Experience

##                                                        Amazon project 2022
### Overview
- I built a tooling service for internal Amazonians to be able to collect a backlog of event data that may have went missing on the customer side. This was integrated within the AWS CloudTrail infrastructure, and
I managed to design a entry point for internal Amazon workers to specify a range of time they would want to inspect potential missing or corrupted data


### How does it work?
- This entry point sends out these specified parameters of start date, end date, and s3 bucket id to a lambda function to handle comparisions between raw ingested data to the single source of truth
in our hive metastores. 

- I streamlined these comparisons by utilizing SQL in the form of AWS Athena, efficiently using JOIN calls for the event data stored in ORC files, which must be first shifted through 
the partitions-by-date from the S3 bucket(s) users specified on the command line. 

- I followed up on this process with much alpha stage testing to comply with our pipeline checks and eventually spearheaded the automation for this
service within critical points where data typically goes missing in our CloudTrail infrastructure. This way, it ensures data retrieval whether the clients noticed or not, meaning it no longer requires clients to submit a ticket after realizing data is missing.

- I typed up this project in two languages: Python and Typescript. I used Python for the entry point scripting with Boto3 as a useful library, along with typescript to integrate the AWS functionality and to easily layer on top of my team's existing codebase.


## Why was this the project

- THINGS TO CONSIDER:
  - THE VALUE OF THE PROJECT AND YOUR CONTRIBUTION?
  - HOW MUCH DO YOU UNDERSTAND THE WIDER ORGANZATION?
  - HOW MUCH DID YOUR CONTRIBUTION BENEFIT THE ORGANIZATION
      - DID IT IMPROVE THE TRANSPARENCY AND 
      - DID YOU UNDERSTAND THE IMPACT? THE SCOPE?
      - HOW WOULD YOU GROW THE PROJECT GIVEN MORE TIME?
- HOW DID YOU COLLABORATE WITH THE TEAM?
  - 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##                                                        Amazon project 2021

UPDATE

### Overview
- I built a full-stack standalone site for AWS security to report selleers' risk and trends on their account, giving them a risk score. This was developed utilizing AWS services in Typescript and Java through AWS Software Development Kit.


### How does it work?
- ADD

- ADD

- ADD
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Personal Projects

##                                                        HopHustle project

UPDATE

- HopHustle is a web application that a team of 4 and I developed in a course called Object Oriented Software Engineering, and that I continued working on as a personal coding and venture project.

- I utilized a Postgres - Express - React - Node JS (PERN) stack to develop an app that helps students servicers and clients on campus. 

- I was very excited and motivated by the support our professor expressed that I took it upon myself to continue working the app during this past summer, working both on implementation and now the venture side of HopHustle. I have implemented new features such as a trending discovery page, live feed for client requests, and a landing page that stands out along with just maintaining what we've already built.

- We had to map out the project ideation, requirement specifications, and system design before starting the work to develop it from scratch.

- We used a dockerized container to support the application both in local and live development,

- 


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##                                                        CommUnity project

UPDATE

- CommUnity is an web application that a team of 6 and I developed in a course called Computer Science Innovation & Entrepreneurship, and not only that, we also hashed out the business venture along with it!

- We implemented this application with a fun & intereting tech stack of Next.js and Supabase, a new database similiar to Firebase but has these cool features of built-in authentication that we were able to tweak for our Johns Hopkins SSO logins and built-in buckets that we utilized to capture the users media uploads. We coded in Typescript, along with using Open AI ChatGPT open sourced AI, implemented a personalized chat feature where users can ask away about specific information about events or about the club and organizations themselves. -

- I was able to implement many of the different flows for the site, including the search filtering or the modals for the homepage, along with the account page where I'd deal with the access policies for different types of users on our platform


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Questions, questions, questions


## Questions THEY may ask
### Self devised
- What did you learn from X project?
- What challenges did you face when working on X project?
- How did this project make you a better software engineer?
- Walk me through the tech stack you used, and what other solutions you may have explored?


### From Chris
####  Prompt 1:
  - **Prelude**: I see here that you have 2 years experience at this company, and that you work on 2 different systems...
  - **Question**: What would've happened if your internship extended for another 6 weeks for either term?
  - **Possible ways to approach**:
    - I would want to optimized this X because 
    - How to apply fixes from your project to another component within the team
      - Ex: consider modules from other team members work
    - 

#### Prompt #:
  - **Prelude**: 
  - **Question**: 
  - **Possible ways to approach**:
    - 


## Question YOU should ask
### Self devised
- I imagine that Bloomberg maintains their services internally through their own pipeleine, I was curious on:
  - how does Bloomberg ensures engineers are onboard with their pipeline?
  - Were there were any particular challenges when interacting with them?

- What are your experiences that you had with your current team?
- How often does your team build services that other Bloomerg engineers can use?


### From Chris
- What are some interesting challengees you faced with your team?
- What are the features on the terminal that your team is responsible for maintaining, implementating, and deploying?
- What are some features that you would want to go back and reimplement and redeploy?
- How is your department evolving?


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Helpful tips

# Behavioral OR SR ENG

## Tips for communicating
- Talk about the project
  - What was the vision/purpose of the project
  - What approaches did you take?
  - why it mattered (to myself or to others)
- Talk about the tech stack
  - Why did I use the particular tools that I did?
  - Talk about the pros/cons (i.e tradeoffs) of services used
- Talk about challenges faced
  - Spans beyond just the project:
    - Examples:
      - Project
      - Team collaboration
      - Onboarding
  - We can split these into 2 different types: technical AND non-technial
  - Technical:
    - Explain in a algorithmic or concise manner
    - ADDDDDDDDD
  - Non-technical:
    - Build a story
    - ADDDDDDDDD
  - Don't just leave it at the challenge...
    - Expand on what you did to overcome it!
- Buzz words
  - Before giving terms, don't rely too much on these since they can actually HURT you if you overuse them (e.g can trap you in a space you might not actually understand)
  - Terms:
    - Instead of "merge legacy code" --> use "migrate legacy code"
    - Cloud computing 
    - Instead od "entry point" --> use



# Behavioral
## Who are recruiters ?
  - ADD
    - ADD

# Senior Manager
## Who are Sr. Managers ?
  - Any Senior Manager will be in ENGINEERING, not external organizations...
    - Their challenges is finding people-person and growing the health of team AND products in the right way.
    - You should learn about insight into this indivdual's team
    - There are always product managers that senior managers work


# Miscellaneous/Interesting
## Interesting facts about Bloomberg 
  - They have their own Javascript engine for <?>
  - C++ specific libraries for performance and <?>