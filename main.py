from nb_class import load, fit

def main():
    x,y =load()
    print("Done loading data...")
    print("Start fitting data..")
    fit(x,y)



if __name__ == "__main__":
    main()
