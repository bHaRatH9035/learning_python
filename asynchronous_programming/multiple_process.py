from multiprocessing import Process

def print_function(value='Full Metal Alchemist Brotherhood'):
    print("I have watched [{}] anime".format(value))

animes = ['Naruto Shippuden', 'Dragon Ball Z', 'Demon Slayer', 'Death Note']
procs = []

if __name__ == '__main__':
    for anime in animes:
        print("creating new process")
        proc = Process(target=print_function, args=(anime,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
