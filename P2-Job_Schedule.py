def find_optimal_schedule (jobs):
    n = len (jobs)
    job_order = sorted(range(n), key=lambda x: -jobs [x][1] / jobs [x][0])
    schedule = []
    for job_index in job_order:
        schedule.append(jobs[job_index])
        total_time = sum(job[0] for job in schedule)
        if total_time > jobs[job_index][1]:
            schedule.remove(jobs [job_index]) # Remove the job if adding it exceeds the allowed time return schedule
    return schedule

def display_schedule(schedule):
    total_time = sum(job[0] for job in schedule)
    total_profit = sum(job[1] for job in schedule)
    print ("Optimal Schedule:")
    for index, job in enumerate(schedule):
        print(f"Job {index + 1}: Duration={job[0]}, Profit={job[1]}") 
    print(f"\nTotal Time: {total_time}") 
    print(f"Total Profit: {total_profit}")

jobs = [(3, 5), (4,6), (2, 2), (1, 8), (5, 10)] # Format: (duration, profit)
optimal_schedule = find_optimal_schedule(jobs)
display_schedule(optimal_schedule)