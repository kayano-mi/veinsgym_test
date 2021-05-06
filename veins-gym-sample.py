import gym
# import veins_gym

gym.register(
    id="veins-v1",
    entry_point="veins_gym:VeinsEnv",
    kwargs={
        "scenario_dir": "/home/oaeeny/veins-gym/serpentine-env/scenario",
    },
)

env = gym.make("veins-v1")

env.reset()
done = False
rewards = []
while not done:
    random_action = env.action_space.sample()
    observation, reward, test, done, info = env.step(random_action)

    #                           dsrc    vlc-head   vlc-follow
    # action 0 0                000
    # action 1 0.9              100
    # action 2 0.99  -0.01      010
    # action 3 0.89             110
    # action 4       -0.01      001
    # action 5 0.89             101
    # action 6 0.98  -0.02      011
    # action 7 0.88             111

    rewards.append(reward[0])  # note: reward is a 1-dimensional vector

print("Number of steps taken:", len(rewards))
print("Sum reward:", sum(rewards))
print("Mean reward:", sum(rewards) / len(rewards))
print(test)
