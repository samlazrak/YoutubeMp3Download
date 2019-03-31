import click
from pytube import YouTube

@click.group()
def main():
    """
    Simple CLI to download YouTube videos as Mp3s
    Use Python3 Converter.py download <video link>
    """
    pass

@main.command()
@click.argument('link')
def download(link):
  link = "+".join(link.split())

  yt = YouTube(link)
  click.echo("Dowloading " + yt.title)
  stream = yt.streams.filter(only_audio=True).first()
  stream.download()

  click.echo("All done!")

if __name__ == "__main__":
  main()