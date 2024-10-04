# Fu

- Category: Web
- Points: 50
- Solves: 488

## Description
"There is just news. There is no good or bad. Except for the news that you can sign up for classes today at [fu.challs.pwnoh.io](fu.challs.pwnoh.io) and become the dragon warrior for a few dollars a month, that is GREAT news!" - Master Oogway

## Solve
With every web challenge, I typically start off with opening the inspect element window. However this site prevented me from opening it up and would redirect me when attempting to get it open.

The solution that I found involved disabling JavaScript in the inspect element settings while on a new tab and going to the website link. This allowed me to keep the tool window open and bypass the redirects.

The flag can be found in the inspector, under the Sign up HTML text as a comment.

![Flag](flag.png)

`bctf{1n5p3c7_3l3m3n7_w0rk4r0und_f0und_88b73569618bcb6a}`

Flag found!