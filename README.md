# Assignments
## Task 1
Write down all sample dialogs you will use to test that the bot is functional and ready for launch.
``` 
HAPPY PATH 1
1. User: I'm going to San Francisco next week. Can you help me book a flight?
Bot: Of course! I'd be happy to help you book a flight to San Francisco. Can you please provide your departure city and the dates you would like to travel?
User: I'm departing from New York and I'd like to leave next Wednesday and return the following Monday.
Bot: I've found a round-trip flight from New York to San Francisco on Wednesday, January 12th and returning on Monday, January 17th. The flight departs at 9:00 am. The return flight departs at 2:00 pm. The total cost for this flight is $500. Would you like to book this flight?
User: Yes, please book this flight for me.
Bot: I have successfully booked your round-trip flight from New York to San Francisco on Wednesday, January 12th and returning on Monday, January 17th. Your confirmation number is XYZ789. Thank you for using our service to book your flight. Is there anything else I can assist you with today?
```
``` 
HAPPY PATH 2
2. User: Can you tell me the status of flight XYZ123?
Bot: Hello! I'd be happy to check the status of flight XYZ123 for you. Can you please provide the date and destination of the flight?
User: The flight is from Los Angeles to New York on January 15th.
Bot: According to our records, flight XYZ123 from Los Angeles to New York on January 15th is currently scheduled to depart at 9:00 am and is expected to arrive at 12:50 pm. The flight is on schedule and there are no reported delays at this time. Is there anything else I can assist you with today?
``` 
``` 
EDGE CASE : 
3. User: Hi, I'm trying to book a flight from Los Angeles to Mars for next week. Can you help me with that?
Bot: I'm sorry, but it is not currently possible to book a flight to Mars. Is there another destination that you would like to book a flight to?
User: Oh, I see. Well, in that case, can you book me a flight to the moon instead?
Bot: I'm sorry, but it is not currently possible to book a flight to the moon. Is there another destination that you would like to book a flight to?
```
``` 
4. What are the available flights from New York to Los Angeles on January 15th?
5. Can you book a round-trip ticket from Chicago to Paris for two people?
6. Is it possible to upgrade to first class on my flight from London to Dubai?
7. Do you have any discounts or promotions for flights to Sydney?
8. I need to change my return flight from Rome to New York, what are my options?
``` 
1.a Which dialogs are the most important? Assign priorities to each of the dialogs.
```
Dialog 1 : Priority 1
Dialog 2 : Priority 1
Dialog 3 : Priority 2
Dialog 4 : Priority 1
Dialog 5 : Priority 1
Dialog 6 : Priority 2
Dialog 7 : Priority 3
Dialog 8 : Priority 1
```
1.b Let’s say you have unlimited resources and unlimited time, how much testing do you need to ensure that that the launch is successful?
```
To ensure the chatbot is ready to launch, I would need to test and validate all the following aspects of it.
1. Basic functionality: Can the chatbot understand and respond to basic commands and questions?
2. Language processing: Can the chatbot understand and respond to more complex inputs, with grammatical mistakes?
3. Contextual understanding: Can the chatbot understand and respond appropriately to inputs in the context of a conversation or task?
4. Error handling: Can the chatbot gracefully handle unexpected input or errors, and provide helpful responses to users in these cases?
It may be necessary to perform extensive testing to ensure that the chatbot is functioning properly in all of these areas. This could involve testing the chatbot with a large number of inputs and scenarios, and using multiple testers to evaluate its performance from different perspectives.

```

## Task 2
You are a QA on a Voice Assistant project.  What are the stages of the software development life cycle that require your involvement?  What will this involvement look like?
```
As a QA analyst on a voice assistant project, I would be involved in various stages of the software development life cycle. 
1. During the planning stage, I would help define the scope and objectives of the project, and create a testing plan. 
2. In the design stage, I would review the design documents and identify potential risks. 
3. During development, I would work closely with the team and conduct early testing. 
4. During the testing stage, I would execute the testing plan and ensure that the voice assistant meets the criteria. 
5. Before deployment, I would conduct final acceptance testing and work with the team to resolve any remaining issues. 
My involvement in the SDLC would involve ensuring that the voice assistant is of high quality and meets the requirements.
```

## Task 3
You have 1 month to work on developing test cases for 2 projects. 
But you realize that project requirements will only be defined in 2 weeks and you won’t be able to work on test cases until then.

Also, a software engineer says that he/she needs 2 more weeks for implementation and it seems like you won’t be able to test the projects end to end until he/she is done.
What will you do?
```
I would try to be proactive and communicate with the team to come up with a plan to make the most of the time I have available.

- Work on other tasks until the project requirements are defined.
- Start brainstorming potential test cases.
- Communicate with the software engineer to understand their timeline and work out a plan for testing.
- Consider building a test automation architecture to save time and ensure thorough testing.

```

## Task 4

### Pre-requisites : 
1. Have python 3.6 or newer
2. Have Selenium 3+ installed

### Running the program 

1. Clone this repository
2. Edit the config.json file depending on your operating system
3. Open a terminal at the root of the project
4. Run the following command : 
```
python3 "Task 4/task_four.py"
```

## Task 5

### Running the program 

1. Run the following command : 
```
python3 "Task 5/task_five.py"
```
