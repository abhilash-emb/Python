import requests
import argparse
import rich
from rich.progress import Progress
import time

def download_url(url, output_file):
    with Progress() as progress:
        rich.print(f'Downloading URL {url}')
        task = progress.add_task(f"Progress downloading URL", total=3)
        progress.advance(task)
        time.sleep(1)
        r = requests.get(url)
        time.sleep(1)
        progress.advance(task)
        if output_file:
            with open(output_file, "w") as f:
                f.write(r.text)
            time.sleep(1)
            progress.advance(task)

def get_output_file(url):
    return url.split("/")[-1]

def handle_download_from_url(args):
    output = args.output or get_output_file(args.input)
    download_url(args.input, output)

def handle_download_from_file(args):
    with open(args.input, "r") as f:
        urls = f.readlines()
        for url in urls:
            output = get_output_file(url)
            download_url(url, output)

def create_parser():
    parser = argparse.ArgumentParser(description="Wget program arguments")
    parser.add_argument("input", help="Input file or URL to download")
    parser.add_argument("-o", "--output", help="Output file name")
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    if args.input.startswith(("https", "wwww")):
        handle_download_from_url(args)
    else:
        handle_download_from_file(args)
        

if __name__ == "__main__":
    main()