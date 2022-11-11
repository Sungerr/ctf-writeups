# spelunk

- Category: Misc
- Difficulty: Medium
- Final Point Value: 174
- Solves: 82
  
## Description

I wrote the flag on a sign [somewhere](spelunk.zip), but I lost it. Only a REAL spelunker can find it!

## Solve

Extracting the zip reveals that the contents of the archive is a minecraft save!

From this, I first attempted to run the save directly on minecraft my moving the archive to `%APPDATA%/.mincraft/.saves` and tried to find the aformentioned sign. I was able to run the save, but had no luck finding the sign.

I then moved on to analyze the files provided. In particular, I was interested in the **.mca** and **.dat/.dat_old files**.

First, I attempted to find the flag through the .mca files, referencing the [Library of Babel](https://ctftime.org/writeup/31289) writeup on CTFtime. The long extraction times on the modified python script with [anvil-parser](https://github.com/matcool/anvil-parser) led me to take a quick look on the .dat files.

Since the description mentioned that the sign was lost, I wondered if the sign could be still be recovered in the old save file (level.dat_old). To test this, I renamed the level.dat file to something random and changed level.dat_old to level.dat.

Lo and behold, running the minecraft world revealed the sign with the flag!

![Flag image](flag.png)

`buckeye{700_m4ny_chunk5_70_5p31unk}`

Flag found!
