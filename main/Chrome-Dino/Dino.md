# Hack the Chrome-Dino Game

<h2 align="center">
   <img src="https://github.com/TSG405/Simple-Games/blob/main/main/Chrome-Dino/119281F1-DFBF-4C53-B0BF-CF7E3FD370F3.png" alt="Here goes an ICON!">
</h2>


 #### Google Chrome includes an endless-runner `Dinosaur game` which appears in the absense of internet connection. 
  >If you are unable to get the `No Internet` page, open a new tab and type `chrome://dino` and press enter.
  
 ## Playing
  * **Space Bar / Up**: Jump (also to start the game)
  * **Down**: Duck (pterodactyls appear after 450 points)
  * **Alt**: Pause
  * *The game enters a black background mode after every multiple of 700 points for the next 100 points.*
  
  
## Open Chrome Console
  * Make sure you are on the `No Internet` Connection page.
  * Right click anywhere on the page and select Inspect. (CTRL + SHIFT + J)[WINDOWS]
  * Go to the `Console` tab. Then, we will enter the commands to `tweak` the game.
  
## Tweaking Speed
 * Type the following command in Console and press enter. You can use any other speed in place of 1000.*
 * When you want to run:
    `Runner.instance_.setSpeed(1000)`
* When you want to stop:
    `Runner.instance_.setSpeed(10)`
    
## Immortality
 * After every command press enter. All the commands are case-sensitive.
 * We store the original game over function in a variable:
    `var original = Runner.prototype.gameOver`
 * Then, we make the game over function empty:
    `Runner.prototype.gameOver = function(){}`
    
  #### Stopping the game after using Immortality
 * When you want to stop the game, Revert back to the original game over function:
      `Runner.prototype.gameOver = original`
      
## Setting the current score
  * Let’s set the score to 1235. You can set any other score less than 99999. The current score is reset on game over.
    `Runner.instance_.distanceRan = 1235 / Runner.instance_.distanceMeter.config.COEFFICIENT`
## Stand still and gain points
  * It does not move but the score increases
    `Runner.instance_.playingIntro = true;`
  * Stopping the game
    `Runner.instance_.playingIntro = false;`
## Auto Play 
   **Paste the entire code from auto_dino.js**
   
 
@TSG405
