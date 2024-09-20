import matplotlib.pyplot as plt
import os
from utils import c_args
from time import sleep

def gen_graph(data:list[float],
         img_save_path:str='./img/result.png',
         **kwargs) -> None:
    """
    Generate a bar graph from the provided data and save it as an image.

    :param data: A list of float values representing the y-values of the bar graph.
    :param img_save_path: The file path to save the generated image. Defaults to './img/result.png'.
    :return None:
    """
    n=len(data)
    index_list = list(range(n))
    plt.bar(index_list,
            data,
            edgecolor='black')
    midpoint = n//2
    custom_ticks = [0, midpoint, n - 1]
    custom_labels = [f'S({n},1)', f'S({n},{midpoint+1})', f'S({n},{n})']
    plt.axvline(midpoint,
                color='red',
                ymax=max(data),
                ymin=0,
                linestyle='--',
                linewidth=2)
    plt.xlabel('k')
    plt.xticks(ticks=custom_ticks, labels=custom_labels)
    plt.ylabel('Number of subsets')
    plt.title(f'Histogram over the distribution of number of k subsets for a set of size {n}')
    plt.savefig(img_save_path)
    plt.close()

def S(n:int=1, k:int=1, **kwargs) -> int:
    """
    Calculate the Stirling number of the second kind S(n, k).
    This function returns the number of ways to partition a set of `n` elements into `k` non-empty subsets.

    :param n: The number of elements in the set.
    :param k: The number of non-empty subsets.
    :return:  S(n, k).
    """
    # Base cases
    if n == 0 and k == 0:
        return 1
    elif n == 0 or k == 0:
        return 0
    elif k > n:
        return 0
    
    return k * S(n - 1, k) + S(n - 1, k - 1)

def calc_bar_plot(n:int=1,
                  img_save_path:str='./img/result.png',
                  **kwargs) -> None:
    """
    Calculate the values of the Stirling number of the second kind for a set of size `n`
    and generate a bar plot to visualize the distribution.

    :param n: The number of elements in the set.
    :param img_save_path: The file path to save the generated image. Defaults to './img/result.png'.
    :return None
    """
    l = []
    for k in range(1,n+1):
        l.append(S(n=n, k=k))
    gen_graph(data=l,
              img_save_path=img_save_path)

def main(n:int=1,
         img_save_path:str='./img/result.png',
         **kwargs):
    """
    Generate and save a series of bar plots for Stirling numbers from 1 to `n`.

    :param n: The number of elements in the set. For each i from 1 to n, a plot will be generated.
    :param img_save_path: The base file path to save the generated images. Defaults to './img/result.png'.
    :return None
    """
    for i in range(1,n+1):
        calc_bar_plot(n=i,
                      img_save_path=img_save_path)
        sleep(0.5)
    print(f'Done!')

if __name__ == "__main__":
    cwd = os.getcwd()
    if not os.path.exists(f'{cwd}/img'):
        os.mkdir(f'{cwd}/img')
    args = c_args()
    main(n=args.n,
         img_save_path=f'{cwd}/img/result.png')