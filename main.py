import argparse
import matplotlib.pyplot as plt
import numpy as np
import process


def main(args):
    results = np.random.rand(int(args.input))

    if args.save_results:
        np.save('results.npy', results)
        print("Результаты сохранены в 'results.npy'")

    if args.console_output:
        print("Результаты: ", results)

    if args.generate_plots:
        plt.plot(results)
        plt.savefig('plot.png')
        print("График сохранен в 'image_folder/plot.png'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Запуск нейронной сети')
    parser.add_argument('--input', type=str, required=True, help='Входные данные для нейронной сети')
    parser.add_argument('--save_results', action='store_true', help='Сохранить результаты в файл')
    parser.add_argument('--console_output', action='store_true', help='Вывести результаты в консоль')
    parser.add_argument('--generate_plots', action='store_true', help='Сгенерировать графики результатов')
    args = parser.parse_args()

    main(args)
