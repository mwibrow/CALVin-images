import os

svg_dir = 'svg'
url_template = 'https://raw.githubusercontent.com/mwibrow/CALVin-images/master/svg/{}?sanitize=true'
def main():
    cols = 6
    svgs = [svg for svg in os.listdir(svg_dir)
            if svg.endswith('svg')]
    with open(os.path.join(svg_dir, 'README.md'), 'w') as file_out:
        file_out.write('{}\n'.format('|' * (cols + 1)))
        file_out.write('{}|\n'.format(
            '|:---:' * cols))
        for i in range(0, len(svgs), cols):
            row = svgs[i:i+cols]
            file_out.write('|{}|\n'.format('|'.join(
                [svg.split(os.extsep)[0] for svg in row])))
            file_out.write('|{}|\n'.format('|'.join(
                ['<img width=64 height=64 src="{}"></img>'.format(url_template.format(svg))
                 for svg in row])))

if __name__ == '__main__':
    main()