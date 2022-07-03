from indeed import get_jobs as get_indeed_jobs
from save import save_to_file

jobs = get_indeed_jobs()

save_to_file(jobs)

# from so import get_jobs as get_so_jobs

# stack_overflow_jobs = get_so_jobs()

# print(stack_overflow_jobs)