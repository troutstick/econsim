# econsim

I will try my best to create an economic simulator here. Inspiration from [this blogpost](https://www.gamasutra.com/blogs/LarsDoucet/20130603/193491/BazaarBot_An_OpenSource_Economics_Engine.php)!

### Done:
* A world with a marketplace populated by agents
 * Prices dynamically shift based on supply and demand
 * Agents able to respond to price shifts accordingly
  * Try to switch to more profitable roles
 * Each agent has a job, specializing in producing certain goods
  * Agents buy goods if they can't produce them
* Name generator randomly makes dank names
* Text-based interaction with world


### To-do:
* Agent desires should dynamically change
* Agent behavior should depend on wealth level
 * Promotion/demotion between wealth
  * Certain roles should be restricted to certain wealth levels
* The world should have multiple marketplaces
  * Agents travel between them to act as merchants
  * Marketplaces should have coordinates
   * Costs time and/or resources to move between them
  * Marketplaces laid out on a graph???
* Implement dynamic, effective demand elasticity
* Let user input things more efficiently
* Add ways to better observe world
  * Ways to look at wealth distribution
  * GUI
* Allow money supply to dynamically grow and shrink
 * Add banking?
