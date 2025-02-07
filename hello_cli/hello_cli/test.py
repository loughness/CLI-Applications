data = [
    {
        "#": 1,
        "AWS Region Name": "US East (N. Virginia)",
        "Region Code": "us-east-1",
        "Mean": "741 ms",
        "Median": "730 ms",
        "Min": "723 ms",
        "Max": "780 ms",
    },
    {
        "#": 2,
        "AWS Region Name": "US East (Ohio)",
        "Region Code": "us-east-2",
        "Mean": "525 ms",
        "Median": "530 ms",
        "Min": "244 ms",
        "Max": "797 ms",
    },
    {
        "#": 3,
        "AWS Region Name": "US West (N. California)",
        "Region Code": "us-west-1",
        "Mean": "540 ms",
        "Median": "535 ms",
        "Min": "270 ms",
        "Max": "819 ms",
    },
    {
        "#": 4,
        "AWS Region Name": "US West (Oregon)",
        "Region Code": "us-west-2",
        "Mean": "602 ms",
        "Median": "594 ms",
        "Min": "299 ms",
        "Max": "923 ms",
    },
    {
        "#": 5,
        "AWS Region Name": "Africa (Cape Town)",
        "Region Code": "af-south-1",
        "Mean": "632 ms",
        "Median": "627 ms",
        "Min": "320 ms",
        "Max": "953 ms",
    },
    {
        "#": 6,
        "AWS Region Name": "Asia Pacific (Melbourne)",
        "Region Code": "ap-southeast-4",
        "Mean": "599 ms",
        "Median": "598 ms",
        "Min": "296 ms",
        "Max": "905 ms",
    },
    {
        "#": 7,
        "AWS Region Name": "Asia Pacific (Hong Kong)",
        "Region Code": "ap-east-1",
        "Mean": "362 ms",
        "Median": "361 ms",
        "Min": "353 ms",
        "Max": "374 ms",
    },
]

print("\nAWS Ping Test results: ")
print("=========================")
for d in data:
    print(d["Region Code"], "\t", d["Mean"])


print("\nAWS Ping Test results: ")
print("=========================")
for d in data:
    ms = int(d["Mean"].replace(" ms", ""))
    ms_bar = round(ms / 10)
    print(d["Region Code"], "\t", "*" * ms_bar)

    def draw_bar(value, legend=None, char="❚"):
        if legend:
            print(legend, "\t", char * value)
        else:
            print(char * value)

print("\nAWS Ping Test results: ")
print("=========================")
for d in data:
    print(d["Region Code"], "\t", d["Mean"])


print("\nAWS Ping Test results: ")
print("=========================")
for d in data:
    ms = int(d["Mean"].replace(" ms", ""))
    ms_bar = round(ms / 10)
    # print(d["Region Code"], "\t", "*" * ms_bar)
    
    draw_bar(ms_bar, d["Region Code"])
    draw_bar(ms_bar, d["Region Code"], "☐")
    draw_bar(ms_bar, d["Region Code"], "░")