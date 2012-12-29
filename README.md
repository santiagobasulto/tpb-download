tpb-download
============

Some time ago, thepiratebay.org stopped providing URLs to download torrent files. That kind of pisses me off. So I made a simple script to download the torrent file you want. It's really easy to use.

Suppose you want to download this open-source, legal, torrent file: [Linux Mint 14 KDE (64-bit)](http://thepiratebay.se/torrent/7955698/Linux_Mint_14_KDE_(64-bit))

You just need to do:

    python tpb.py 7955698

That will download the torrent file and will name it `7955698.torrent`

If you don't want to clone the repository, or download the `tpb.py` file you can use this command:

    python  <(curl -s https://raw.github.com/santiagobasulto/tpb-download/master/tpb.py) 7955698

That's it! Really simple. Please use it at your own risk, and don't download illegal stuff.

**Disclaimer: This program is intended to use just for legal torrents (eg: Linux distros). The author has no relation with illegal downloads of copyrighted material or any other shit like that**
