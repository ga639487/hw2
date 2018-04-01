if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--source',
                       default='source.csv',
                       help='input source data file name')
    parser.add_argument('--query',
                        default='query.txt',
                        help='query file name')
    parser.add_argument('--output',
                        default='output.txt',
                        help='output file name')
    args = parser.parse_args()
    
    import csv
    target = []
    query = {}
    temp1 = []
    temp2 = []

    f1 = open(args.query, 'r')  
    for line in f1:
        line=line.strip('\n')
        target.append(line.split(' '))
    f = open(args.source, 'r')  
    for row in csv.reader(f):
        key = row[0]
        query[key] = row[1]
    #for k,v in query.items():
        #print(k,v)
    csv_writer = open(args.output, 'w')
    for i in range(len(target)):
        for j in range(0,len(target[i]),2): 
            for key in query:
                if target[i][j] in query[key]:
                    if j == 0:
                        temp1.append(key)
                    else:
                        temp2.append(key)
            if j == 2:
                x = set(temp1)
                y = set(temp2)
                temp2.clear()
                if target[i][1] == 'and':
                    a = x & y
                elif target[i][1] == 'or':
                    a = x | y
                elif target[i][1] == 'not':
                    a = x - y
            if j > 2:
                x = set(temp1)
                y = set(temp2)
                temp2.clear()
                if target[i][1] == 'and':
                    a = a & y
                elif target[i][1] == 'or':
                    a = a | y
                elif target[i][1] == 'not':
                    a = a - y
        ans = list(a)
        ans = list(map(int, ans))
        ans.sort()
        if ans == []:
            ans.append(0)
        print (ans)
        for item in ans:
            csv_writer.write("%s," % item)
        csv_writer.write('\n')
        temp1.clear()    
        