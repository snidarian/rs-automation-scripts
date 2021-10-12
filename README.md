# rs-automation-scripts
Basic tasks automated to eliminate monotony



### Usage of the cursor_waypoint_journey_taskmaker.py and the taskheadsman.py


The cursor taskmaker is meant to generate a csv file of click coordinates that is then executed by the taskheadsman. They are meant to both be used everytime a task is to be automate. The reason for this is necessity as the locations of the things you want to click on will vary wildy as perspectives and zoom changes and it's radically easier to take several seconds to remake a fletching.csv or cooking.csv

1 - Get your character's inv the way it will look at the end of a loop. Meaning for example with cooking, you would begin with a full inv of sharks, and start the cursor waypoint generator at that point. In such a case your first two clicks would be to open your bank and then deposit all your sharks.
2 - run the cursor_waypoint_journey_taskmaker.py and make your csv title at the prompt (cooking for example),
3 - left or right click very carefully on each point right or left click that you want in the loop and then when finished hit ESC and the recording sequence will conclude. Then hit CTRL-C to exit the generator.
4 - now run taskheadsman with your new .csv as its argument. for example 'taskheadsman.py cooking.csv' and select all the appropriate options when prompted. You have to find the exact time of loop (at least for efficiency sake you do)


It should be noted that this is an autoclicker and as such possesses no intelligence in the way it operates besides what randomness between intervals and non-linear mouse mapping that is built into the taskheadsman.py program.


No garauntees are provided with these programs.



### Autotypers


The autotypers folders contains programs that will auto type messages (or sequencial lists of messages) on loop so that you don't have to




### Agility shortcut programs


These are still in development and may still require quite a bit of development before they are reliable.







