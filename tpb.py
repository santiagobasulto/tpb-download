import urllib2
import argparse

TPB_TORRENT_URL = "http://torrents.thepiratebay.se"


def torrent_download_url(torrent_id):
    url = '%s/%s/%s.torrent' % (TPB_TORRENT_URL, torrent_id, torrent_id)
    return url


def download_torrent(torrent_id):
    url = torrent_download_url(torrent_id)
    u = urllib2.urlopen(url)
    torrent_file_name = '%s.torrent' % torrent_id
    torrent_file = open(torrent_file_name, 'w')
    print "Downloading %s.torrent" % torrent_id
    torrent_file.write(u.read())
    torrent_file.close()


def main(torrent_ids):
    print "Starting to download torrent files."
    for tid in torrent_ids:
        download_torrent(tid)
    print "Done downloading torrents."

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Downloads one or more torrent files from ThePirateBay.org'
    )
    parser.add_argument(
        'torrent_ids',
        metavar='Torrent-ID',
        type=int,
        nargs='+',
        help='One or more Torrent IDs to download'
    )

    args = parser.parse_args()
    main(args.torrent_ids)
