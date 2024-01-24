# poker-CFR

Counterfactual Regret Minimization for Simplified Poker game and rock paper scissors.

This is a personal project created to find an optimal strategy for the simplified poker game - Kuhn poker. The chosen simplification of poker is played with 2 players and uses a regret minimization algorithm. This algorithm is initally implemented for rock paper scissors game in the file rps.py

rps.py uses Counterfactual Regret Minimization (CFR) to minimize the "regret" felt when making a possible move (rock, paper, scissor). The script eventually optimizes to the best strategy: 1/3 rock, 1/3 paper, and 1/3 scissors.

The same CFR algorithm was used for Kuhn poker game. 2-player Kuhn poker is played as follows:
- Each player antes 1.
- Each player is dealt one of the three cards, and the third is put aside unseen.
- Player one can check or bet 1.
  - If player one checks then player two can check or bet 1.
    - If player two checks there is a showdown for the pot of 2 (i.e. the higher card wins 1 from the other player).
    - If player two bets then player one can fold or call.
      - If player one folds then player two takes the pot of 3 (i.e. winning 1 from player 1).
      - If player one calls there is a showdown for the pot of 4 (i.e. the higher card wins 2 from the other player).
  - If player one bets then player two can fold or call.
    - If player two folds then player one takes the pot of 3 (i.e. winning 1 from player 2).
    - If player two calls there is a showdown for the pot of 4 (i.e. the higher card wins 2 from the other player).

Kuhn Poker does have an optimal strategy which CFR does find after training.

For this project I used information from many online sources including:
1. https://justinsermeno.com/posts/cfr/
2. https://scholar.google.com/citations?view_op=view_citation&hl=en&user=RLDbLcUAAAAJ&sortby=pubdate&citation_for_view=RLDbLcUAAAAJ:hMod-77fHWUC
3. https://www.youtube.com/watch?v=ygDt_AumPr0&list=LL&index=2
4. https://www.youtube.com/watch?v=Wa-fRIBGZZI&list=LL&index=3&t=3s
