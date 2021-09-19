# the following lines are reserved for imports
#
#
import os


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child_path = os.path.join(path, filename)
            total += disk_usage(child_path)
    print('{0: < 7}'.format(total), path)
    return total


# driver code
if __name__ == '__main__':
    disk_usage('D:\Codes\DSA_Python')
