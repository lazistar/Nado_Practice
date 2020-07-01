# for num in range(1,51):
#     n_week = open("{0}주차.txt".format(num), "w", encoding="utf8")
#     n_week.write("- {0} 주차 주간보고 -".format(num))
#     n_week.write("\n부서 :")
#     n_week.write("\n이름 :")
#     n_week.write("\n업무 요약 :")

# n_week.close()

for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")