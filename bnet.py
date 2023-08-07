import sys
import copy

with open(sys.argv[1], 'r') as file:
    data = [list(map(int, line.split())) for line in file]

if len(sys.argv) not in [2,3,5,6]:
    print("invalid input of arguements")
    exit()

#task 1
btable = [0, 0]
gtable = [[0,0], [0,0]]
ctable = [0, 0]
ftable = [[[0,0], [0,0]], [[0,0], [0,0]]]

for d in data:
    b, g, c, f = d
    btable[b] += 1
    gtable[b][g] += 1
    ctable[c] += 1
    ftable[g][c][f] += 1

b1=c1=g1_b0=g1_b1=f1_g1c1=f1_g1c0=f1_g0c1=f1_g0c0=float("inf")

b1 = btable[1]/(btable[0]+btable[1])
c1 = ctable[1]/(ctable[0]+ctable[1])
g1_b1 = gtable[1][1]/btable[1]
g1_b0 = gtable[0][1]/btable[0]
f1_g1c1 = ftable[1][1][1]/ (ftable[1][1][1] + ftable[1][1][0])
f1_g1c0 = ftable[1][0][1]/ (ftable[1][0][1] + ftable[1][0][0])
f1_g0c1 = ftable[0][1][1]/ (ftable[0][1][1] + ftable[0][1][0])
f1_g0c0 = ftable[0][0][1]/ (ftable[0][0][1] + ftable[0][0][0])
print("\n")
print(f"---------------This is solution of task 1-----------------")
print(f"---------------This is a JPD-----------------")
print("P(Baseball Game on TV=t) = {:.4f} | P(Baseball Game on TV=f) = {:.4f}\n".format(b1,1-b1))
# print("P(B=t) = {:.4f} | P(B=f) = {:.4f}\n ".format(b1,1-b1))
print("P(watches TV=t|Baseball Game on TV=t) = {:.4f}  | P( watches TV=f|Baseball Game on TV=t) = {:.4f}".format(g1_b1,1-g1_b1))
# print("P(G=t|B=t) = {:.4f}  | P(G=f|B=t) = {:.4f}".format(g1_b1,1-g1_b1))
print("P(watches TV=t|Baseball Game on TV=f) = {:.4f} | P( watches TV=f|Baseball Game on TV=f) = {:.4f}\n".format(g1_b0,1-g1_b0))
# print("P(G=t|B=f) = {:.4f} | P(G=f|B=f) = {:.4f}\n ".format(g1_b0,1-g1_b0))
print("P(out of Cat Food=t) = {:.4f} | P(out of Cat Food=f) = {:.4f}\n".format(c1,1-c1))
# print("P(C=t) = {:.4f} | P(C=f) = {:.4f}\n ".format(c1,1-c1))
print("P(feeds his cat=t| watches TV=t,out of Cat Food=t) = {:.4f} | P(feeds his cat=f| watches TV=t,out of Cat Food=t) = {:.4f}".format(f1_g1c1, 1-f1_g1c1))
# print("P(F=t|G=t,C=t) = {:.4f} | P(F=f|G=t,C=t) = {:.4f}".format(f1_g1c1, 1-f1_g1c1))
print("P(feeds his cat=t| watches TV=t,out of Cat Food=f) = {:.4f} | P(feeds his cat=f| watches TV=t,out of Cat Food=f) = {:.4f}".format(f1_g1c0, 1-f1_g1c0))
# print("P(F=t|G=t,C=f) = {:.4f} | P(F=f|G=t,C=f) = {:.4f}".format(f1_g1c0, 1-f1_g1c0))
print("P(feeds his cat=t| watches TV=f,out of Cat Food=t) = {:.4f} | P(feeds his cat=f| watches TV=f,out of Cat Food=t) = {:.4f}".format(f1_g0c1, 1-f1_g0c1))
# print("P(F=t|G=f,C=t) = {:.4f} | P(F=f|G=f,C=t) = {:.4f}".format(f1_g0c1, 1-f1_g0c1))
print("P(feeds his cat=t| watches TV=f,out of Cat Food=f) = {:.4f} | P(feeds his cat=f| watches TV=f,out of Cat Food=f) = {:.4f}\n".format(f1_g0c0, 1-f1_g0c0))
# print("P(F=t|G=f,C=f) = {:.4f} | P(F=f|G=f,C=f) = {:.4f}\n".format(f1_g0c0, 1-f1_g0c0))

