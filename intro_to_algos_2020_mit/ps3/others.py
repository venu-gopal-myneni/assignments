
# Problem 3-1. [5 points]  Hash Practice 
A = [47, 61, 36, 52, 56, 33, 92]

def inf_seq():
    start =1
    while True:
        yield start
        start +=1
def hash1(ele,leng):
    return (10*ele+4)%leng
def hash2(ele,leng,c):
    return ((10*ele+4)%c)%leng
hashed_A = [hash1(ele,len(A)) for ele in A]
print(f"hashed A : {hashed_A}")
for c in inf_seq():
    hashed_A = [hash2(ele,len(A),c) for ele in A]
    if len(set(hashed_A)) == len(hashed_A):
        break
print(f"hashed A : {hashed_A}")
print(f"C : {c}")

