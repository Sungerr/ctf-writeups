# Wanna Flag II: Payments

- Category: OSINT
- Difficulty: Easy
- Final Point Value: 348
- Solves: 75
  
## Description

Ok well.........................something may have gone wrong

WannaFlag's ransom demand is insane, there's no way we are paying that. Can you figure out which address the money is being funneled to?

From the ransom note: `send 500,000 Goerli to 0x08f5AF98610aE4B93cD0A856682E6319bF1be8a6`

## Solve

Looking at the ransom note, we get an address for the ransaction. Searching up the transaction address in [Etherscan](https://goerli.etherscan.io/address/0x08f5AF98610aE4B93cD0A856682E6319bF1be8a6) we find one instance where the account conducts a transaction out. 

Brute forcing through all the transactions, you will eventually find a [transaction](https://goerli.etherscan.io/tx/0xd62a1d10d6c6ccfa9b51fd93eb2704cf454c2d0c39bfd80823ad7fb1d441aa45) sent to self containing a message.

Viewing the mssage in UTF-8 gives us the flag!

`wctf{g1v3_m3_b4cK_mY_cRypT0!!11!}`

Flag found!
