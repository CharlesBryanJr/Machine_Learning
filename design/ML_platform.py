'''
Design a machine learning platform 
to support some arbitrary big tech company 
like Google or Amazon.

Many systems design questions
are intentionally left very vague 
and are literally given in the form of 
`Design Foobar`. 

It's your job to ask clarifying questions 
to better understand the system 
that you have to build.


1
Q: Are we building this ML platform mainly for a website and/or app?

    understand the intended deployment environment
    so we can tailor the platform to meet website/app needs

A: Yes, there's a website and a corresponding mobile version

2
Q: How many users interact with the a website and/or app daily?

    understand the scale of user activity 
    so we can determine the potential impact of the platform

A: millions of people visit every day.

3
Q: I'm assuming that we'll be supporting dozens of teams, tens of thousands of features, and potentially hundreds of models. Is that a correct assumption?

    Verify scale and scope
    Confirm support for multiple teams
    Assess capacity for tens of thousands of features
    Evaluate capability to handle potentially hundreds of models
    Ensure scalability and performance considerations are met

A: Yes, that's the right scale.

4
From a high level, here are the different conmponets we'll need.
We can dive into each conmponet later on
- Managed Data (how will the ML platform control data?)
- Managed Models (how will the ML platform use the Managed Data?)
- Managed Hosting (we will need to host the model that our ML platform creates)
- Managed Experiments (with our hosted models we will peform experiments to compare performance)
- Managed Monitoring (we must monitor hosted models during experiments or production)

each of these processes can/will be configured for a team's need

managed == 
    the ML platform controls the supporting hardware 
    the ML platform controls the configuration processes for execution
5
What do you mean by managed?


4
Q: Do we have access to a data lake of all the clickstreams and logs required to create relevant features?

A: Yes, there's an HDFS data lake.

Question 4
Q: Is the data that we need to process on the order of petabytes?

A: Yes, it is.

Question 5
Q: Along with that sized data, is there also the need for thousands of daily data jobs to create the tens of thousands of features and labels?

A: Yes, that's reasonable.

Question 6
Q: Does the platform need to support deep learning models?

A: For now, we'll stick to basic models.
'''