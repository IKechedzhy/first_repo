def caching_fibonacci():

    cache = {}
    
    def fibonacci(n):
        if n <= 0: 
            return 0
        elif n == 1: 
            return 1
        else:
            for key in cache.items():
                return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        # print(cache)
        return cache[n]
    
    return fibonacci
result = caching_fibonacci()
print(result(15))
 