# Dragon Age Compendium
Refactoring the Dragon Age: Origins Toolset SQL database for use without game files, for the purpose of accessing dialogue and codex text

### Codex entries/Dialogue

![codex](https://github.com/pod7/dragonage_compendium/blob/master/screenshots/clean_codex.PNG)

### Conversations

```
Duncan (a bit concerned, there shouldn't be a problem):
Did you find the archive?

Alistair (exasperated, but trying to be cool about it all):
Yes, but the scrolls aren't there. We encountered a creepy woman named Morrigan who says her mother has them, but I don't trust her.

Duncan (curious, asking for more information from his soldiers):
What are she and her mother doing in the Wilds? Are they Chasind?

Daveth (said as if anyone should know that witches are terrible, terrible people):
They're witches! She all but said so!

```


In the future, I plan to do something similar for DA2 and DA:I, essentially creating a searchable corpus that spans across the games, but for now it's just Origins. 

## Notes/contact info

I spent *a lot* of time on this. There were a lot of unknowns when I first started this and I went down a lot of wrong paths as I tried to get my bearings. In the end, two of the resources I found most helpful in bridging gaps in my knowledge were [the wiki](http://www.datoolset.net/wiki/Main_Page) and [Sapphimod's tutorials](https://sapphimods.me/tutorials/dialogue-modding-pt-1/). Neither had complete information, but they would occassionally have just what I needed when I encountered a DA:O database-specific problem. If you have the toolset already you're interested in working with the database directly, it's actually not very difficult to use, and I have left an html notebook of what I learned [here](https://github.com/pod7/dragonage_compendium/blob/master/notebooks/origins/origins_exploration_html.html). 


Weird to use tumblr as my calling card, but it's Dragon Age, so feel free to reach out: http://planesofduality.tumblr.com/
Also, twitter: https://twitter.com/planesofduality

## How to Use

**There are csv and raw text files of the dialogue and codices in the `data` folder. These can be downloaded and manipulated however you'd like.**

There are also some Python functions that make searching for keywords or returning character dialogue easy. These are what I like to use. Download the repository as a zipfile and extract it to a folder on your computer (such as 'Documents'). 

If you haven't used Python before, that's ok! There are directions below on how to install and get going with Python using Anaconda.

### Installing Python

* [Download Anaconda](https://www.anaconda.com/products/individual) and follow installation direction
* Open the Terminal or Command Prompt


* Navigate to the folder where you saved the dragonage_compendium. Create the conda environment by following these steps (you only need to do this the first time):
  - Inside of this folder there is a file called `dac.yml` which contains information on the Python version and packages needed to use the Compendium's functions. 
  - To create the conda environment from the `yml` file, type this into the terminal: `conda env create -f dac.yml` and press `Enter`
* To activate the conda environment, type `conda activate da_sql` and press `Enter`
  - To double check you're using the right environment `dac` should be returned if you enter this command: `conda --info envs` and there should be a `*` by the environment name, `da_sql`
* That's it!

## Jupyter Notebook

Run the command `jupyter notebook` from the `dragonage_compendium` folder and navigate to the `notebook` folder to directly interact with these files. 

### Example Notebooks
  - [CharacterDialogue Notebook]() returns all the dialogue for a given character name.
![Flemeth_DB](https://github.com/pod7/dragonage_compendium/blob/master/screenshots/char_dialogue_flemeth2.PNG)
  - [KeywordSearch Notebook]() returns all lines containing a given keyword
![Search](https://github.com/pod7/dragonage_compendium/blob/master/screenshots/keyword_search.PNG)




