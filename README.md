# Angry Broker

This is a project in NUS Summer Workshop which topic is how to secure service in the untrusted environment  . We are group 3 and we design a game called angry broker with smart contract.

This is group member (in alphabetical order): 

-  Bi Chao ( USTC )
- Liu Jiayi  ( SCU )
- Wu Haotian ( SCU )
- Zhang Wenxuan ( XJTU )



## introduction

Our project is a gambling game based on smart contracts. We generate a unique secret by the player's corresponding value entered by the player. Players are free to bet and compare the value of the secret with the broker to make a profit or loss.



 Advantages : 

- Safety,

- Prevent tampering with data

-  Prevent players from repenting and cheating

- Strong playability

 

## Smart Contract

A smart contract is a set of commitments defined in digital form, including agreements on which contract participants can execute these commitments. It allows trusted transactions without third parties, which are traceable and irreversible.



The part of our smart contract has detailed the initate() function, join() function, calculate() function, payoff() function and other related functions. Before the player joins the game, we determine the player's assets and determine whether he can join the game. Throughout the data transfer process, we also prevent players from repenting and deceiving by uploading hash values and plaintexts. In calculating the secret, we use the method of hashing the player's own plaintext 2 with the plaintexts of the other two players to achieve its uniqueness. The data in the transaction is published on the billboard and uploaded to each block defined by the blockchain by the mine function.





## Contact us

You can contact us by QQ group number 135357489 for more information.

