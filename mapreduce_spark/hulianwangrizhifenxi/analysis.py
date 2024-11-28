import re
import os

# 1.编写程序进行页面访问量统计，结果保存至本地/root/internetlogs/pv/目录下part-00000文件中
# 指定要统计的页面列表
pages_to_track = {
    '/about',
    '/black-ip-list/',
    '/cassandra-clustor/',
    '/finance-rhive-repurchase/',
    '/hadoop-family-roadmap/',
    '/hadoop-hive-intro/',
    '/hadoop-zookeeper-intro/',
    '/hadoop-mahout-roadmap/',
}

# 创建一个字典来存储每个页面的访问次数
page_visits = {page: 0 for page in pages_to_track}

# 定义日志文件路径
log_file_path = './internetlogs/journal.log'

# 读取日志文件并处理每一行
with open(log_file_path, 'r') as file:
    for line in file:
        # 使用正则表达式匹配并提取访问资源
        match = re.search(r'"(\S+)\s+(\S+)\s+HTTP', line)
        if match:
            _, resource = match.groups()
            if resource in page_visits:
                page_visits[resource] += 1

# 结果保存路径
output_dir = './internetlogs/pv'
output_path = os.path.join(output_dir, 'part-00000')

# 如果目录不存在，则创建
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 将结果保存到指定的文件中
with open(output_path, 'w') as output_file:
    for page, count in page_visits.items():
        output_file.write(f"{page}\t{count}\n")

print("页面访问统计已完成，结果已保存至", output_path)


# 2.编写程序进行页面独立IP的访问量统计，结果保存至本地/root/internetlogs/ip/目录下part-00000文件中
# 例如1.80.249.223 1表示此IP访问量为1

# 指定要统计的页面列表
pages_to_track = [
    '/about',
    '/black-ip-list/',
    '/cassandra-clustor/',
    '/finance-rhive-repurchase/',
    '/hadoop-family-roadmap/',
    '/hadoop-hive-intro/',
    '/hadoop-zookeeper-intro/',
    '/hadoop-mahout-roadmap/',
]

# 创建一个字典来存储每个页面的访问次数
unique_ips_per_page = {}

# 读取日志文件并处理每一行
with open(log_file_path, 'r') as file:
    for line in file:
        # 使用正则表达式匹配并提取访问资源
        if len(line.split()) > 11:
            if line.split()[6] in pages_to_track:
                if int(line.split()[8]) <= 400:
                    if line.split()[0] not in unique_ips_per_page:
                        unique_ips_per_page[line.split()[0]] = 1
                    else:
                        unique_ips_per_page[line.split()[0]] += 1

# print(unique_ips_per_page)
# 结果保存路径
output_dir = './internetlogs/ip'
output_path = os.path.join(output_dir, 'part-00000')

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 将结果保存到指定的文件中
with open(output_path, 'w') as output_file:
    for ips, counts in unique_ips_per_page.items():
        output_file.write(f"{ips}\t{counts}\n")

print("页面独立IP访问统计已完成，结果已保存至", output_path)