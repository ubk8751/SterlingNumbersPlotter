from argparse import ArgumentParser as argparser

def c_args():
    parser = argparser(prog='Sterling count calculator',
                       description='''A program to investigate the development
                                      of the distribution of number of subsets of
                                      size k of a set with size n.''')
    parser.add_argument('-n',
                        type=int,
                        default=1,
                        dest='n',
                        help='''The size of the largest set to calculate the sterling
                                count for.''')
    a = parser.parse_args()
    if a.n < 1:
        print(f'Set size cannot be less than 1!')
        exit(1)
    return a