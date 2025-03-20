import pstats

p = pstats.Stats("profile.stats")
x = p.sort_stats("cumulative")
print(vars(x))
