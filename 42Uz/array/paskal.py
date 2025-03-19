def generate_row(prev):
    next_ = [1]
    for i in range(len(prev)-1):
        next_.append(prev[i]+ prev[i+1])
    next_.append(1)
    return next_

def generate(n: int) -> list:
    if n == 0:
        return []
    row = [1]
    result = [row]
    
    for i in range(n-1):
        row = generate_row(row)
        result.append(row)
    return result
print(generate(5))
