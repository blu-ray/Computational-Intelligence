import random
def fitness(member):

    num_of_attacking = 0

    for i in range(len(member)):
        for j in range(i+1,len(member)):
            if((int(member[i])==int(member[j])) or (int(member[i])-int(member[j])==i-j) or(int(member[i])-int(member[j])==j-i)):
                num_of_attacking+=1

    return 28-num_of_attacking

def crossover(member1,member2):
    n = random.randint(0,7)
    m = random.randint(0,7)
    child1 = member1[:min(n,m)]+member2[min(n,m):max(n,m)+1]+member1[max(n,m)+1:]
    child2 = member2[:min(n, m)] + member1[min(n, m):max(n, m)+1] + member2[max(n, m)+1 :]
    return [child1,child2]

def mutation(member):
    n = random.randint(0,7)
    m = random.randint(1,8)
    after = member[:n]+str(m)+member[n+1:]
    return after


def draw_board(member):
    for i in range(8,0,-1):
        line = ""
        for j in range(8):
            if(int(member[j]) == i):
                line += "* "
            else:
                line += "O "
        print (line)



population = []
number_of_pop = 500
number_of_crossovers = 100
number_of_mutations = 100
number_of_notchanged = 150
for i in range(number_of_pop):
    member = ""
    for j in range(8):
        xj = random.randint(1,8)
        member += str(xj)
    #print (member)
    population.append(member)


#print(population[0],population[1])
#print(crossover(population[0],population[1]))

#print (population[0])
#print(mutation(population[0]))
'''
draw_board(population[0])
print(fitness(population[0]))
population.sort(key=fitness,reverse=True)
#print (population[0])
draw_board(population[0])
print(fitness(population[0]))
'''
gen_counter = 1
while(gen_counter<100):
    population.sort(key=fitness, reverse=True)

    # evaluation
    score = 0
    for i in range(number_of_pop):
        score += fitness(population[i])

    #print(str(gen_counter) + " " + str(score/number_of_pop))
    print(score/number_of_pop , end=' ')

    score = 0
    for i in range(int(number_of_pop/2)):
        score += fitness(population[i])

    #print(str(gen_counter) + " " + str(score/number_of_pop))
    print(score*2/number_of_pop)


    nextgeneration = [population[i] for i in range(50) ]
    for i in range(number_of_crossovers):
        n = random.randint(0,int(number_of_pop/2))
        m = random.randint(0, int(number_of_pop / 2))
        childs = crossover(population[n],population[m])
        nextgeneration.append(childs[0])
        nextgeneration.append(childs[1])

    for i in range(number_of_mutations):
        n = random.randint(0,number_of_pop-1)
        changed = mutation(population[n])
        nextgeneration.append(changed)

    for i in range(number_of_notchanged):
        n = random.randint(0, number_of_pop-1)
        nextgeneration.append(population[n])


    population = nextgeneration
    gen_counter += 1

if (fitness(population[0])==28):
    print (population[0])
    draw_board(population[0])
