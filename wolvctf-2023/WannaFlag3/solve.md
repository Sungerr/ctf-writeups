# Wanna Flag III: Infiltration

- Category: OSINT
- Difficulty: Medium
- Final Point Value: 318
- Solves: 82
  
## Description

We have some solid leads so far. However, we need our flags back. Find a way to locate their communication and infiltrate their private ransom service, and submit the stolen flag we wanted to use for the first OSINT!

From outside intelligence, we know the group sometimes goes by w4nn4_fl4g

Completion of this Challenge Unlocks:

**WannaFlag IV: Exfiltration**

**WannaFlag V: The Mastermind**

## Solve

Seaching up `w4nn4_fl4g` we find their [reddit server](https://www.reddit.com/r/w4nn4_fl4g/). 

Going though all the posts, we see instances of a [deleted] user, hinting towards a possible clue in a deleted post or on the deleted user.

My first though was to go through the [Wayback Machine](https://archive.org/web/), however going through the snapshots do not reveal anything noteworthy. 

Next, I tried a combination of the reveddit and unddit tools. Although unddit gave an error on the subreddit, reveddit showed a deleted post labeled [hiiiiiiiii help](https://www.reveddit.com/v/w4nn4_fl4g/comments/11p5w72/hiiiiiiiii_help/). However going under the post through reveddit was unable to display the deleted text. Thus changing the link back over to [unddit](https://www.unddit.com/r/w4nn4_fl4g/comments/11p5w72/hiiiiiiiii_help/), it was able to display the hidden comments. 

One of the comments provide a link to their [hidden website](https://wanna-flag-d60bf7cd-012a-4fcc-9a4c-e60eca6b653f-tlejfksioa-ul.a.run.app/) where we can find the flag on the front page!

`wctf{sp1nnnNn_tH3_cUb333e3E}`

Flag found!
