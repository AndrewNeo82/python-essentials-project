# Quiz Game

I created a Quiz game using python. The quiz allows the user to test their general knowledge with two different difficulty levels and a sixty seconds time limit.

# Technologies used
* PYTHON

## Features 

![rpsScreenshot]()

### Username

* Game allows user to input their username to add to the user experience




### time limit

![win](https://github.com/AndrewNeo82/Rock_Paper_Scissors/assets/90483176/e0a3cb0d-f43d-4ff7-9dd3-c01f47bc53bd)

### Message 

* 
![message](https://github.com/AndrewNeo82/Rock_Paper_Scissors/assets/90483176/7a101fb5-54c3-4610-8cdc-df2e40a8ae0f) ![lose](https://github.com/AndrewNeo82/Rock_Paper_Scissors/assets/90483176/7028c876-8371-42e1-9861-c191b584e6b6)


  ### Game Over

* 

 ![over](https://github.com/AndrewNeo82/Rock_Paper_Scissors/assets/90483176/72943755-f147-4167-80ba-ae5175575786)

 ## Future Features 

 * I would like to add a modal for the player to enter a username which opens automatically on page load and insert the username into the game in place of the term "player" to make a better user experience.

## Testing

* 
*
* 
  
![)


* The buttons shake as intended on all device types and rapid pressing of the ssame button in succession will not break the game or affect the game counting of the score.

## Bugs

### Solved

* When i first deployed the website to github pages the message displayed when a round is lost was not working. 

I realised when i had copy pasted the code from my Win message function i had neglected to change "const winMessage = winMessages[winIndex];" to loseMessages[loseIndex];. Once i made this change the function worked as intended.

* The player choice would occasionally return undefined error in the console and fail to display the player last pick.

I solved this by changing "const playerChoice = event.target.dataset.choice;" in the gamePlay function to "const playerChoice = this.dataset.choice;"

## Validator Testing

### PYTHON


## Deployment



[The live link can be found here 
](https://my-python-quiz-fe97e900f186.herokuapp.com/)https://my-python-quiz-fe97e900f186.herokuapp.com/
## Credits   

### Content



  



## Media



