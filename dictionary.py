i = 0
while(i<45):
    dictionary = {
        "Programming" : "Programming is the process of creating a set of instructions that tell a computer how to perform a task",

                  "Machine Learning" : "Machine learning is the study of computer algorithms that improve automatically through experience.",

        "Data Science" : "Data science is a concept to unify statistics, data analysis and their related methods in order to understand and analyze actual phenomena with data."
                  }

    print("Welcome to coding dictionary")
    print("Write the word from the following to know the meaning")
    print("Programming")
    print("Machine Learning")
    print("Data Science")
    word = input()

    print(dictionary[word])
    print("")