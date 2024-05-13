import gym

env = gym.make("CartPole-v1")

def random_games():
    for episode in range(10):  # Juega 10 episodios
        state = env.reset()  # Reinicia el entorno al estado inicial
        for t in range(500):  # Intenta hasta 500 pasos por episodio
            env.render()  # Renderiza el entorno visualmente
            action = env.action_space.sample()  # Elige una acción aleatoria
            print(env.step(action))  # Imprime el resultado de la acción
    env.close()  # Cierra el entorno correctamente

random_games()