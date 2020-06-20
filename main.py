""" Main script """
import matplotlib.pyplot as plt
import cell_game

### Main loop
if __name__ == "__main__":
    BOARD = cell_game.generate_board(15, 15)
    GENERATION = 1
    ALIVE = [sum(sum(BOARD))]
    FIG = plt.figure()
    plt.imshow(BOARD, interpolation='none', cmap='binary')
    FIG.suptitle('Generation {}'.format(GENERATION))
    plt.pause(1)
    try:
        while True:
            BOARD = cell_game.new_generation(BOARD)
            ALIVE.append(sum(sum(BOARD)))
            if ALIVE[-1] == 0:
                print('all dead')
                input('Press Enter to Exit')
                break
            if len(ALIVE) > 5:
                _ = ALIVE.pop(0)
            if len(ALIVE) == 5 and len(set(ALIVE)) == 1:
                print('Generation stable')
                input('Press Enter to Exit')
                break
            GENERATION += 1
            plt.imshow(BOARD, interpolation='none', cmap='binary')
            FIG.suptitle('Generation {}'.format(GENERATION))
            plt.pause(0.25)
            plt.clf()
    except KeyboardInterrupt:
        pass
    finally:
        plt.close()
