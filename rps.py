import numpy as np
from numpy.random import choice


class RPS:
    def __init__(self):
        self.actions = 3
        self.possible_actions = np.arange(self.actions)        
        self.regret = np.zeros(self.actions)
        self.strategy_val = np.zeros(self.actions)
        self.p2_regret = np.zeros(self.actions)
        self.p2_strategy_val = np.zeros(self.actions)

        # 3x3 table with regret values, top down is player 1 RPS, left right is player 2 RPS
        self.regret_table = np.array([
                    [0, -1, 1],
                    [1, 0, -1],
                    [-1, 1, 0]
                ])


    # gives normalized percentage to play with given regret table
    def normalizedPerc(self, regret):
        new_sum = np.clip(regret, a_min=0, a_max=None)
        normalizing_sum = np.sum(new_sum)
        if normalizing_sum > 0:
            new_sum /= normalizing_sum
        else:
            new_sum = np.repeat(1/self.actions, self.actions)
        return new_sum

    # use numpy choice to select move with normalized regret probability
    def get_move(self, strategy):
        return choice(self.possible_actions, p=strategy)

    # given both players moves, return regret values
    def get_reward(self, my_action, p2_action):
        return self.regret_table[my_action, p2_action]

    # train to achieve nash equilibrium
    def train(self, iterations):
        for i in range(iterations):
            strategy = self.normalizedPerc(self.regret)
            opp_strategy = self.normalizedPerc(self.p2_regret)
            self.strategy_val += strategy
            self.p2_strategy_val += opp_strategy

            p2_action = self.get_move(opp_strategy)
            my_action = self.get_move(strategy)
            my_reward = self.get_reward(my_action, p2_action)
            opp_reward = self.get_reward(p2_action, my_action)

            # loop through each action and calculate overall reward, keep track of total regret for both players
            for a in range(self.actions):
                my_regret = self.get_reward(a, p2_action) - my_reward
                opp_regret = self.get_reward(a, my_action) - opp_reward
                self.regret[a] += my_regret
                self.p2_regret[a] += opp_regret

        
    def final_strategy(self, strategy_val):
        average_strategy = [0, 0, 0]
        normalizing_sum = sum(strategy_val)
        for a in range(self.actions):
            if normalizing_sum > 0:
                average_strategy[a] = strategy_val[a] / normalizing_sum
            else:
                average_strategy[a] = 1.0 / self.actions
        return average_strategy


def main():
    trainer = RPS()
    trainer.train(100000)
    p1_target = trainer.final_strategy(trainer.strategy_val)
    p2_target = trainer.final_strategy(trainer.p2_strategy_val)
    print('p1: {}'.format(p1_target))
    print('p2: {}'.format(p2_target))


if __name__ == "__main__":
    main()