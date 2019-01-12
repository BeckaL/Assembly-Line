from task_manager import Task_Manager

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('iterations')
    args = ap.parse_args()

    tm = Task_Manager()
    for i in range(int(args.iterations)):
        tm.allocate_resources()
    print tm.assembly_line.widgets_count

if __name__ == '__main__': main()
