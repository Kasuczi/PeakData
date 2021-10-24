# PeakData
hiring_assignments/data-engineering/data_engineering_hiring

**1 ) How to build and run the code**

For proper working of this project You should start with installing requirements using pip install -r /path/to/requirements.txt
After all this You can run the script using any IDE or even form cmd typing python main.py at the source file location.

**2) Documentation on your approach, i.e. what did you do and why?**

Firstly I am opening the compressed .csv file and selecting the needed columns. Then I am cleaning the data from null authors. 
After that I am unpacking all author to the specific rows. Next I am dropping the duplicates and cleaning rest of data from unnecessary marks.
When it's done, I am aligning the text in the columns and  asking user if he wants only those records when the authors has also affiliation.
Last step is saving the file to .csv with the same compression as at the beginning.

**3) A reporting of potential failure points and bottlenecks**

Probably the greatest threat is the appearance of authors' names and surnames in a different notation, for example with dots between the first name and the surname. 
Then the scribe will not fulfill its role properly.

**4) An accounting of the remaining steps needed before putting deploying your code to a production system**

Now when You know the main function and limitations, the scrip is ready to go.