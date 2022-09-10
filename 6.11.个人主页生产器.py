import os

def main():
    name=input('Enter your name: ')
    describle=input('Descrinle yourself: ')

    file=open(r'D:\name.txt','w')
    file.write('<html>\n')
    file.write('<head>\n')
    file.write('</head>\n')
    file.write('<body>\n')
    file,write('    <center>\n')
    file.write(f'        <h1>{name}</h1>\n')
    file.write('    <\center>\n')
    file.write('    <hr />\n')
    file.write(f'    {describle}\n')
    file.write('<hr />\n')
    file.write('</body>\n')
    file.write('</html>')

    file.close()
    os.rename(r'D:\name.txt',r'D:\name.html')

if __name__=='__main__':
    main()
    
    
