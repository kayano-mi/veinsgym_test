import gym

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

print(test)
