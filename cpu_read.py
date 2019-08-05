import psutil

def get_percentage_CPU():

    list_with_CPU_utilization_percentage = psutil.cpu_percent(interval=0.5, percpu=True)
    return list_with_CPU_utilization_percentage


if __name__ == "__main__":
    
    list_with_CPU_utilization_percentage = []
    in_value = None
    print(psutil.cpu_times())

    while(in_value != '\n'):

        in_value = input("Enter \\n to exit: ")
        list_with_CPU_utilization_percentage = psutil.cpu_percent(interval=1, percpu=True)
        print(list_with_CPU_utilization_percentage)