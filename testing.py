import gym

env = gym.make("CartPole-v1")

def Random_games():
    # cada episodio es en si mismo aleatorio
    for episode in range(10):
        env.reset()
        # se reinicia y renderiza 500 frames 
        for t in range(500):
            env.render()
            action = env.action_space.sample()
            # array 4 posiciones = (0) posición del Cart, (1) velocidad del Cart, (2) angulo del palo, (3) velocidad angular del palo
            # recompensa obtenida tomada la acción
            # bool estado terminal
            # bool el agente se sale del MDP o del ambiente
            print(env.step(action))


Random_games()