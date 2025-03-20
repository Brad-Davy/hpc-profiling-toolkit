python3 -m timeit -n 5 -r 1 -s "import julia_set" "julia_set.calc_pure_python(desired_width=1000, max_iterations=300)"
