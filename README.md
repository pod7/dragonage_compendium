# Dragon Age Compendium
Refactoring the Dragon Age: Origins Toolset SQL database for use without game files, for the purpose of accessing dialogue and codex text

I spent many, many hours scouring the wiki, old forums, random tumblr posts, StackOverflow... all to understand how the Dragon Age: Origins Toolset database and GUI works and how to get the text from the encoded game files into a format that is not only easy to manipulate (because if that was all I cared about I would just use the Toolset or write SQL queries until my eyes hurt - which, funnily enough, was the only way I could understand where anything was so joke's on me) but also easily available to people across platforms (since the Toolset only works if you have DA:O installed) and operating systems (although Windows is not necessarily the only SQL-friendly machine anymore, with the database hacked into two excel files, it's no longer really necessary).

In the future, I plan to do something similar for DA2 and DA:I, but for now, it's just Origins.

## How to Use

### Installing Python

### Jupyter Notebook

### Example Notebooks

#### Character Dialogue

### Executable File

## History

I spent a lot of time on this, but I don't expect that once this is made public to get credit every single time someone uses the files I have provided here. There was a lot of unknowns when I first started this -- I didn't understand the database architecture, I don't really know SQL, I didn't understand the game file organization (and I didn't know I didn't really need to) -- and I went down a lot of wrong paths at first as I tried to get my bearings. In the end, two of the resources I found most helpful in bridging some of my understandings were [the wiki]() and [Sapphimod's tutorials](). Neither had complete information, but they would occassionally have just the information I needed when I encountered a DA:O database-specific problem.

For understand SQL, why I was always getting errors, StackOverflow, as usual, was my friend. But, surprisingly, I would not have been able to even get started if Microsoft didn't have such great documentation of their SQL server software. I was using their SQL Server Management Software from 2005, because that's what the database is compatible with, and they still have up-to-date addendums on their tutorials (probably because Oracle still uses the very old stuff). Microsoft saved me when I couldn't even connect to the database because of permissions issues, even though it took me an entire evening of Googling to pinpoint that as the problem. 

# Current Resources

* csv files
* Jupyter Notebook for searching

# Future improvements



