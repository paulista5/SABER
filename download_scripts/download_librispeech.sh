aria2c --dir=/tts_data/asrdata/librispeech_tars --input-file=librispeech_download_links.txt --log=download_log.txt --max-concurrent-downloads=3 --continue true --all-proxy=$http_proxy --max-connection-per-server=5 --max-tries=0