#task 2
def prob_fm_jpd(b_val, g_val, c_val, f_val):
    # P(b, c, g, f) = P(b) * P(g | b) * P(c) *  P(f | g, c)
    Pob = btable[b_val] / (btable[0] + btable[1])
    Pog_b = gtable[b_val][g_val] / btable[b_val]
    Poc = ctable[c_val] / (ctable[0] + ctable[1])
    Pof_gc = ftable[g_val][c_val][f_val] / (ftable[g_val][c_val][1] + ftable[g_val][c_val][0])
    prob = Pob * Pog_b * Poc * Pof_gc 
    return prob

if len(sys.argv) == 6:
    if sys.argv[2] == "Bt":
        B_in = 1
    elif sys.argv[2] == "Bf":
        B_in = 0
    else:
        print("invalid input at B value: pass Bt/Bf")
        exit()

    if sys.argv[3] == "Gt":
        G_in = 1
    elif sys.argv[3] == "Gf":
        G_in = 0
    else:
        print("invalid input at G value: pass Gt/Gf")
        exit()

    if sys.argv[4] == "Ct":
        C_in = 1
    elif sys.argv[4] == "Cf":
        C_in = 0
    else:
        print("invalid input at C value: pass Ct/Cf")
        exit()

    if sys.argv[5] == "Ft":
        F_in = 1
    elif sys.argv[5] == "Ff":
        F_in = 0
    else:
        print("invalid input at F value: pass Ft/Ff")
        exit()

    finalprob = prob_fm_jpd(B_in,G_in,C_in,F_in)
    print(f"---------------This is solution of task 2-----------------")
    print("Solution - P(Baseball Game on TV={},  watches TV={},  is out of Cat Food={},  feeds his cat={}) = {:.4f}".format(sys.argv[2][1:], sys.argv[3][1:], sys.argv[4][1:], sys.argv[5][1:], finalprob))

# task 3
def inference(query):
    if  "Bt" in query:
        B_in = [1]
    elif "Bf" in query:
        B_in = [0]
    else:
        B_in = [0, 1]
    
    if  "Gt" in query:
        G_in = [1]
    elif "Gf" in query:
        G_in = [0]
    else:
        G_in = [0, 1]

    if  "Ct" in query:
        C_in = [1]
    elif "Cf" in query:
        C_in = [0]
    else:
        C_in = [0, 1]
    
    if  "Ft" in query:
        F_in = [1]
    elif "Ff" in query:
        F_in = [0]
    else:
        F_in = [0, 1]
    
    qcount = 0
    for b in B_in:
        for g in G_in:
            for c in C_in:
                for f in F_in:
                    pof = prob_fm_jpd(b, g, c, f)
                    qcount += pof
    return qcount

query_vars = {}
evidence_vars = {}
if len(sys.argv) in [3,5]: 
    query_vars = sys.argv[2].split(",")
    query = inference(query_vars)
    if len(sys.argv) == 3:
        print(f"---------------This is solution of task 3-----------------")
        print(f"->This is the key for solution\nBt if B is true, Bf if B is false\nGt if G is true, Gf if G is false\nCt if C is true, Cf if C is false\nFt if F is true, Ff if F is false\n")
        print("Solution - P({}) = {:.4f}".format(query_vars, query))

    if len(sys.argv)==5 and sys.argv[3] == "given":
        evidence_vars = sys.argv[4].split(",")
        route = copy.deepcopy(query_vars)
        for t in range(len(evidence_vars)):
            query_vars.append(evidence_vars[t])
        query = inference(query_vars)
        evide = inference(evidence_vars)
        print(f"---------------this is solution of task 3-----------------")
        print(f"->This is the key for solution\nBt if B is true, Bf if B is false\nGt if G is true, Gf if G is false\nCt if C is true, Cf if C is false\nFt if F is true, Ff if F is false\n")
        print("Solution - P({}|{}) = {:.4f}".format(route, evidence_vars, query/evide))
    
    if len(sys.argv)==5 and sys.argv[3] != "given":
        print("Invalid input arguements for Task 3, Please use 'given' betweeen query and evidence vars")