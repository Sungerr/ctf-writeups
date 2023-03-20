# We Will Rock You

- Category: Misc
- Difficulty: Beginner
- Final Point Value: 50
- Solves: 229
  
## Description

Hey! Here's the code for your free tickets to the rock concert! I just can't remember what I made the password...

[we_will_rock_you.zip](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

## Solve

Looking at the title of this challenge and the password protected zip, it seems that we will have to use brute force to access its contents. 

To do this, I used the `fcrackzip` tool with the famous [rockyou](rockyou.txt) password list.

```sh
fcrackzip -b -D -p ./rockyou.txt -u we_will_rock_you.zip
```

Running the line above gives us the password `michigan4ever`

And opening up the text file with the password gives us the flag!

`wctf{m1cH1g4n_4_3v3R}`

Flag found!
