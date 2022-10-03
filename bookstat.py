import argparse
import string
import time #elapsed time

start=time.time() #start for elapsed time

#input from command line
if __name__ == '__main__':
    parser=argparse.ArgumentParser(description="Print some book statistics")
    parser.add_argument('input_file', type=str, help="path of input file") #help option
    args=parser.parse_args()

def process(file_path):
    """Open a file and read/print text inside."""
    print(f'Opening input file: {file_path}')
    with open(file_path,'r',encoding='utf-8') as book: #with: open and close file
        text=book.read()
    print(text)

#alphabet=dict(zip(string.ascii_lowercase, range(1,27)))
process(args.input_file)

end=time.time() #end for elapsed time
print('Total elapsed time:', end-start)
