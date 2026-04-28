# The Birthday Problem:

print("""If there are n people in a room, how large does n need to be for atleast a 50% possibility that atleast 2 people share a birthday""")


# equation:
# P(more than 2 ppl share a birthday)  = 1- P(nobody shares a birthday)

# P(nobody shares a birthday)  = number of unique birthdays/ number of choices
# number of unique birthdays = 365!/(365-n)!
# number of possible choices = 365**n
# P(nobody shares a birthday) = 365! / ((365-n)! * 365**n )


from math import factorial
import matplotlib.pyplot as plt

def birthday_problem(n):
    values_of_n = []
    P_nobody_list = []
    P_more_than_2_share_list = []
    for i in range(1, n+1):
        number_of_unique_birthdays = (factorial(365)/factorial(365-i))
        number_of_possible_choices = 365**i
        P_nobody = number_of_unique_birthdays/number_of_possible_choices
        P_more_than_2_share = 1- P_nobody
        P_nobody_list.append(P_nobody)
        P_more_than_2_share_list.append(P_more_than_2_share)
        values_of_n.append(i)
        print(f"When n is {i}, the Probability of more than two people are sharing a birthday: {P_more_than_2_share}")

    
    plt.plot(values_of_n, P_more_than_2_share_list)
    plt.xlabel("Number of People (n)")
    plt.ylabel("Probability")
    plt.axhline(y = 0.5, linestyle = "--", label = "50% probility", color = "red")

    for n, p in zip(values_of_n,P_more_than_2_share_list):
        if p>= 0.5:
            plt.axvline(x=n, linestyle = ":", label = f"n_value = {n}")
            plt.scatter(n, p, s = 80, zorder = 5, label = f"Cross at 50 at n = {n}") # s = dot size, zorder = makes sure dot is above the line, 5 is an arbitary number and just means that its above the other layers
            print(f"Minimum number of people required for there to be a more than 50% probability two people share a birthday is at n = {n} and the probability is: {p:.5f}")
            break
    
    plt.legend()
    plt.show()



        


birthday_problem(100)
